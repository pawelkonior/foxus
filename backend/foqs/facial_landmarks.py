from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2

from eye_tracking import track_eye

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

(l_start, l_end) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(r_start, r_end) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

zeros_landmarks = np.zeros((68, 2), dtype=int)

frame = []

response_dict = {"track": None, "back_video": None}


def detect_face(image):
    # image = cv2.imread(args["image"])
    try:
        image = imutils.resize(image, width=340)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except cv2.error:
        return zeros_landmarks, response_dict

    response_dict["back_video"] = 0

    # TODO query previous frame and change code for frame[0]
    chang_frame = imutils.resize(gray, width=100)
    if not frame:
        frame.append(chang_frame)
        delta_frame = chang_frame
    else:
        delta_frame = cv2.absdiff(frame[0], chang_frame)
        frame[0] = chang_frame

    _, thresh = cv2.threshold(delta_frame, 25, 255, cv2.THRESH_BINARY)
    thresh = cv2.dilate(thresh, None, iterations=2)

    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    for contour in contours:
        if cv2.contourArea(contour) > 30:
            response_dict["back_video"] = 2
            continue

    rects = detector(gray, 1)

    if len(rects) > 1:
        response_dict["back_video"] = 1

    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        (x, y, w, h) = face_utils.rect_to_bb(rect)

        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)

        if len(shape) == 68:
            for (x, y) in shape:
                cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

            left_eye = shape[l_start:l_end]
            right_eye = shape[r_start:r_end]
            eyes = [left_eye, right_eye]
            response_dict["track"] = track_eye(eyes, image)
            return shape, response_dict, image
        else:
            response_dict["track"] = 0

    return zeros_landmarks, response_dict, image  # TODO change the image

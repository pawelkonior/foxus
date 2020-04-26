from collections import OrderedDict

from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2

from foxus.face_analysis.eye_tracking import track_eye
from foxus.database import UserModel
from foxus import db

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

(l_start, l_end) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(r_start, r_end) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

zeros_landmarks = np.zeros((68, 2), dtype=int)

response_dict = {"track": None, "back_video": None, "eyebrow": None, "high-wid": None, "d1": None, "a1": None, "a2": None}

FACIAL_LANDMARKS_68_IDXS = OrderedDict([
    ("mouth", (48, 68)),
    ("inner_mouth", (60, 68)),
    ("right_eyebrow", (17, 22)),
    ("left_eyebrow", (22, 27)),
    ("right_eye", (36, 42)),
    ("left_eye", (42, 48)),
    ("nose", (27, 36)),
    ("jaw", (0, 17))
])


def json_face(landmarks):
    response = {}
    for (i, name) in enumerate(FACIAL_LANDMARKS_68_IDXS.keys()):
        (j, k) = FACIAL_LANDMARKS_68_IDXS[name]
        a = landmarks[j:k]
        response[name] = a.tolist()
    return response


def calculate_angle(a, b, c):
    ba = a - b
    bc = c - b
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)
    return np.degrees(angle)


def calculating_data(shape):
    dist_1 = np.linalg.norm(shape[42] - shape[45])
    dist_2 = np.linalg.norm(shape[43] - shape[47])
    dist_3 = np.linalg.norm(shape[26] - shape[45])
    d_smile = np.cross(shape[48]-shape[54], shape[54]-shape[57])/np.linalg.norm(shape[54]-shape[48])
    angle_1 = calculate_angle(shape[31], shape[48], shape[54])
    angle_2 = calculate_angle(shape[35], shape[54], shape[48])
    return dist_3 / dist_1, dist_2 / dist_1, d_smile, angle_1, angle_2


def detect_face(user, image):
    try:
        image = imutils.resize(image, width=340)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except cv2.error:
        return json_face(zeros_landmarks), response_dict

    user = UserModel.query.filter_by(user_id=user).first()

    response_dict["back_video"] = 0

    frame = user.frame_move

    chang_frame = imutils.resize(gray, width=100)
    if not frame:
        frame.append(chang_frame)
        delta_frame = chang_frame
    else:
        delta_frame = cv2.absdiff(frame[0], chang_frame)
        user.frame_move = chang_frame
        db.session.commit()

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

        if len(shape) == 68:
            left_eye = shape[l_start:l_end]
            right_eye = shape[r_start:r_end]
            eyes = [left_eye, right_eye]
            response_dict["track"] = track_eye(eyes, image)
            val_1, val_2, d1, a1, a2 = calculating_data(shape)
            response_dict["eyebrow"] = val_1
            response_dict["high-wid"] = val_2
            response_dict["d1"] = d1
            response_dict["a1"] = a1
            response_dict["a2"] = a2
            return json_face(shape), response_dict
        else:
            response_dict["track"] = 0

    return json_face(zeros_landmarks), response_dict

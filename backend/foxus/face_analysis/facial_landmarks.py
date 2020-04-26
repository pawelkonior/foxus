import base64
import json
from collections import OrderedDict

from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2

from foxus.face_analysis.eye_tracking import track_eye
# from foxus.database import UserModel, add_user

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

(l_start, l_end) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(r_start, r_end) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

zeros_landmarks = np.zeros((68, 2), dtype=int)

frame = []

inactive_dict = {"track": 0, "back_video": 1, "eyebrow": 0, "high-wid": 0, "d1": 0, "a1": 0, "a2": 0}

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
    return json.dumps(response)


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

def show_edges(img, x, y, w, color):
    cv2.line(img, (x, y), (x, y + int(0.3 * w)), color, 1)
    cv2.line(img, (x, y), (x + int(0.3 * w), y), color, 1)

    cv2.line(img, (x, y + w), (x, y + int(0.7 * w)), color, 1)
    cv2.line(img, (x, y + w), (x + int(0.3 * w), y + w), color, 1)

    cv2.line(img, (x + w, y), (x + int(0.7 * w), y), color, 1)
    cv2.line(img, (x + w, y), (x + w, y + int(0.3 * w)), color, 1)

    cv2.line(img, (x + w, y + w), (x + w, y + int(0.7 * w)), color, 1)
    cv2.line(img, (x + w, y + w), (x + int(0.7 * w), y + w), color, 1)


def print_line(roi_color, point_1, point_2):
    cv2.line(roi_color, (point_1[0], point_1[1]), (point_2[0], point_2[1]), (20, 255, 57), 1)

def print_schema(points, roi_color):
    print_line(roi_color, points[42], points[45])
    print_line(roi_color, points[43], points[47])
    print_line(roi_color, points[48], points[31])
    print_line(roi_color, points[54], points[35])
    print_line(roi_color, points[54], points[57])
    print_line(roi_color, points[57], points[48])
    print_line(roi_color, points[48], points[50])
    print_line(roi_color, points[50], points[51])

    print_line(roi_color, points[51], points[52])
    print_line(roi_color, points[52], points[54])


def detect_face(user_id, image):

    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except cv2.error:
        a, g = cv2.imencode('.jpeg', image)
        a = g.tobytes()
        a = base64.b64encode(a)
        a = 'data:image/jpeg;base64,' + a.decode()
        return a, inactive_dict

    # user = UserModel.query.filter_by(user_id=user_id).first()
    # if user is None:
    #     add_user(user_id)

    # else:
    #     user.count = (user.count + 1) % 180
    chang_frame = imutils.resize(gray, width=100)
    response_dict = inactive_dict
    if not frame:
        frame.append(chang_frame)
    else:

        delta_frame = cv2.absdiff(frame[0], chang_frame)
        frame[0] = chang_frame

        _, thresh = cv2.threshold(delta_frame, 25, 255, cv2.THRESH_BINARY)
        thresh = cv2.dilate(thresh, None, iterations=2)

        contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)

        for contour in contours:
            if cv2.contourArea(contour) > 30:
                response_dict["back_video"] = 1
                continue

    rects = detector(gray, 0)



    if len(rects) > 1:
        response_dict["back_video"] = 2

    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        show_edges(image, x, y, w, (20, 255, 57))
        if len(shape) == 68:
            for (x, y) in shape:
                cv2.circle(image, (x, y), 1, (20, 255, 57), -1)
            #print_schema(shape, image)
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

            a, g = cv2.imencode('.jpeg', image)
            a = g.tobytes()
            a = base64.b64encode(a)
            a = 'data:image/jpeg;base64,' + a.decode()
            return a, response_dict

    a, g = cv2.imencode('.jpeg', image)
    a = g.tobytes()
    a = base64.b64encode(a)
    a = 'data:image/jpeg;base64,' + a.decode()
    return a, inactive_dict

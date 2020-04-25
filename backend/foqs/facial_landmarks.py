from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2

from eye_tracking import track_eye


ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True)
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

image = cv2.imread(args["image"])

image = imutils.resize(image, width=340)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rects = detector(gray, 1)

(l_start, l_end) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(r_start, r_end) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

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
        track_state = track_eye(eyes, image)
        print(track_state)
    else:
        print("Not enough points for analysis")
cv2.imwrite("new_photo.jpg", image)

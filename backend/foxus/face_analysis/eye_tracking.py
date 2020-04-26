"""
Function to detect iris and pupil

eye_status for single eye:
1 - pupil not found
2 - eye closed/looking down
3 - looking left
4 - looking right
5 - looking forward

:return 0 - pupil not found
        1 - looking somewhere else
        2 - looking forward
"""
import numpy as np
import cv2


def track_eye(eyes, image):
    eye_state = [0]
    for index, eye in enumerate(eyes):
        left_edge = eye[0]
        right_edge = eye[3]
        top_eye = eye[1]
        bottom_eye = eye[4]

        eye_width = right_edge[0] - left_edge[0]
        eye_height = bottom_eye[1] - top_eye[1]

        eye_x1 = int(left_edge[0] - 0 * eye_width)
        eye_x2 = int(right_edge[0] + 0 * eye_height)

        eye_y1 = int(top_eye[1] - 1 * eye_height)
        eye_y2 = int(bottom_eye[1] + 1 * eye_height)

        roi = image[eye_y1:eye_y2, eye_x1:eye_x2]

        if eye_width / eye_height > 0.3:
            try:
                gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            except cv2.error:
                return 0
            blur = cv2.medianBlur(gray, 3)
            equ = cv2.equalizeHist(blur)
            thres = cv2.inRange(equ, 0, 15)
            kernel = np.ones((3, 3), np.uint8)

            dilation = cv2.dilate(thres, kernel, iterations=2)

            erosion = cv2.erode(dilation, kernel, iterations=3)

            contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

            pupil_found = True if len(contours) == 1 else False

            if pupil_found:
                eye_state.append(2)
            else:
                eye_state.append(1)
        else:
            eye_state.append(1)
    return max(eye_state)

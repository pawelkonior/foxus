import cv2
import argparse

from facial_landmarks import   detect_face

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

cap = cv2.VideoCapture(args["image"])
while cap.isOpened():
    ret, image = cap.read()
    if not ret:
        break
    landmark, database_data, image = detect_face(image)
    print(landmark)
    cv2.imshow('frame2', image)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
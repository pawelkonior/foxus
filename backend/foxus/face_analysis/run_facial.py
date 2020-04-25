import cv2
import base64
import numpy as np

from foxus.face_analysis.facial_landmarks import detect_face

img = cv2.imread("pawel1.jpg")

def render_face(user, img):
	# encoded_image = img.split(",")[1]
	# img = base64.b64decode(encoded_image)
	# image = np.frombuffer(img, dtype="uint8")
	# img = cv2.imdecode(image, cv2.IMREAD_COLOR)[1]

	landmark, database_data = detect_face(img)
	print(database_data)
	# TODO add to db
	return landmark

render_face(1, img)


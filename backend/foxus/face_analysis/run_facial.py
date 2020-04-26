import cv2
import base64
import numpy as np

from foxus.face_analysis.facial_landmarks import detect_face
from foxus.database import DataModel
from foxus import db


def render_face(user, img):
    encoded_image = img.split(",")[1]
    img = base64.b64decode(encoded_image)
    image = np.frombuffer(img, dtype="uint8")
    img = cv2.imdecode(image, cv2.IMREAD_COLOR)[1]

    landmark, database_data = detect_face(user, img)

    data_entry = DataModel(
        user_id=user,
        back_move=database_data['back_video'],
        eye_track=database_data['track'],
        eyebrow=database_data['eyebrow'],
        high_width=database_data['high-wid'],
        d=database_data['d1'],
        a1=database_data['a1'],
        a2=database_data['a2'],
    )
    db.session.add(data_entry)
    db.session.commit()
    return landmark

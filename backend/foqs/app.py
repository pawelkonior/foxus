import glob

import dlib as dlib
import imutils as imutils
from imutils import face_utils
import cv2
import numpy as np
from matplotlib import pyplot as plt
from landmask_detection import calculate_parameters_left, calculate_parameters_right


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


def draw_plots(emot, img, first, second, plot, lab_1, lab_2, left, right):
    x = range(len(left))
    y_1 = [n[first] for n in left]
    y_2 = [n[second] for n in left]
    y_3 = [n[first] for n in right]
    y_4 = [n[second] for n in right]
    plt.plot(x, y_1, color='blue')
    plt.plot(x, y_2, color='orange')
    plt.plot(x, y_3, color='red')
    plt.plot(x, y_4, color='green')
    plt.title(f"{emot}-{plot}-{img}")
    plt.legend([f"lewe {lab_1}", f"lewe_{lab_2}", f"prawe_{lab_1}", f"prawe_{lab_2}"])
    plt.savefig(f"{emot}-{plot}-{img}.png")
    plt.close()


for video in glob.glob("/home/kasia/Dokumenty/projekt/face_recognition/bau/boredom/*.mp4"):# 	print(img[0])

    img = video.split("/")[-1]
    img = img.split(".")[0]
    print(img)
    cap = cv2.VideoCapture(video)
    left = []
    right = []
    k = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            try:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            except:
                continue
            else:
                rects = detector(gray, 1)

                for (i, rect) in enumerate(rects):

                    shape = predictor(gray, rect)
                    shape = face_utils.shape_to_np(shape)

                    left.append(calculate_parameters_left(shape))
                    right.append(calculate_parameters_right(shape))
        else:
            break
    cap.release()

    draw_plots("bored", img, 0, 1, "skupienie", "wysokosc", "stosunek", left, right)
    draw_plots("bored", img, 0, 2, "zaciekawienie", "wysokosc", "kacik", left, right)
    draw_plots("bored", img, 3, 4, "znuzenie_1", "wewn", "brew_wew", left, right)
    draw_plots("bored", img, 0, 5, "znuzenie_2", "wysokosc", "brew", left, right)
    draw_plots("bored", img, 6, 7, "sen", "oko1", "oko2", left, right)

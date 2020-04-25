import numpy as np


def middle_point(point_1, point_2):
    return np.mean([point_1, point_2], axis=0, dtype=int)


def calculate_parameters_left(shape):
    dist_1 = np.linalg.norm(middle_point(shape[44], shape[43])-middle_point(shape[46], shape[47]))
    dist_2 = np.linalg.norm(shape[42]-shape[45])
    dist_3 = np.linalg.norm(shape[43]-shape[47])
    dist_4 = np.linalg.norm(shape[26]-shape[45])
    dist_5 = np.linalg.norm(shape[23]-shape[43])
    dist_6 = np.linalg.norm(shape[24]-shape[44])
    return [dist_1/dist_2, dist_3/dist_1, dist_4/dist_2, dist_3/dist_2, dist_5/dist_2, dist_6/dist_2, dist_3, dist_2]


def calculate_parameters_right(shape):
    dist_1 = np.linalg.norm(middle_point(shape[38], shape[37])-middle_point(shape[40], shape[41]))
    dist_2 = np.linalg.norm(shape[36]-shape[39])
    dist_3 = np.linalg.norm(shape[38]-shape[40])
    dist_4 = np.linalg.norm(shape[17]-shape[36])
    dist_5 = np.linalg.norm(shape[20]-shape[38])
    dist_6 = np.linalg.norm(shape[19]-shape[37])
    return [dist_1/dist_2, dist_3/dist_1, dist_4/dist_2, dist_3/dist_2, dist_5/dist_2, dist_6/dist_2, dist_3, dist_2]

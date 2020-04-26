from foxus.database import UserModel, DataModel
from foxus import db


def calculate_mean(user_id):
    data = DataModel.query.filter_by(user_id=user_id).all()

    mean_eyebrow = [n.__dict__["mean_eyebrow"] for n in data if n.__dict__["mean_eyebrow"] is not None]
    mean_high_width = [n.__dict__["mean_high_width"] for n in data if n.__dict__["mean_high_width"] is not None]
    mean_d = [n.__dict__["mean_d"] for n in data if n.__dict__["mean_d"] is not None]
    mean_a1 = [n.__dict__["mean_a1"] for n in data if n.__dict__["mean_a1"] is not None]
    mean_a2 = [n.__dict__["mean_a2"] for n in data if n.__dict__["mean_a2"] is not None]

    mean_eyebrow = sum(mean_eyebrow) / len(mean_eyebrow)
    mean_high_width = sum(mean_high_width) / len(mean_high_width)
    mean_d = sum(mean_d) / len(mean_d)
    mean_a1 = sum(mean_a1) / len(mean_a1)
    mean_a2 = sum(mean_a2) / len(mean_a2)

    user = UserModel.query.filter_by(user_id=user_id).first()
    user.mean_eyebrow = mean_eyebrow
    user.mean_high_width = mean_high_width
    user.mean_d = mean_d
    user.mean_a1 = mean_a1
    user.mean_a2 = mean_a2
    db.session.commit()


FRAME_LEVELS = {2: 1, 3: 4, 4: 4, 5: 3, 6: 2}
SMILE_LEVELS = {0: 0, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 3}


def calculate_status(user_id):
    data = UserModel.query.filter_by(user_id=user_id).order_by(UserModel.id.desc()).limit(30)

    eyebrow = [n.__dict__["eyebrow"] for n in data if n.__dict__["eyebrow"] is not None]
    high_width = [n.__dict__["high_width"] for n in data if n.__dict__["high_width"] is not None]
    eye_track = [n.__dict__["eye_track"] for n in data if n.__dict__["eye_track"] is not None]
    back_move = [n.__dict__["back_move"] for n in data if n.__dict__["back_move"] is not None]

    eyebrow = sum(eyebrow) / len(eyebrow)
    high_width = sum(high_width) / len(high_width)
    eye_track = sum(eye_track) / len(eye_track)
    back_move = sum(back_move)

    back_move_status = 0 if back_move >= 0 else 1
    user = UserModel.query.filter_by(user_id=user_id).first()

    eyebrow_ration = eyebrow / user.mean_eyebrow
    high_width = high_width / user.mean_high_width

    eye_score = 3 if eyebrow_ration > 1.04 else 1 if eyebrow_ration < 0.96 else 2
    high_score = 1 if high_width > 1.04 else 3 if high_width < 0.96 else 2

    status = eye_score + high_score
    focus = user.focus + user.focus * (status + back_move_status + eye_track - 5) * 2 / 100

    user.focus = focus
    db.session.commit()

    return FRAME_LEVELS[status], focus


def calculate_smile(user_id):
    data = UserModel.query.filter_by(user_id=user_id).order_by(UserModel.id.desc()).limit(30)

    d = [n.__dict__["d"] for n in data if n.__dict__["d"] is not None]
    a1 = [n.__dict__["a1"] for n in data if n.__dict__["a1"] is not None]
    a2 = [n.__dict__["a2"] for n in data if n.__dict__["a2"] is not None]

    d = sum(d) / len(d)
    a1 = sum(a1) / len(a1)
    a2 = sum(a2) / len(a2)

    user = UserModel.query.filter_by(user_id=user_id).first()

    d = d / user.mean_d
    a1 = a1 / user.mean_a1
    a2 = a2 / user.mean_a2

    status_d = 0 if d <= 1 else 1 if d < 1.2 else 3 if d < 1.35 else 3
    status_a1 = 2 if a1 > 1.15 else 1 if a1 > 1 else 0
    status_a2 = 2 if a2 > 1.15 else 1 if a2 > 1 else 0

    return SMILE_LEVELS[status_d + status_a1 + status_a2]


def calculate_data(user_id):
    user = UserModel.query.filter_by(user_id=user_id).first()
    if user.mean_eyebrow is None and user.count < 120:
        return {"idx": user, "focused": 50, "status": 3, "smile": 1}
    elif user.mean_eyebrow is None and user.count >= 120:
        calculate_mean(user_id)
        return {"idx": user, "focused": 50, "status": 3, "smile": 1}
    status, focus = calculate_status(user_id)
    smile = calculate_smile(user_id)
    return {"idx": user_id, "status": status, "focus": focus, "smile": smile}

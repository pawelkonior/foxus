#from foxus.database import UserModel, DataModel
#from foxus import db


FRAME_LEVELS = {1: 1, 2: 1, 3: 4, 4: 3, 5: 3, 6: 2}
SMILE_LEVELS = {0: 0, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 3}
FOCUS_LEVELS = {0: -4, 1: -3, 2: -2, 3: -1, 4: -0.5, 5: 1, 6: 2, 7: 3, 8: 4}


def calculate_mean(user_id):
    data = DataModel.query.filter_by(user_id=user_id).all()

    mean_eyebrow = [n.__dict__["eyebrow"] for n in data]
    mean_high_width = [n.__dict__["high_width"] for n in data]
    mean_d = [n.__dict__["d"] for n in data]
    mean_a1 = [n.__dict__["a1"] for n in data]
    mean_a2 = [n.__dict__["a2"] for n in data]

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


def calculate_status(user_id):
    data = DataModel.query.filter_by(user_id=user_id).order_by(DataModel.id.desc()).limit(30)

    eyebrow = [n.__dict__["eyebrow"] for n in data]
    high_width = [n.__dict__["high_width"] for n in data]
    eye_track = [n.__dict__["eye_track"] for n in data]
    back_move = [n.__dict__["back_move"] for n in data]

    eyebrow = sum(eyebrow) / len(eyebrow)
    high_width = sum(high_width) / len(high_width)
    eye_track = sum(eye_track) / len(eye_track)
    back_move = sum(back_move)

    back_move_status = 0 if back_move >= 0 else 1
    user = UserModel.query.filter_by(user_id=user_id).first()

    eyebrow_ration = eyebrow / user.mean_eyebrow
    high_width = high_width / user.mean_high_width
    eye_score = 1 if eyebrow_ration > 1.09 else 3 if eyebrow_ration < 1.00 else 2
    high_score = 3 if high_width > 0.92 else 0 if high_width < 0.9 else 2

    status = eye_score + high_score
    focus = user.focus + user.focus * (FOCUS_LEVELS[int(round(status + back_move_status + eye_track))]) / 100
    focus = min(focus, 100)
    focus = max(focus, 0)

    user.focus = focus
    db.session.commit()

    d = [n.__dict__["d"] for n in data]
    a1 = [n.__dict__["a1"] for n in data]
    a2 = [n.__dict__["a2"] for n in data]

    d = sum(d) / len(d)
    a1 = sum(a1) / len(a1)
    a2 = sum(a2) / len(a2)


    d = d / user.mean_d
    a1 = a1 / user.mean_a1
    a2 = a2 / user.mean_a2

    status_d = 0 if d <= 0.9 else 1 if d < 1.1 else 2 if d < 1.35 else 3
    status_a1 = 2 if a1 < 0.85 else 1 if a1 < 1 else 0
    status_a2 = 2 if a2 < 0.85 else 1 if a2 < 1 else 0

    return FRAME_LEVELS[status], focus, SMILE_LEVELS[status_d + status_a1 + status_a2]


def calculate_data(user_id):
    user = UserModel.query.filter_by(user_id=user_id).first()

    time_interval = 120
    if user.mean_eyebrow is None and user.count < time_interval:
        return {"idx": user_id, "focused": 50, "status": 3, "smile": 1}
    elif user.mean_eyebrow is None and user.count >= time_interval:
        calculate_mean(user_id)
        return {"idx": user_id, "focused": 50, "status": 3, "smile": 1}

    status, focus, smile = calculate_status(user_id)
    return {"idx": user_id, "status": status, "focus": focus, "smile": smile}

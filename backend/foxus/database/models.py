from foxus import db


class DataModel(db.Model):
    __tablename__ = 'user_frame'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    back_move = db.Column(db.Integer)
    eye_track = db.Column(db.Integer)
    eyebrow = db.Column(db.Float)
    high_width = db.Column(db.Float)
    d = db.Column(db.Float)
    a1 = db.Column(db.Float)
    a2 = db.Column(db.Float)


class UserModel(db.Model):
    __tablename__ = 'user_data'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    frame_move = db.Column(db.Text)
    frame_user = db.Column(db.Text)
    count = db.Column(db.Integer, default=0)
    mean_eyebrow = db.Column(db.Float)
    mean_high_width = db.Column(db.Float)
    mean_d = db.Column(db.Float)
    mean_a1 = db.Column(db.Float)
    mean_a2 = db.Column(db.Float)
    focus = db.Column(db.Integer)


def uuid(idx):
    def inner(new_id=None):
        nonlocal idx
        idx += 1
        return idx if new_id is None else new_id
    return inner


uid = uuid(0)


def add_user():
    user = UserModel(user_id=uid(), name="Pawel", focus=60)
    db.session.add(user)
    db.session.commit()

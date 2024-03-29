from application import db, login_manager, bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    email_address = db.Column(db.String())
    password_hash = db.Column(db.String())
    age = db.Column(db.Integer)
    sex = db.Column(db.Integer)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    sys_bp = db.Column(db.Integer)
    dia_bp = db.Column(db.Integer)
    glucose = db.Column(db.Integer)
    tot_chol = db.Column(db.Integer)
    cigs_per_day = db.Column(db.Integer)
    prevalent_hyp = db.Column(db.Integer)
    bp_meds = db.Column(db.Integer)
    diabetes = db.Column(db.Integer)
    education = db.Column(db.Integer)
    current_smoker = db.Column(db.Integer)
    heart_rate = db.Column(db.Integer)
    prevalent_stroke = db.Column(db.Integer)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password_correction(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

from application import db, login_manager
from application import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    f_name = db.Column(db.String(length=30), nullable=True)
    l_name = db.Column(db.String(length=30), nullable=True)
    dob = db.Column(db.String(length=30), nullable=True)
    sex = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
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
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

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
    password = db.Column(db.String(length=60), nullable=False)
    f_name = db.Column(db.String)
    l_name = db.Column(db.String)
    dob = db.Column(db.String)
    sex = db.Column(db.String)
    weight = db.Column(db.String)
    height = db.Column(db.String)
    sys_bp = db.Column(db.String)
    dia_bp = db.Column(db.String)
    glucose = db.Column(db.String)
    tot_chol = db.Column(db.String)
    cigs_per_day = db.Column(db.String)
    prevalent_hyp = db.Column(db.String)
    bp_meds = db.Column(db.String)
    diabetes = db.Column(db.String)
    education = db.Column(db.String)
    current_smoker = db.Column(db.String)
    heart_rate = db.Column(db.String)
    prevalent_stroke = db.Column(db.String)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password, attempted_password)

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
    fName = db.Column(db.String)
    lName = db.Column(db.String)
    dob = db.Column(db.String)
    sex = db.Column(db.String)
    weight = db.Column(db.String)
    height = db.Column(db.String)
    sysBP = db.Column(db.String)
    diaBP = db.Column(db.String)
    glucose = db.Column(db.String)
    totChol = db.Column(db.String)
    cigsPerDay = db.Column(db.String)
    prevalentHyp = db.Column(db.String)
    BPMeds = db.Column(db.String)
    diabetes = db.Column(db.String)
    education = db.Column(db.String)
    currentSmoker = db.Column(db.String)
    heartRate = db.Column(db.String)
    prevalentStroke = db.Column(db.String)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from application.models import Users


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = Users.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = Users.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class MonitorForm(FlaskForm):
    age = IntegerField('Age in Years:', validators=[DataRequired()])
    sex = SelectField('Sex:', validators=[DataRequired()], choices=[(1, 'Male'), (0, 'Female')])
    height = IntegerField('Height m:', validators=[DataRequired()])
    weight = IntegerField('Weight kg:', validators=[DataRequired()])
    sys_bp = IntegerField('Systolic BP mmHg:', validators=[DataRequired()])
    dia_bp = IntegerField('Diastolic BP mmHg:', validators=[DataRequired()])
    glucose = IntegerField('Glucose mg/dL:', validators=[DataRequired()])
    tot_chol = IntegerField('Total Cholesterol mg/dL:', validators=[DataRequired()])
    cigs_per_day = IntegerField('Number of cigarettes:')
    prevalent_hyp = SelectField('Previous Hypertensive:', validators=[DataRequired()], choices=[(0, 'No'), (1, 'Yes')])
    bp_meds = SelectField('BP Medication:', validators=[DataRequired()], choices=[(0, 'No'), (1, 'Yes')])
    diabetes = SelectField('Diabetes:', validators=[DataRequired()], choices=[(0, 'No'), (1, 'Yes')])
    education = SelectField('Education:', validators=[DataRequired()],
                            choices=[(1, 'High School'), (2, 'GED'), (3, 'Vocational School'),
                                     (4, 'College')])
    current_smoker = SelectField('Current Smoker:', validators=[DataRequired()], choices=[(0, 'No'), (1, 'Yes')])
    heart_rate = IntegerField('Heart Rate BPM:', validators=[DataRequired()])
    prevalent_stroke = SelectField('Previous Stroke:', validators=[DataRequired()], choices=[(0, 'No'), (1, 'Yes')])
    submit = SubmitField(label='Monitor My Health')

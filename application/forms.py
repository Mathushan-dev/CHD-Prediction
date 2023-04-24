from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from application.models import Users


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = Users.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('An account with this username already exists')

    def validate_email_address(self, email_address_to_check):
        email_address = Users.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('An account with the same email address exists')

    username = StringField(label='username:', validators=[Length(min=1, max=20), DataRequired()])
    email_address = StringField(label='email_address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='password:', validators=[Length(min=7), DataRequired()])
    password2 = PasswordField(label='password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='submit')


class LoginForm(FlaskForm):
    username = StringField(label='username:', validators=[DataRequired()])
    password = PasswordField(label='password:', validators=[DataRequired()])
    submit = SubmitField(label='submit')


class MonitorForm(FlaskForm):
    age = IntegerField('Age in Years:', validators=[DataRequired()])
    sex = SelectField('Sex:', validators=[DataRequired()], choices=[(1, 'Male'), (0, 'Female')])
    height = IntegerField('Height cm:', validators=[DataRequired()])
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


class MonitorFitbitForm(FlaskForm):
    submit = SubmitField(label='Monitor My Health')

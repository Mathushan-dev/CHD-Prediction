from application import app
from application.prediction import predict
from flask import render_template, redirect, url_for, flash, request, session
from application.models import Users
from application.forms import RegisterForm, LoginForm, MonitorForm
from application import db
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = Users(username=form.username.data,
                               email_address=form.email_address.data,
                               password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category='success')
        return redirect('/monitor')

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = Users.query.filter_by(username=form.username.data).first()

        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect('/home')

        else:
            flash('Username and password are not match! Please try again', category='danger')

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with logging in: {err_msg}', category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return render_template('home.html')


def extract_health_factors(form):
    return {"age": form.age.data, "sex": form.sex.data.strip(), "height": form.height.data,
            "weight": form.weight.data, "prevalent_stroke": form.prevalent_stroke.data, "sys_bp": form.sys_bp.data,
            "dia_bp": form.dia_bp.data, "glucose": form.glucose.data, "tot_chol": form.tot_chol.data,
            "cigs_per_day": form.cigs_per_day.data, "prevalent_hyp": form.prevalent_hyp.data,
            "bp_meds": form.bp_meds.data, "diabetes": form.diabetes.data, "education": form.education.data,
            "current_smoker": form.current_smoker.data, "heart_rate": form.heart_rate.data}


def save_to_database(health_factors):
    current_user.age = health_factors['age']
    current_user.sex = health_factors['sex']
    current_user.height = health_factors['height']
    current_user.weight = health_factors['weight']
    current_user.prevalent_stroke = health_factors['prevalent_stroke']
    current_user.sys_bp = health_factors['sys_bp']
    current_user.dia_bp = health_factors['dia_bp']
    current_user.glucose = health_factors['glucose']
    current_user.tot_chol = health_factors['tot_chol']
    current_user.cigs_per_day = health_factors['cigs_per_day']
    current_user.prevalent_hyp = health_factors['prevalent_hyp']
    current_user.bp_meds = health_factors['bp_meds']
    current_user.diabetes = health_factors['diabetes']
    current_user.education = health_factors['education']
    current_user.current_smoker = health_factors['current_smoker']
    current_user.heart_rate = health_factors['heart_rate']
    db.session.commit()
    return


@app.route('/monitor', methods=['GET', 'POST'])
@login_required
def monitor_page():
    form = MonitorForm()
    if form.validate_on_submit():
        health_factors = extract_health_factors(form)
        save_to_database(health_factors)
        prediction = predict(health_factors)
        return result_page(prediction)

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with monitoring your health: {err_msg}', category='danger')

    return render_template('monitor.html', form=form)


@app.route('/monitor_fitbit', methods=['GET', 'POST'])
@login_required
def monitor_fitbit_page():
    form = MonitorForm()
    if form.validate_on_submit():
        health_factors = extract_health_factors(form)
        save_to_database(health_factors)
        prediction = predict(health_factors)
        return result_page(prediction)

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with monitoring your health: {err_msg}', category='danger')

    return render_template('monitor_fitbit.html', form=form, id=current_user.email_address)


@app.route('/result', methods=['GET', 'POST'])
@login_required
def result_page(prediction):
    return render_template('result.html', prediction=prediction)

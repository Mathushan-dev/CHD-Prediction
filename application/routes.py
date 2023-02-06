import json

import requests
from flask import render_template, redirect, flash
from flask_login import login_user, logout_user, login_required, current_user
from requests.structures import CaseInsensitiveDict

from application import app, db
from application.forms import RegisterForm, LoginForm, MonitorForm, MonitorFitbitForm
from application.models import Users
from application.prediction import predict, predict_fitbit


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register_page(debug_form=False):
    form = RegisterForm()
    if form.validate_on_submit() or debug_form:
        if not debug_form:
            user_to_create = Users(username=form.username.data,
                                   email_address=form.email_address.data,
                                   password=form.password1.data)
        else:
            user_to_create = Users(username="test_debug",
                                   email_address="test_debug@test_debug.com",
                                   password="test_debug_password")
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category='success')
        return redirect('/home')

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page(debug_form=False):
    form = LoginForm()
    if form.validate_on_submit() or debug_form:
        if debug_form:
            attempted_user = Users.query.filter_by(username="test_debug").first()
            password = "test_debug_password"
        else:
            attempted_user = Users.query.filter_by(username=form.username.data).first()
            password = form.password.data

        if attempted_user and attempted_user.check_password_correction(attempted_password=password):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect('/home')

        else:
            flash('Username and password are not match! Please try again', category='danger')

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with logging in: {err_msg}', category='danger')

    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout_page(debug=False):
    if debug:
        login_page(debug_form=True)
    if not current_user.is_authenticated:
        return redirect('/login')
    logout_user()
    flash("You have been logged out!", category='info')
    return render_template('home.html')


def extract_from_form(form, fitbit=False, debug=False):
    if not fitbit:
        return {"age": form.age.data, "sex": form.sex.data.strip(), "height": form.height.data,
                "weight": form.weight.data, "prevalent_stroke": form.prevalent_stroke.data, "sys_bp": form.sys_bp.data,
                "dia_bp": form.dia_bp.data, "glucose": form.glucose.data, "tot_chol": form.tot_chol.data,
                "cigs_per_day": form.cigs_per_day.data, "prevalent_hyp": form.prevalent_hyp.data,
                "bp_meds": form.bp_meds.data, "diabetes": form.diabetes.data, "education": form.education.data,
                "current_smoker": form.current_smoker.data, "heart_rate": form.heart_rate.data}

    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    heights_data = requests.get("https://api.zivacare.com/api/v2/human/heights?access_token=demo",
                                headers=headers).json()
    heights_value = str(json.loads(list(heights_data.values())[0][-1])["value"])

    weights_data = requests.get("https://api.zivacare.com/api/v2/human/weights?access_token=demo",
                                headers=headers).json()
    weights_value = str(json.loads(list(weights_data.values())[0][-1])["value"])

    pressures_data = requests.get("https://api.zivacare.com/api/v2/human/blood_pressures?access_token=demo",
                                  headers=headers).json()
    systolic_value = str(json.loads(list(pressures_data.values())[0][-1])["systolic"])
    diastolic_value = str(json.loads(list(pressures_data.values())[0][-1])["diastolic"])
    heart_rate_value = str(json.loads(list(pressures_data.values())[0][-1])["heart_rate"])

    glucoses_data = requests.get("https://api.zivacare.com/api/v2/human/blood_glucoses?access_token=demo",
                                 headers=headers).json()
    glucose_value = str(json.loads(list(glucoses_data.values())[0][-1])["value"])

    if debug:
        return {"height": int(float(heights_value)), "weight": int(float(weights_value)), "sys_bp": int(systolic_value),
                "dia_bp": int(diastolic_value), "glucose": int(glucose_value), "heart_rate": int(heart_rate_value)}

    return {"age": int(current_user.age), "sex": int(current_user.sex), "height": int(float(heights_value)),
            "weight": int(float(weights_value)), "prevalent_stroke": int(current_user.prevalent_stroke),
            "sys_bp": int(systolic_value),
            "dia_bp": int(diastolic_value), "glucose": int(glucose_value), "tot_chol": int(current_user.tot_chol),
            "cigs_per_day": int(current_user.cigs_per_day), "prevalent_hyp": int(current_user.prevalent_hyp),
            "bp_meds": int(current_user.bp_meds), "diabetes": int(current_user.diabetes),
            "education": int(current_user.education),
            "current_smoker": int(current_user.current_smoker), "heart_rate": int(heart_rate_value)}


def save_to_database(health_factors):  # pragma: no cover
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
def monitor_page(debug_form=False, debug=False, health_factors=None):
    form = MonitorForm()
    if form.validate_on_submit() or debug_form:
        if not debug_form:
            health_factors = extract_from_form(form)
            save_to_database(health_factors)  # pragma: no cover
        prediction = predict(health_factors)
        return result_page(prediction, debug_form)

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with monitoring your health: {err_msg}', category='danger')

    if not (current_user.is_authenticated or debug):
        return redirect("/login")
    return render_template('monitor.html', form=form)


@app.route('/monitor_fitbit', methods=['GET', 'POST'])
def monitor_fitbit_page(debug_form=False, debug=False, health_factors=None, email_address=None):
    form = MonitorFitbitForm()
    if form.validate_on_submit() or debug_form:
        if not debug_form:
            health_factors = extract_from_form(form, True)
            save_to_database(health_factors)  # pragma: no cover
        prediction = predict_fitbit(health_factors)
        return result_page(prediction, debug_form)

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with monitoring your health: {err_msg}', category='danger')

    if not (current_user.is_authenticated or debug):
        return redirect("/login")
    if debug:
        return render_template('monitor_fitbit.html', form=form, id=email_address)
    return render_template('monitor_fitbit.html', form=form, id=current_user.email_address)


def extract_from_database():  # pragma: no cover
    return {"age": current_user.age, "sex": current_user.sex, "height": current_user.height,
            "weight": current_user.weight, "prevalent_stroke": current_user.prevalent_stroke,
            "sys_bp": current_user.sys_bp,
            "dia_bp": current_user.dia_bp, "glucose": current_user.glucose, "tot_chol": current_user.tot_chol,
            "cigs_per_day": current_user.cigs_per_day, "prevalent_hyp": current_user.prevalent_hyp,
            "bp_meds": current_user.bp_meds, "diabetes": current_user.diabetes, "education": current_user.education,
            "current_smoker": current_user.current_smoker, "heart_rate": current_user.heart_rate}


@app.route('/view_health', methods=['GET', 'POST'])
def view_health_page(debug=False, health=None):
    if not (current_user.is_authenticated or debug):
        return redirect("/login")
    if not debug:
        health = extract_from_database()  # pragma: no cover
    return render_template('view_health.html', health=health, form=MonitorForm())


@app.route('/result', methods=['GET', 'POST'])
def result_page(prediction, debug_form):
    if not (current_user.is_authenticated or debug_form):
        return redirect("/login")
    return render_template('result.html', prediction=prediction)

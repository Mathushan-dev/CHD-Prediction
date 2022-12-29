from application import app
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
        return monitor_page()

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
            return monitor_page()

        else:
            flash('Username and password are not match! Please try again', category='danger')

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with logging in: {err_msg}', category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return render_template('home.html')


@app.route('/monitor', methods=['GET', 'POST'])
def monitor_page():
    form = MonitorForm()
    if form.validate_on_submit():
        flash('Welcome to monitor page', category='success')

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with monitoring your health: {err_msg}', category='danger')

    return render_template('monitor.html', form=form)
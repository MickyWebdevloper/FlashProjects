import os
import secrets
from PIL import Image
from flask import render_template, flash, url_for, redirect, flash, request
from PythonNCS import app, datetime, db, bcrypt
from PythonNCS.forms import registrationForm, loginForm, UpdateAccountForm
from PythonNCS.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        "Author": "Roki Handsome",
        "Title": "Full Stack Project",
        "Addr": "United State Of Umerica"
    },
    {
        "Author": "Roki Handsome",
        "Title": "Usa",
        "Addr": "United State Of Umerica"
    }
]


@app.route('/')
def home():
    return render_template('home.html', posts=posts, title='Home Page!')


@app.route('/about')
def about():
    return render_template('about.html', posts=posts, title='About Page!')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = registrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        # flash second argument is 'category'
        flash(
            f'Your Account created successfully! Now you are able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register Page!', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # if user and bcrypt.check_password_hash(user.password, form.password.data):
        #     login_user(user, remember=form.remember.data)
        #     next_page = request.args.get('next')
        #     return redirect(next_page) if next_page else redirect(url_for('ihome))
        if user:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful, Plese check username and password', 'danger')

    return render_template('login.html', title='Login Page!', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path, 'static/Profile_pics', picture_fn)
    output_size = (100, 100)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated successfully!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        # Email is not working, i do not know why.
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for(
        'static', filename='Profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account Page', image_file=image_file, form=form)

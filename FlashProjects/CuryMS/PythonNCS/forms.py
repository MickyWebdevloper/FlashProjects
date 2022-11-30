from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms.validators import InputRequired, DataRequired, length, EqualTo, Email, ValidationError
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from PythonNCS.models import User


class registrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           InputRequired(), length(min=2, max=15)])
    email = PasswordField('Email', validators=[
                          DataRequired(), Email(), length(min=5, max=25)])
    password = PasswordField('Password', validators=[
                             InputRequired(), length(min=5, max=25)])
    confirm_password = PasswordField('Confirm Password', validators=[
        InputRequired(), EqualTo('password'), length(min=5, max=25)])
    submit = SubmitField('Sign Up')

# ValidationError checking is taken from wtforms.validators
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username has been taken, Please choose an another username')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email has been taken, Please choose an another email')


class loginForm(FlaskForm):
    email = PasswordField('Email', validators=[
                          DataRequired(), Email(), length(min=5, max=25)])
    password = PasswordField('Password', validators=[
                             InputRequired(), length(min=5, max=25)])
    remember = BooleanField('Rememeber Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[
                           InputRequired(), length(min=2, max=15)])
    email = PasswordField('Email', validators=[
                          DataRequired(), Email(), length(min=5, max=25)])
    picture = FileField('Upload a Profile Picture', validators=[
                        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    'That username has been taken, Please choose an another username')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'That email has been taken, Please choose an another email')

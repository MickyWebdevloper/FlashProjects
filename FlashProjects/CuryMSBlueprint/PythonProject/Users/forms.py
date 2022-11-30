from flask import Blueprint
from flask_wtf import FlaskForm
from flask_login import current_user
from PythonProject.models import User
# from flask_wtf.file import FileField, FileAllowed
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=25)])
    email = StringField('Email', validators=[
                        DataRequired(), Email(), Length(min=5, max=25)])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=5, max=25)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password'), Length(min=2, max=25)])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is already taken, Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is already taken, Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired(), Email(), Length(min=5, max=25)])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=5, max=25)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=25)])
    email = StringField('Email', validators=[
                        DataRequired(), Email(), Length(min=5, max=25)])
    picture = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    'That username is already taken, Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'That email is already taken, Please choose a different one.')


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired(), Email(), Length(min=5, max=25)])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                'There is no account with that email. You must register first')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=5, max=25)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password'), Length(min=2, max=25)])
    submit = SubmitField('Reset Password')

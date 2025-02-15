from flask import flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from website.models import User

class RegisterForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=6,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8,max=16)])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')

class UpdateForm(FlaskForm):
    username = StringField('Username',validators=[Length(min=6,max=20)])
    email = StringField('Email',validators=[Email()])
    current = PasswordField('Current Password',validators=[Length(min=8,max=16)])
    new = PasswordField('New Password',validators=[Length(min=8,max=16)])
    confirm_new = PasswordField('Confirm New Password',validators=[EqualTo('new')])
    image = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png','jpeg','jfif'])])
    submit = SubmitField('Save')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8,max=16)])
    submit = SubmitField('Login')

class RequestResetForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            flash('User does not exist with that email!',category="error")
        
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('ConfirmPassword',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Request Password Reset')
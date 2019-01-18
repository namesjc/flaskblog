from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


# class inherited from FlaskForm
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           # limititation for username
                           validators=[DataRequired(), Length(min=2, max=24)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # validate if username already existed in database
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken, Please choose a different one.')


    # validate if email already existed in database
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is taken, Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')  # check box
    submit = SubmitField('Login')

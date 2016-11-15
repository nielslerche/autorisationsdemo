from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
  first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=25)])
  last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
  """
  IMPROVEMENT: Email-felt passer bedre til at være af typen Email.
  """
  email = StringField('Email Address', validators=[DataRequired(), Length(min=6, max=50)])
  password = PasswordField('New Password', validators=[
    DataRequired(), Length(min=8, max=128),
    EqualTo('confirm', message='Passwords must match.')
  ])
  confirm = PasswordField('Repeat Password')
  agree_tos = BooleanField('I agree with the Terms of Service.', validators=[DataRequired()])

class LoginForm(FlaskForm):
  email = StringField('Email Address', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
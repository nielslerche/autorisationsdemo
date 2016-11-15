from flask import g
from flask_login import LoginManager, current_user
from jobbr import app
from jobbr.models import User
from jobbr.db import db

login_manager = LoginManager()

login_manager.login_view = 'login'

@app.before_request
def before_request():
  g.user = current_user

@login_manager.user_loader
def load_user(id):
  try:
    return User.query.get(id)
  except:
    return None
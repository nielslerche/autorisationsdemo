from jobbr.db import db
from jobbr.security import bcrypt
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
  __tablename__ = 'user'
  id = db.Column('user_id', db.Integer, primary_key=True)
  first_name = db.Column('first_name', db.String(25))
  last_name = db.Column('last_name', db.String(50))
  email = db.Column('email', db.String(50), unique=True, index=True)
  password = db.Column('password', db.String(128))
  registered_on= db.Column('registered_on', db.String(50))

  def __init__(self, first_name, last_name, email, password):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.set_password(password)
    self.registered_on = date.today().strftime('%d. %B %Y')
  
  def set_password(self, password):
    self.password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)

  def is_authenticated(self):
    return True
  
  def is_active(self):
    return True
  
  def is_anonymous(self):
    return False
  
  def get_id(self):
    return str(self.id)
  
  def __repr__(self):
    return '<User %r>' % (self.username)
from flask import render_template, redirect, url_for, request, session, g, flash
from flask_login import login_user, logout_user, login_required, current_user
from jobbr import app
from jobbr.db import db
from jobbr.models import User
from jobbr.forms import RegistrationForm, LoginForm
import jobbr.auth

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('home'))

  form = RegistrationForm(request.form)
  """
  BUG: Flash-besked angående allerede registreret email vises ikke.
  FJERNET
  """
  if request.method == 'POST' and form.validate_on_submit():
    user = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
    db.session.add(user)
    db.session.commit()
    flash(u'Your user has successfully been registered. You can login now.', 'success')
    return redirect(url_for('login'))
    
  return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('home'))

  form = LoginForm(request.form)
  if request.method == 'POST' and form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    """
    BUG:    Ingen redirect væk fra 'login', ved et succesfuldt login.
    UGLY:   Mangler D.R.Y.
    """
    if user is None:
      flash(u'Could not find a user with that Email Address and Password combination.', 'negative')
      return redirect(url_for('login'))
    if not user.check_password(form.password.data):
      flash(u'Could not find a user with that Email Address and Password combination.', 'negative')
      return redirect(url_for('login'))
    login_user(user)
    flash(u'You have successfully logged in.', 'info')
    redirect(url_for('home'))
  return render_template('login.html', form=form)

""" DEPRECATED """ 
# @app.route('/auth/login', methods=['GET','POST'])
# def auth_login():
#   if current_user.is_authenticated:
#     return redirect(url_for('home'))
#   email = request.form['email']
#   password = request.form['password']
#   registered_user = User.query.filter_by(email=email).first()
#   if registered_user is None:
#     return redirect(url_for('login'))
#   if not registered_user.check_password(password):
#     return redirect(url_for('login'))
#   login_user(registered_user)
#   return redirect(request.args.get('next') or url_for('home'))

@app.route('/logout')
@login_required
def logout():
  logout_user()
  flash(u'You have logged out.', 'info')
  return redirect(url_for('home'))

@app.route('/profile')
@login_required
def profile():
  full_name = '{} {}'.format(g.user.first_name, g.user.last_name)
  joined = str(g.user.registered_on)
  return render_template('profile.html', full_name=full_name, joined=joined)

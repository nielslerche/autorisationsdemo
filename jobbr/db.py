from flask_sqlalchemy import SQLAlchemy
from jobbr import app

db = SQLAlchemy(app)

""" DEPRECATED """
# def migrate():
#   db.create_all()
#   db.session.commit()
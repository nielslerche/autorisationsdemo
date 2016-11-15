import jobbr.models
from jobbr.db import db

db.create_all()
db.session.commit()
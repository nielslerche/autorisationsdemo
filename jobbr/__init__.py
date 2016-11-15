from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

from jobbr.auth import login_manager

login_manager.init_app(app)

import jobbr.views
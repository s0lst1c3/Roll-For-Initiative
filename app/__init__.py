import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID

app = Flask(__name__)
app.debug = True
app.config.from_pyfile('../config.py')

db = SQLAlchemy(app)

lm = LoginManager()
lm.init__app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models

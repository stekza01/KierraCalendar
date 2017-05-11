import os, sys, time
from flask import *
from jinja2 import Template
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from wtforms import *
from wtforms.validators import *
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, TextAreaField, StringField, SubmitField, validators
from flask import Flask, render_template, flash, request, url_for
from flask.ext.heroku import Heroku
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.secret_key = '\xa7h\xb7)\xce\xce\x8c\xa9`\xce\xa1\xdb\x9b1;F\x12c\xb2\xe9\xe7\xe8\x92\xe2'
app.debug = True

heroku = Heroku(app)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
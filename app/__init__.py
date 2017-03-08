from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_whooshee import Whooshee

page = Flask(__name__, static_url_path='/static')
page.config.from_object('config')

UPLOAD_FOLDER = '/home/manan/Programs/EduTech/app/static/userdata/'
page.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(page)
migrate = Migrate(page, db)

whooshee = Whooshee(page)

from app import views, models

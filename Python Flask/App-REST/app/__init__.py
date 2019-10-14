from flask import Flask
import os
from dotenv import load_dotenv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
ROOT_PATH = os.path.join(os.path.dirname(__file__), '..')
ENV_PATH = os.path.join(ROOT_PATH, '.env')
load_dotenv(ENV_PATH)


if app.config['ENV'] == 'development':
	app.config.from_envvar('DEV_SETTINGS')
else:
	app.config.from_envvar('PRO_SETTINGS')

from app import views
from app.model.TechModel import db
db.create_all()

from flask import Flask
import os
from dotenv import load_dotenv
import redis
from rq import Queue


# load Environment Variables
ROOT_PATH = os.path.join(os.path.dirname(__file__), '..')
ENV_PATH = os.path.join(ROOT_PATH, '.env')
load_dotenv(ENV_PATH)

app = Flask(__name__)

# Type 1 - config intgration
"""
if app.config['ENV'] == 'development':
	app.config.from_object('app.config.DevelopmentConfig')
else:
	app.config.from_object('app.config.ProductionConfig')
"""
# Type 2 - config intgration
if app.config['ENV'] == 'development':
	app.config.from_envvar('DEV_SETTINGS')
else:
	app.config.from_envvar('PRO_SETTINGS')

r = redis.Redis()
q = Queue(connection = r)

from app import views
from app import admin_views


# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, request
from flask_script import Manager
from werkzeug.datastructures import MultiDict

from form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hey I am optimus prime'
manager = Manager(app)

@app.route('/')
def index():
	form = LoginForm(MultiDict([('username', 'sara@gmail.com'), ('password', 'Optimus')]))
	return render_template('index.html', form=form)

@app.route('/login', methods = ['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	if username == 'saravana@gmail.com' and password == 'Optimus':
		return 'Login Successfully'
	else:
		return 'Login Fail'

if __name__ == '__main__':
	manager.run()
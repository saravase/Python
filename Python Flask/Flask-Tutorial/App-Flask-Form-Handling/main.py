# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, request, redirect, flash
from flask_script import Manager
from werkzeug.datastructures import MultiDict

from form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hey I am optimus prime'
manager = Manager(app)

@app.route('/', methods=['POST', 'GET'])
def index():
	form = LoginForm()
	if form.validate_on_submit():
		username = request.form['username']
		password = request.form['password']
		print(username)
		print(password)
		msg = 'Login Successfully'
		flash('Login Successfully', 'success')
		return redirect(url_for('home'))
	return render_template('index.html', form=form)

@app.route('/home')
def home():
	return 'Home Page'

@app.route('/login', methods = ['POST'])
def login():
	pass

if __name__ == '__main__':
	manager.run()
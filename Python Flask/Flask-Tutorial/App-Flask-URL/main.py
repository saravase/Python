# -*- coding: utf-8 -*-

from flask import Flask,url_for, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/home')
def home():
    return 'Home Page'

@app.route('/contact/<name>')
def contact(name):
    return render_template('contact.html')


@app.route('/profile')
def profile():
    return 'Profile Page'

@app.route('/login')
def login():
    if 'admin' == 'admin':
        try:
            print(url_for('contact'))
        except Exception:
            pass
    return redirect(url_for('contact', name = 'optimuz',age= 90, salary = 23000.00, _external = True))

if __name__ == '__main__':
    app.run()
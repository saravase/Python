# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_script import Manager,Command,Shell


class Smile(Command):
    def run(self):
        print('Optimus smile please')

def add_libs():
    import os
    return dict(os=os, app=app).update(sys_libs())

def sys_libs():
    import sys
    return dict(sys=sys)

app = Flask(__name__)
manager = Manager(app)

@manager.command
def keep():
    print('keep smile always')
    
manager.add_command('smile', Smile())
manager.add_command('shell', Shell(make_context=add_libs))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return 'Login Template'

if __name__ == '__main__':
    manager.run()
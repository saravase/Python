from flask import Flask, render_template,url_for,request
from flask_script import Manager
import json

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/detail')
def detail():
	return render_template('detail.html')

@app.route('/custom', methods= ['POST', 'GET'])
def custom():
	return json.dumps({'name':'optimus', 'age':34, 'salary':int(request.form['id'])*1000})

@app.route('/emp-detail')
def emp_detail():
	print(request.args['employee'])
	return json.dumps('Success')

if __name__ == '__main__':
	manager.run()
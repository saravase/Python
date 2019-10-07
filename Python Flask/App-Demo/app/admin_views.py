from app import app
from flask import render_template,url_for,session

@app.route('/admin/dashboard')
def dashboard():
	return render_template('admin/dashboard.html')

users = {
	'optimus':{
		'name': 'Optimus Prime',
		'age' : 21,
		'position': 'Developer',
		'Salary': 45000
	},
	'saravana':{
		'name': 'Saravanakumar',
		'age' : 22,
		'position': 'Developer',
		'Salary': 50000
	},
	'dharshni':{
		'name': 'Priyadharshni',
		'age' : 16,
		'position': 'Student',
		'Salary': 0
	}
}

@app.route('/admin/profile/<user>')
def profile(user):
	if session.get('username') is not None and session.get('username') in users:
		user = users[session.get('username')]
	else:
		user = ''
	return render_template('admin/profile.html', user= user)
from app import app
import json as JSON
from flask import render_template,url_for,request,redirect
from flask import make_response, jsonify, abort, session,flash
from werkzeug.utils import secure_filename
from flask import send_from_directory, safe_join,send_file
import os
from app.admin_views import profile
from app import r,q
import time

@app.route('/')
def index():
	#print(os.path.join(app.instance_root))
	return render_template('public/index.html')

@app.route('/about')
def about():
	return render_template('public/about.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('public/404.html'), 404

@app.route('/cookie', methods= ['GET'])
def cookie():
	if request.cookies:
		print(request.cookies)
	result = make_response(render_template('public/cookie.html'))
	result.set_cookie('name', value='optimus', max_age=10, path = request.path)
	return result

@app.route('/get_image/<image_name>')
def get_image(image_name):
	try:
		return send_from_directory(os.path.join(os.path.dirname(__file__), app.config['CLIENT_IMAGES']), filename=image_name, as_attachment=True)
	except FileNotFoundError:
		return abort(404)

@app.route('/get_csv/<path:filename>')
@app.route('/get_csv/<csv_id>')
def get_csv(csv_id, filename=''):
	if filename != '':
		file_path = safe_join(os.path.join(os.path.dirname(__file__), app.config['CLIENT_REPORTS']),filename)
		print(file_path)
	if csv_id != '':
		file_path = safe_join(os.path.join(os.path.dirname(__file__), app.config['CLIENT_CSV']),f'{csv_id}.csv')
	try:
		return send_file(file_path, as_attachment=True)
	except FileNotFoundError:
		return abort(404)

@app.route('/get_pdf/<pdf_id>')
def get_pdf(pdf_id):
	if pdf_id != '':
		filename = f'{pdf_id}.pdf'
	try:
		return send_from_directory(os.path.join(os.path.dirname(__file__), app.config['CLIENT_PDF']), filename=filename, as_attachment=True)
	except FileNotFoundError:
		return abort(404)

def isNameEmpty(filename):
	if filename == '':
		return False
	else:
		return True

def isInvalidFileType(filename):
	if filename.rsplit('.', 1)[1].upper() in app.config['ALLOWED_IMAGE_EXTENSIONS']:
		return True
	else:
		return False

def isInvalidSize(filesize):
	if filesize <= app.config['MAX_CONTENT_LENGTH']:
		return True
	else:
		return False

@app.route('/upload', methods=['POST','GET'])
def upload():
	print(app.config)
	if request.method == 'POST':
		if request.files and request.cookies:
			sizeData = JSON.loads(request.cookies['imagesSize'])
			checkList = [isNameEmpty(image.filename) and isInvalidFileType(image.filename) and isInvalidSize(sizeData[image.filename]) for image in request.files.getlist('images')]		
			if all(checkList):
				for image in request.files.getlist('images'):
					filename = secure_filename(image.filename)
					image.save(os.path.join( os.path.dirname(__file__), app.config['IMAGE_UPLOADS'], filename))
				return redirect(request.url)
			else:
				return abort(404)
	return render_template('public/upload.html')

@app.route('/guest')
def quest():
	print(f'args = {request.args}')
	print(f'query_string = {request.query_string}')
	print(f'values = {request.values}')
	return render_template('public/guest_book.html')

@app.route('/guest_msg', methods= ['POST'])
def questMsg():
	data = request.get_json()
	print(f'get_json = {data}')
	data = {
		'msg' : 'Data received successfully',
		'status' : 200
	}
	return make_response(jsonify(data), 200)


@app.route('/signup', methods=['POST', 'GET'])
def signup():
	if request.method == 'POST':
		form = request.form
		missing = []
		if form['username'] != '':
			session['username'] = form['username']
		for k,v in form.items():
			if v == '':
				missing.append(k)
				flash(k+" : It is mandatory")
		if missing:
			feedback = f'Missed Fields for {",".join(missing)}'
			return render_template('public/signup.html', feedback = feedback)
		return redirect(url_for("profile",user= form['username']))
	return render_template('public/signup.html')

@app.route('/json', methods=['POST'])
def json():
	print(request.__dict__)
	data = request.get_json()
	print(data)
	result = {
		'msg' : 'received successfully',
	} 
	return make_response(jsonify(result), 200)

@app.route('/jinja')
def jinja():
	from datetime import datetime
	# Strings
	name = 'Optimus Prime'

	# Integers 
	age = 22

	# Lists
	langs = ['Python', 'R', 'JS']

	# Dictionries
	friends = {
		'optimus': 22,
		'prime': 22,
		'sskumar': 22,
		'303': 22
	}

	# Tuples
	colors = ('SkyBlue', 'Orange')

	#Booleans
	male = True

	# Classes
	class SlackRemote:
		def __init__(self, username, password, msg):
			self.username = username
			self.password = password
			self.msg = msg

	remote = SlackRemote('optimus', 'Optimus323', 'Hai, how are you?')

	# Functions
	def displayFullName(firstname, lastname):
		return firstname+' '+lastname
	return render_template('public/jinja.html', name=name, age=age, langs=langs,friends=friends, colors=colors, male=male, SlackRemote=SlackRemote,remote=remote, displayFullName=displayFullName, date = datetime.utcnow())

@app.template_filter('clean_date')
def cleanDate(dt):
	return dt.strftime('%d %b %Y')

"""
	HTTP Methods
"""

stock = {
    "fruit": {
        "apple": 30,
        "banana": 45,
        "cherry": 1000
    }
}

@app.route('/stock/<collection>/<member>')
def get_collection(collection, member):
	if collection in stock:
		if stock[collection][member] is not None:
			result = make_response(jsonify(stock[collection][member]), 200)
		else:
			result = make_response({'response': 'Not Found'}, 404)
	else:
		result = make_response({'response': 'Not Found'}, 404)
	return result


def background_task(n):
    """ Function that returns len(n) and simulates a delay """
    delay = 2
    print("Task running")
    print(f"Simulating a {delay} second delay")
    time.sleep(delay)
    print(len(n))
    print("Task complete")
    return len(n)

@app.route("/task")
def task():
    if request.args.get("n"):
        job = q.enqueue(background_task, request.args.get("n"))
        return f"Task ({job.id}) added to queue at {job.enqueued_at}"
    return "No value for count provided"

from app.task import count_words
from time import strftime

@app.route('/add-task', methods = ['POST', 'GET'])
def add_task():
	jobs = q.jobs
	message = None
	if request.args:
		url = request.args.get('url')
		task = q.enqueue(count_words, url)
		jobs = q.jobs
		q_len = len(q)
		message = f"Task queued at {task.enqueued_at.strftime('%a, %d %b %Y %H:%M:%S')}. {q_len} jobs queued"
	return render_template('public/task.html', message =message , jobs = jobs)		

from app.task import create_image_set
import secrets

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    message = None
    if request.method == "POST":
        image = request.files["image"]
        image_dir_name = secrets.token_hex(16)
        os.mkdir(os.path.join(os.path.dirname(__file__), app.config["UPLOAD_DIRECTORY"], image_dir_name))
        image.save(os.path.join(os.path.dirname(__file__), app.config["UPLOAD_DIRECTORY"], image_dir_name, image.filename))
        image_dir = os.path.join(os.path.dirname(__file__), app.config["UPLOAD_DIRECTORY"], image_dir_name)
        q.enqueue(create_image_set, image_dir, image.filename)
        flash("Image uploaded and sent for resizing", "success")
        message = f"/image/{image_dir_name}/{image.filename.split('.')[0]}"
    return render_template("public/upload_image.html", message=message)

@app.route("/image/<dir>/<img>")
def view_image(dir, img):
    return render_template("public/view_image.html", dir=dir, img=img)

@app.route('/table')
def table():
	return render_template('public/table.html')
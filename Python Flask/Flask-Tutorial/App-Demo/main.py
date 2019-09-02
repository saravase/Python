from flask import Flask, render_template, request,url_for, escape, redirect,make_response,abort, current_app
from flask import g

app = Flask(__name__)

app.config['SECRET_KEY'] = 'I am optimus prime'
app.config['APPLICATION_ROOT'] = '/detail'

@app.route('/')
def index():
	print(url_for('index'))
	print(request.args)
	print(escape(request.args['name']))
	print(g.__dict__)
	return make_response(render_template('index.html'), 200, {'Content-Type':'text/html'})


@app.route('/500', methods=['GET'])
def detail():
	return abort(404)

@app.errorhandler(500)
def server_error(error):
	return '<h1 style="color:red;">Internal Server Error Occured</h1>'


@app.errorhandler(404)
def server_error(error):
	return '<h1 style="color:red;">Page not found error occured</h1>'


@app.before_first_request
def before_first():
	print('before_first_request')
	return redirect(url_for('detail'))

@app.before_request
def before_first():
	print('before_request')
	res = make_response(render_template('detail.html'))
	res.set_cookie('name','optimus prime')
	res.set_cookie('password','Optimusmom@1492')

@app.after_request
def after_request(response):
	print(response.__dict__)
	print('after_request')
	return response

@app.teardown_request
def teardown_request(response):
	print('teardown_request')
	return response

if __name__ == '__main__':
	app.run(port=9000, debug=True)
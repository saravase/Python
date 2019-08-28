# -*- coding: utf-8 -*-

from flask import Flask, make_response, redirect, abort

"""
    Response Format:
        * String (or emplate engine)
        * object
        * tuple(response, status, headers) or (response, headers)
        

"""
app = Flask(__name__)

@app.route('/<name>')
def index(name = 'prime'):
    res = make_response(f'<h2>Hi {name}, This is Flask Response </h2>')
    res.headers['Content-Type'] = 'text/plain'
    res.headers['server'] = 'Demo'
    return res

app.add_url_rule('/index', 'index', index)

@app.route('/')
def http_404_handler():
    return make_response('<h3 style = "color: red;">Page Not Found Error 404</h3>', 404)

@app.route('/set_cookie')
def set_cookie():
    res = make_response('Set Cookie')
    res.set_cookie('color', 'light-green', 60)
    res.set_cookie('font', 'Time New Roman',60)
    return res

@app.route('/500')
def http_500_handler():
    return ('<h3>500 Error Occured</h3>', 500)


@app.route('/markdown')
def render_markdown():
    return ('Markdown Rendered', 200, {'Content-Type' : 'text/markdown'})


@app.route('/location')
def location():
    return ('', 302, {'location': 'http://localhost:5000/markdown'})


@app.route('/locate')
def locate():
    return redirect('http://localhost:5000/optimusprime', code = 301)


"""
    Hook Points:
        * before_first_request
            => exeute before first request handled
        * before_request:
            => execute before each request handled
        * after_request:
            => execute after each request handled, but if any unhandled exception
            throw it will not executed.
        * teardown_request:
            => execute after each request handled, but if any unhandled exception
            occur or not, it will executed.
"""

@app.before_first_request
def before_first_request():
    print("before_first_request() called")
 
@app.before_request
def before_request():
    print("before_request() called")
 
@app.after_request
def after_request(response):
    print("after_request() called")
    return response

@app.teardown_request
def teardown_request(response):
    print("teardown_request() called")
    return response

"""
    abort request:
        * abort() => 404, 500 and etc.
"""

@app.route('/404')
def http_400():
    abort(404)
    

@app.route('/error_500')
def http_500():
    abort(500)

"""
    Custom Error Pages:
    
"""

@app.errorhandler(404)
def error_404(error):
    return '<h2 style = "color: green;">Hi optimus, this is 404.</h2>', 404


@app.errorhandler(500)
def error_500(error):
    return '<h2 style = "color: light-green;">Hi optimus, this is 500.</h2>', 500

if __name__ == '__main__':
    app.run()
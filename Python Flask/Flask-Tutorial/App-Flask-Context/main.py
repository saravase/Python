# -*- coding: utf-8 -*-

from flask import Flask,request,current_app

"""
Type of Flask Context:
    * Application Context:
        => It is used to store app generic varible. like, database connection
            
    * Request Context:
        => It is used to store specific request variables.
"""

app = Flask(__name__)

"""
@app.route('/')
def requestdata():
    print(request)
    return f'Request to = {request.remote_addr}'

if __name__ == '__main__':
    app.run(port=9000, debug=True)

"""

with app.app_context():
    print(current_app.__dict__)
    
with app.test_request_context('index'):
    print(request.method)
    print(request.path)
    print(request.__dict__)
    print(current_app.name)

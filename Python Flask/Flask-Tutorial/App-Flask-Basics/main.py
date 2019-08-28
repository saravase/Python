from flask import Flask,request

app = Flask(__name__)


# This is used to find the list of url binded in app
"""
app.url_map
"""
    
@app.route('/')
def index():
	return  '<h1 style="background-color:orange">Hai Optimus, This is Flask</h1>'

@app.route('/optional2', methods = ['GET'])
@app.route('/optional1', methods = ['GET'])
def optional_index(name = 'optimus', id =303):
	return f'<h3>Hai {request.args.get("name", name)}, this is optional page {request.args.get("id", id)}</h3>'

app.add_url_rule('/optional/', 'optional_index', optional_index)

if __name__ == '__main__':
	app.run(port=8080,debug = True)
    
    
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def display(self):
        return f'Name : {self.name} , Age : {self.age}, Salary : {self.salary}'
        
    def __str__(self):
        return f'Employee - ({self.name}, {self.age}, {self.salary})'

app = Flask(__name__)

# Collection of data
@app.route('/index', methods= ['GET'])
def index():
    first_name, last_name = request.args.get('first_name', None),request.args.get('last_name', None)
    data = dict(first_name = first_name, last_name = last_name)
    return render_template('index.html',**data)

@app.route('/template/')
def template():
    return render_template('template-index.html')


# Passing List
@app.route('/list/')
def list_index():
    return render_template('list-index.html',colors = ['red', 'green', 'blue', 'yellow'],
                           background_colors = ('#234423', '#aaff23', '#234221', '#ad2342'))


# Passing Dict
@app.route('/dict/')
def dict_index():
    emp = Employee('optimus prime', 22, 340000.00)
    emp_data = {'name': emp.name, 'age' : emp.age, 'salary' : emp.salary}
    return render_template('dict-index.html',employee = emp_data, emp = emp)

if __name__ == '__main__':
    app.run()

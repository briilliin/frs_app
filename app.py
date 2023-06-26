import os

import psycopg2
from flask import Flask, redirect
from flask import render_template, request
from data.OperationsStudents import OperationsStudents

app = Flask(__name__)
db_name = 'frs_db'
user = "postgres"
password = "123"
host = "localhost"
port = "5432"


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        try:

            student_name = request.form.get('name')
            surname = request.form.get('surname')
            middle_name = request.form.get('middle_name')
            group = int(request.form.get('group'))
            student = OperationsStudents()
            student.create_student(name=student_name, surname=surname, middle_name=middle_name, group=group)

            data = student.get_all()
            return render_template("index.html", data=data)
        except AssertionError:
            return render_template('index.html')
    else:
        student = OperationsStudents
        data = student.get_all(student)
        return render_template("index.html", data=data)


@app.route('/take_photo', methods=['POST', 'GET'])
def take_photo():
    # student_name = request.form.get('name')
    # surname = request.form.get('surname')
    # middle_name = request.form.get('middle_name')
    # group = int(request.form.get('group'))
    # student = OperationsStudents()
    # student.create_student(name=student_name, surname=surname, middle_name=middle_name, group=group)
    #
    # data = student.get_all()
    print(request.form.get('imageURL'))
    return render_template("camera.html")


#
# @app.route('/', methods=['POST', 'GET'])
# def registration():
#     try:
#         student = OperationsStudents()
#         name = request.form.get('name')
#         surname = request.form.get('surname')
#         middle_name = request.form.get('middle_name')
#         group = request.form.get('group')
#         student.create_students(name=name, surname=surname, middle_name=middle_name, group=group)
#         data = student.get_all()
#         return render_template("index.html", data=data)
#     except AssertionError:
#         return render_template('registration.html')


if __name__ == '__main__':
    app.run()

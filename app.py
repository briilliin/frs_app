import os

import psycopg2
from flask import Flask, redirect
from flask import render_template, request, Response, send_from_directory
import cv2
import requests
import json
# from data.OperationsStudents import OperationsStudents

app = Flask(__name__)
db_name = 'frs_db'
user = "postgres"
password = "123"
host = "localhost"
port = "5432"


def gen_frames():  # generate frame by frame from camera
    camera = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        try:

            student_name = request.form.get('name')
            surname = request.form.get('surname')
            middle_name = request.form.get('middle_name')
            group = int(request.form.get('group'))
            return render_template('index.html')
        except AssertionError:
            return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/take_photo', methods=['POST', 'GET'])
def take_photo():

    print(request.form.get('imageURL'))
    return render_template("camera.html")

@app.route('/add_stream')
def add_stream():
    payload = dict(streamId='1', url='http://127.0.0.1:5000/video_feed', callback="http://127.0.0.1:5000/faceRecognized")
    json = '{"streamId":"1","url":"http://127.0.0.1:5000/video_feed","callback":"http://127.0.0.1:5000/faceRecognized"}'
    r = requests.post('http://localhost:9051/api/addStream', data=json)
    print(payload)
    return Response(r)

@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/photo_feed',methods=['GET'])
def photo_feed():
    name = '1.jpg'
    dir = app.root_path  + '\static'
    return send_from_directory(
        dir, name
    )

@app.route('/faceRecognized')
def face_recognized():
    print("ЛИЦО РАСПОЗНАНО")
    return 0

@app.route('/capture', methods=['POST', 'GET'])
def capture():
    # imageulr='https://i.ytimg.com/vi/lqYKkloAWMc/maxresdefault.jpg'
    imageulr='https://i0.wp.com/spp-photo.ru/wp-content/uploads/2021/01/2-7.jpg'
    my_dict = {
    'streamId': '1',
    'url': imageulr,
    'left': 537,
    'top': 438,
    'width': 142,
    'height': 156
    }

    json_str = json.dumps(my_dict)
    print(json_str)

    r = requests.post('http://localhost:9051/api/registerFace', data=json_str)
    return r.content


if __name__ == '__main__':
    app.run()

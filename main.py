from flask import Flask, render_template, Response, redirect, request
from camera import VideoCamera
import os
app = Flask(__name__)


@app.route('/tryon/<file_path>', methods=['POST', 'GET'])
def tryon(file_path):
    file_path = file_path.replace(',', '/')
# os.system('python test.py ' + file_path + "images/Sunglasses6/1.png")
    os.system('python test.py ' + file_path)
# os.system('python test.py ' )
    return redirect('http://127.0.0.1:5000/', code=302, Response=None)


@app.route('/')
def index():
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run()
    app.run()

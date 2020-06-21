from flask import Flask, render_template, Response, request
import os
from PIL import Image

IMAGE_FOLDER = os.path.join('static' , 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

def gen(data):

    image = Image.frombytes('RGBA', (640,480), data)
    image.save("test.jpg")
        

@app.route('/get_stream', methods=['POST'])
def get_stream():
    data = request.data


    return Response(gen(data),
                mimetype='multipart/x-mixed-replace; boundary=frame') 

@app.route('/')
@app.route('/test_image')
def test_image():
   
   

    while True:
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
        return render_template("test.html", user_image = full_filename)

if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='5000', debug=True)

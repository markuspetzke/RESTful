from flask import Flask, render_template, Response, request
import os, io
import cv2
from PIL import Image 

IMAGE_FOLDER = os.path.join('static' , 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

def gen():
    while True:
        path = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')   
        img  = Image.open(path)
        frame = img.tobytes()
        
        imgByteArr = io.BytesIO()
        img.save(imgByteArr, format='PNG')
        frame = imgByteArr.getvalue()

        yield(b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        

@app.route('/get_stream', methods=['POST'])
def get_stream():
    image = request.files['image_data']
    image.save(os.path.join('C:/Users/marku/Desktop/Projekt X/git/RESTful/static/images/' + image.filename))
    return "image: succed " + image.filename


@app.route('/video_feed_1')
def video_feed1():
        #image = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
        #return render_template("test.html", user_image = image)
        return Response(gen(),
                mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='5000', debug=True)

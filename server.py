from flask import Flask, render_template, Response, request
import os

IMAGE_FOLDER = os.path.join('static' , 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

def gen():
    cap = cv2.VideoCapture('today.mp4')

    # Read until video is completed
    while(cap.isOpened()):
      # Capture frame-by-frame
        ret, img = cap.read()
        if ret == True:
            img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 
            frame = cv2.imencode('.jpg', img)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.1)
        else: 
            break
        

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_stream', methods=['POST'])
def get_stream():
    image = request.files['image_data']
    print(image.filename)
    image.save(os.path.join('C:/Users/marku/Desktop/Projekt X/git/RESTful/static/images/' + image.filename))
    return "image: succed" + image.filename

    print(request.files['image_data'])

@app.route('/')
@app.route('/test_image')
def test_image():
    while True:
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
        return render_template("test.html", user_image = full_filename)

if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='5000', debug=True)

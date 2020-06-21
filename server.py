from flask import Flask, render_template, Response, request
<<<<<<< HEAD
import os
=======

>>>>>>> 0d531d2d32b6d1d53ac36c43f35ce6251b991b6c

app = Flask(__name__)

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
<<<<<<< HEAD
    image = request.files['image_data']
    print(image.filename)
    image.save(os.path.join(app.root_path, 'images/' + image.filename))
    return "image: succed" + image.filename
=======
    print(request.files['image_data'])
>>>>>>> 0d531d2d32b6d1d53ac36c43f35ce6251b991b6c

if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='5000', debug=True)

import request, requests,  json, time
import cv2

cam = cv2.VideoCapture(0)
time.sleep(0.2)

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    image = cv2.imwrite("image.jpg", frame)

    with open(image, "rb") as imageFile:
        # f = imageFile.read()
        # b = bytearray(f)    
        url = 'http://192.168.8.10:5000/get_stream'
        header = {'Content-Type': 'application/octet-stream'}
        try:
            response = requests.post(url, files=[('image_data',('test.jpg', imageFile, 'image/jpg'))])
            print(response.status_code)
        except Exception as e:
            print(e)
            print ("Fehler")
        # res = requests.put(url, files={'image': imageFile}, headers=headers)
        # res = requests.get(url, data={'image': imageFile}, headers=headers)
        ##print received json response
        print(response.text)
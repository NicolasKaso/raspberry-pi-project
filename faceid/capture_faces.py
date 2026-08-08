from picamera2 import Picamera2
import cv2
import time

picam2 = Picamera2()
picam2.start()
face_detector = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')


count = 0
target_count = 30
while count < target_count:
    frame = picam2.capture_array()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)

    if len(faces) > 0:
        faces = sorted(faces, key = lambda f: f[2] * f[3], reverse = True)
        largest_face = faces[0]

        x, y, w, h = largest_face
        face_crop = gray[y:y+h, x:x+w]
    
        count += 1
        cv2.imwrite(f"dataset/face_{count}.jpeg", face_crop)
        print(f"saved {count} / {target_count}")

        time.sleep(0.5)

    
    else:
        print("no face detected")   

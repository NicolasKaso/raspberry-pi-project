#setup
import cv2
from picamera2 import Picamera2

face_detector = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

picam2 = Picamera2()
picam2.start()


#taking a photo and finding a face
def check_face():   
    frame = picam2.capture_array()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)

    if len(faces) > 0:
        x, y, w, h = faces[0]
        face_crop = gray[y:y+h, x:x+w]


#recognizing the face
        label, confidence = recognizer.predict(face_crop)
        
        if confidence < 60:
            return "Match"

        else:
            return "Unknown"

    else:
        return "No_face"


import cv2
import os
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer.create()

faces = []
labels = []

image_files = os.listdir("dataset")

for filename in image_files:
    path = os.path.join('dataset', filename)
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    
    if image is not None:
        faces.append(image)
        labels.append(1)


labels = np.array(labels)
recognizer.train(faces, labels)
recognizer.save("trainer.yml")
print("training complete, saved to trainer.yml")

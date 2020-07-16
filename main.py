import cv2
import numpy as np
import face_detect
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img1 = cv2.imread("images/real_3.jpg")
# Converting the image into grayscale
gray=cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img = face_detect.detect_faces(face_cascade, gray)
cv2.imshow('aligned image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

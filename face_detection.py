import cv2
import cv2.data
path = cv2.data.haarcascades +"haarcascade_frontalface_default.xml"
model = cv2.CascadeClassifier(path)
image = cv2.imread("./images.jpg")
faces = model.detectMultiScale(image, 1.3, 5)
for oneface in faces:
    x,y,w,h = oneface
    image = cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),3)
cv2.imshow("facessss",image)
cv2.waitKey(0)
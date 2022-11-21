import cv2
img = cv2.imread("4f.jpg")
gray =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face = faceCascade.detectMultiScale(gray) 
for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),3)

cropImage = img[y:y+h,x:x+w]
cv2.imwrite("face.jpg",cropImage)

cv2.imshow("image",img)
cv2.waitKey(0)






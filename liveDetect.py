import cv2
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
vid = cv2.VideoCapture(0)
while(True):
    ret,frame = vid.read()
    gray =  cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face = faceCascade.detectMultiScale(gray,1.1,4) 
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),3)
        cv2.imshow("webcam",frame)


    if  cv2.waitKey(25)==32:
        break

vid.release()
cv2.destroyAllWindows()

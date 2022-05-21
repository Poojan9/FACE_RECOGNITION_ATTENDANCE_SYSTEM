import cv2
from train import *
face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
def face_detector(img,size=0.5):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray,1.3,5)
    if face is():
        return img,[]
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi=img[y:y+h,x:x+w]
        roi=cv2.resize(roi,(200,200))


        return img,roi

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    image,face=face_detector(frame)

    try:
        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        result=Train.predict(face)

        if result[1]< 500:
            confidence=int(100*(1-(result[1]/300)))
        if confidence > 82:
            cv2.putText(image,"your name / user name",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            cv2.imshow("face cropper",image)
        else:
            cv2.putText(image,"unknown",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
            cv2.imshow("face cropper", image)
    except:
        cv2.putText(image,"face not found",(250,450),1,(255,0,0),2)
        cv2.imshow("face cropper", image)
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()


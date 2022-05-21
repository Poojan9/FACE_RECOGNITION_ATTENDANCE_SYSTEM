from tkinter import *
from mttkinter import mtTkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
from deepface import DeepFace



class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x792+0+0")    # first two values for length and width ,last two zeros stand for x and y axis
        self.root.title("Face Recognition System")
         #main label
        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 30, "bold"),
                          bg="white", fg="navy")
        title_lbl.place(x=0, y=0, width=1536, height=45)

        # image1
        img_1 = Image.open(r"images\Artificial-Intelligence-and-the-Future-of-Humans.jpg") #if we dont use backward slash then we used r
        img_1 = img_1.resize((1536, 753), Image.ANTIALIAS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        f_lbl = Label(self.root, image=self.photoimg_1)
        f_lbl.place(x=0, y=48, width=1536, height=753)
         #button
        b_11 = Button(f_lbl, text="Face Recognition",cursor="hand2",command=self.face_recog,
                     font=("times new roman", 15, "bold"), bg="black", fg="white")
        b_11.place(x=719, y=350, width=180, height=32)

#============================attendance=======================
    def mark_attendance(self,i1,n1,d1,s1):
        with open("barot.csv","r+",newline="\n") as f:
            mydatalist=f.readlines()
            name_list=[]
            for line in mydatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i1 not in name_list)) and ((n1 not in name_list)) and ((d1 not in name_list)) and ((s1 not in name_list)):
                now=datetime.now()
                d=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i1},{n1},{d1},{s1},{dtstring},{d},present")


#=================== face recognition ====================

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id, predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
               # confidence = int(100 * (1 - (predict[1] / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="poojan123@",
                                               database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT name FROM student WHERE EnNo = " + str(id))
                n = my_cursor.fetchone()
                n1 = "+".join(n)

                my_cursor.execute("SELECT dep FROM student WHERE EnNo = " + str(id))
                d = my_cursor.fetchone()
                d1 = "+".join(d)

                my_cursor.execute("SELECT sem FROM student WHERE EnNo = " + str(id))
                s = my_cursor.fetchone()
                s1 = "+".join(s)

                my_cursor.execute("SELECT EnNo FROM student WHERE EnNo = " + str(id))
                i = my_cursor.fetchone()
              #  i1 = "+".join(i)
                i1 = "+".join([str(v) for v in i])




                if confidence > 77:
                    cv2.putText(img, f"EnNo:{i1}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"name:{n1}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"dep:{d1}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"sem:{s1}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i1,n1,d1,s1)
                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h), (0, 0, 255), 3)

                    cv2.putText(img,"Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord=[x, y, w, y]
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img


        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)


        while True:
            ret, img = video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)


            if cv2.waitKey(1)==13: #enter
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
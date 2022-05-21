from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x792+0+0")    # first two values for length and width ,last two zeros stand for x and y axis
        self.root.title("Face Recognition System")
      # main title
        title_lbl = Label(self.root, text="Train Data Set", font=("times new roman", 30, "bold"),
                          bg="white", fg="navy")
        title_lbl.place(x=0, y=0, width=1536, height=45)

      #image1
        img_top = Image.open(
            r"images\ML.jpg")
        img_top = img_top.resize((1536, 380), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=48, width=1536, height=370)

        # button
        b_1 = Button(self.root, text="Train Data",command=self.train_classifier,cursor="hand2",
                      font=("times new roman", 20, "bold"), bg="aqua", fg="navy")
        b_1.place(x=0, y=418, width=1536, height=32)


      #image2
        img_down = Image.open(
            r"images\image2.jpg")
        img_down = img_down.resize((1536, 352), Image.ANTIALIAS)
        self.photoimg_down = ImageTk.PhotoImage(img_down)

        f_lbl = Label(self.root, image=self.photoimg_down)
        f_lbl.place(x=0, y=450, width=1536, height=352)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert("L")  #gray scale image
            imagenp=np.array(img,"uint8") #datatype of array
            id=int(os.path.split(image)[1].split(".")[1])

            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==13  #after enter close the window
        ids=np.array(ids)


        #================== train the classifier and save ===============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed !!")




if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
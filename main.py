import tkinter.messagebox
from tkinter import *
import tkinter
from tkinter import ttk
from PIL import ImageTk,Image
import os
from time import strftime
from datetime import datetime
from student import student
from train import Train
from face_recognition import Face_Recognition
from developer import Developer
from help import Help
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x792+0+0")    # first two values for length and width ,last two zeros stand for x and y axis
        self.root.title("Face Recognition System")

#bg image
        img =Image.open(r"images\5fce3f19f029a525723595.jpg")
        img=img.resize((1536,792),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1536,height=792)

#main title
        title_lbl=Label(bg_img,text="Face Recognition Attendance System",font=("times new roman",30,"bold"),bg="white",fg="navy")
        title_lbl.place(x=0,y=0,width=1536,height=45)

#=================time===================
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",14,"bold"),background="white",foreground="black")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

#====student button====
        img2=Image.open(r"images\students.jpg")
        img2=img2.resize((150,150),Image.ANTIALIAS) # aliasing effects
        self.photoimg2=ImageTk.PhotoImage(img2)
# tap on image
        b1 = Button(bg_img,image=self.photoimg2,command=self.student_details,cursor="hand2")
        b1.place(x=250,y=200,width=150,height=150)
#tap on student label
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=250,y=350,width=150,height=40)


#==========Detect Face button===========
        img3 = Image.open(r"images\face detector.jpg")
        img3 = img3.resize((150, 150), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
#tap on image
        b2 = Button(bg_img, image=self.photoimg3, cursor="hand2",command=self.face_data)
        b2.place(x=550, y=200, width=150, height=150)
#tap on detect face label
        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"), bg="navy blue",fg="white")
        b2_1.place(x=550, y=350, width=150, height=40)

#====Attendance=====
        img4 = Image.open(r"images\attendance.jfif")
        img4 = img4.resize((150, 150), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
#tap on image
        b3 = Button(bg_img, image=self.photoimg4, cursor="hand2",command=self.attendance_data)
        b3.place(x=850, y=200, width=150, height=150)
#tap on attendance label
        b3_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data, font=("times new roman", 15, "bold"), bg="navy blue",fg="white")
        b3_1.place(x=850, y=350, width=150, height=40)


#========Help desk Button==============
        img5 = Image.open(r"images\help.jpeg")
        img5 = img5.resize((150, 150), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
#tap on image
        b4 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.help)
        b4.place(x=1150, y=200, width=150, height=150)
#tap on help desk label
        b4_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help, font=("times new roman", 15, "bold"), bg="navy blue",fg="white")
        b4_1.place(x=1150, y=350, width=150, height=40)


#===========Training phase Button============
        img6 = Image.open(r"images\training.jpg")
        img6 = img6.resize((150, 150), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
#tap on image
        b5 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.train_data)
        b5.place(x=250, y=500, width=150, height=150)
#tap on training label
        b5_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data,font=("times new roman", 15, "bold"), bg="navy blue",fg="white")
        b5_1.place(x=250, y=650, width=150, height=40)

#==========Photos Button==============
        img7 = Image.open(r"images\photos.jpg")
        img7 = img7.resize((150, 150), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
#tap on image
        b6 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.open_img)
        b6.place(x=550, y=500, width=150, height=150)
#tap on photos label
        b6_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img,font=("times new roman", 15, "bold"), bg="navy blue",
                      fg="white")
        b6_1.place(x=550, y=650, width=150, height=40)

#======Developer Button=======
        img8 = Image.open(r"images\developer.jpg")
        img8 = img8.resize((150, 150), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
#tap on image
        b7 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.developer_data)
        b7.place(x=850, y=500, width=150, height=150)
#tap on developer label
        b7_1 = Button(bg_img, text="Developer", cursor="hand2",command=self.developer_data,font=("times new roman", 15, "bold"), bg="navy",
                      fg="white")
        b7_1.place(x=850, y=650, width=150, height=40)

#=======Exit Button=======
        img9 = Image.open(r"images\exit.jpg")
        img9 = img9.resize((150, 150), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
#tap on image
        b8 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.iExit)
        b8.place(x=1150, y=500, width=150, height=150)
#tap on exit label
        b8_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit,font=("times new roman", 15, "bold"), bg="navy",
                      fg="white")
        b8_1.place(x=1150, y=650, width=150, height=40)


#photos open in photos button
    def open_img(self):
        os.startfile("data")

#=======exit function============
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognization","Are you sure?",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return



    #============ function buttons ====================
#new windows for each button
    def student_details(self):
         self.new_window=Toplevel(self.root) #new window overlapp the main window
         self.app=student(self.new_window) #from pressing the button we go on new window

    def train_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Train(self.new_window)

    def face_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help(self):
        self.new_window = Toplevel(self.root)
        self.app =Help(self.new_window)



#exicute all the program
if __name__ == "__main__":
    root=Tk()# It helps to display the root window and manages all the other components of the tkinter application
    obj=Face_Recognition_System(root)
    root.mainloop()
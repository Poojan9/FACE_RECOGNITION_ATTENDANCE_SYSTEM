from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x792+0+0")    # first two values for length and width ,last two zeros stand for x and y axis
        self.root.title("Face Recognition System")

        # main title
        title_lbl = Label(self.root, text="Help Desk", font=("times new roman", 30, "bold"),
                          bg="white", fg="navy")
        title_lbl.place(x=0, y=0, width=1536, height=45)

        # image1
        img_top = Image.open(r"images\cloud-computing-concept.jpg")
        img_top = img_top.resize((1536, 755), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=48, width=1536, height=755)

        dev_label = Label( f_lbl, text="Email: barotpoojan91201@gmail.com", font=("times new roman", 15, "bold"),fg="navy", bg="white")
        dev_label.place(x=720, y=250)

if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
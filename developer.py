from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x792+0+0")    # first two values for length and width ,last two zeros stand for x and y axis
        self.root.title("Face Recognition System")

        # main title
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 30, "bold"),
                          bg="white", fg="navy")
        title_lbl.place(x=0, y=0, width=1536, height=45)

        # image1
        img_top = Image.open(r"images\wp4974476.webp")
        img_top = img_top.resize((1536, 792), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=48, width=1536, height=792)

        #frame
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=900, y=20, width=580, height=398)


        #developer info
        dev_label8 = Label(main_frame,
                           text="front end and back kjslahdksjdoqmkvfkkfkfkfkfkfkfkfkfkkkpppppkkkkkkkkkkkkkkkkk;ncnlfhaslfalkksjdkskkkskskkskskskskskskskskqoks;ljhdhkwdjq;ok;q end developer for python",
                           font=("times new roman", 5, "bold"), bg="black")
        dev_label8.place(x=0, y=5)

        dev_label = Label(main_frame, text="1.Barot Poojan B", font=("times new roman", 20, "bold"), bg="white")
        dev_label.place(x=0,y=45)

        dev_label1 = Label(main_frame, text="- front end and back end developer for python", font=("times new roman", 15, "bold"), bg="white")
        dev_label1.place(x=0, y=85)

        dev_label2= Label(main_frame, text="2.Patel Manthan B", font=("times new roman", 20, "bold"), bg="white")
        dev_label2.place(x=0, y=125)

        dev_label3 = Label(main_frame, text="- front end and back end developer for python",
                           font=("times new roman", 15, "bold"), bg="white")
        dev_label3.place(x=0, y=165)

        dev_label4 = Label(main_frame, text="3.Panchal Jigar K", font=("times new roman", 20, "bold"), bg="white")
        dev_label4.place(x=0, y=205)

        dev_label5 = Label(main_frame, text="- front end and back end developer for python",
                           font=("times new roman", 15, "bold"), bg="white")
        dev_label5.place(x=0, y=245)

        dev_label6 = Label(main_frame, text="4.Thakor Krunal M", font=("times new roman", 20, "bold"), bg="white")
        dev_label6.place(x=0, y=285)

        dev_label7 = Label(main_frame, text="- front end and back end developer for python",
                           font=("times new roman", 15, "bold"), bg="white")
        dev_label7.place(x=0, y=325)

        dev_label8 = Label(main_frame, text="front end and back kjslahdksjdoqmkvfkkfkfkfkfkfkfkfkfkkkpppppkkkkkkkkkkkkkkkkk;ncnlfhaslfalkksjdkskkkskskkskskskskskskskskqoks;ljhdhkwdjq;ok;q end developer for python",
                           font=("times new roman", 5, "bold"), bg="black")
        dev_label8.place(x=0, y=375)




if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
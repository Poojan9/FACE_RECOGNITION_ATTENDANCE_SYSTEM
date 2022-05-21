from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
import cv2


class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x792+0+0")    # first two values for length and width ,last two zeros stand for x and y axis
        self.root.title("Face Recognition System") #main title

        #============variables==================
        #using this variables we have to fill entries and combo boxes when we tap on the table where the data is
        self.var_dep=StringVar()
        self.var_Course= StringVar()
        self.var_Year= StringVar()
        self.var_Sem= StringVar()
        self.var_EnNo= StringVar()
        self.var_name= StringVar()
        self.var_gender= StringVar()
        self.var_dob= StringVar()
        self.var_phoneno= StringVar()
        self.var_email= StringVar()
        self.var_address= StringVar()
        self.var_mentorname= StringVar()


#=======bg image========
        img = Image.open(r"C:\Users\barot\OneDrive\Pictures\Saved Pictures\5fce3f19f029a525723595.jpg")
        img = img.resize((1536, 792), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1536, height=792)

#=======main title=========
        title_lbl = Label(bg_img, text="Student Management System", font=("times new roman", 30, "bold"),
                          bg="white", fg="navy")
        title_lbl.place(x=0, y=0, width=1536, height=45)

#main frame(upon the bg image)
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1510,height=727)

# left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"))
        left_frame.place(x=5, y=9, width=745, height=707)

# image
        img_left=Image.open(r"C:\Users\barot\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\images\student-engagement-definition-1024x619-1.jpg")
        img_left=img_left.resize((735,250),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=3,y=0,width=735,height=250)

 #frame :current cource information
        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Cource Information",
                                font=("times new roman", 12, "bold"))
        current_course_frame.place(x=3, y=260, width=735, height=130)


        # innear label : department
        dep_label=Label(current_course_frame,text="Department :",font=("times new roman", 11, "bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=12)
        #combo box for department
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman", 11, "bold"),width=25,state="readonly")
        dep_combo["values"]=("Select Department","Computer","Information Technology","Civil","Mechanical","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=7,pady=12,sticky=W)


        #innear label : course
        course_label = Label(current_course_frame, text="Course :", font=("times new roman", 11, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=12,sticky=W)
        # combo box for course
        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_Course,font=("times new roman", 11, "bold"), width=25, state="readonly")
        course_combo["values"] = ("Select Course","FE","SE","TE","BE","ME") #fe=further education,se=systems engineering,te=telecom engineering
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=7, pady=12, sticky=W)


        #innear label : year
        year_label = Label(current_course_frame, text="Year :", font=("times new roman", 11, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=12, sticky=W)
        # combo box for year
        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_Year, font=("times new roman", 11, "bold"), width=25, state="readonly")
        year_combo["values"] = ("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=7, pady=12, sticky=W)

        # innear label : semester
        sem_label = Label(current_course_frame, text="Semester :", font=("times new roman", 11, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=12, sticky=W)
        # combo box for semester
        sem_combo = ttk.Combobox(current_course_frame,textvariable=self.var_Sem, font=("times new roman", 11, "bold"), width=25,state="readonly")
        sem_combo["values"] = ("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=7, pady=12, sticky=W) #sticky: for cell problems


       #frame : class student information
        class_stud_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information",
                                          font=("times new roman", 12, "bold"))
        class_stud_frame.place(x=3, y=400, width=735, height=280)

        #innear label : en no
        enno_label = Label(class_stud_frame, text="Enrollment_No :", font=("times new roman", 11, "bold"), bg="white")
        enno_label.grid(row=0, column=0, padx=7, sticky=W)
        #entry for en no
        enno_entry=ttk.Entry(class_stud_frame,width=25,textvariable=self.var_EnNo,font=("times new roman", 11, "bold"))
        enno_entry.grid(row=0,column=1,padx=5,pady=7,sticky=W)

        #innear label : Student name
        studname_label = Label(class_stud_frame, text="Student_Name :", font=("times new roman", 11, "bold"), bg="white")
        studname_label.grid(row=0, column=2, padx=7, sticky=W)
        # entry for student name
        studname_entry = ttk.Entry(class_stud_frame, width=25,textvariable=self.var_name,font=("times new roman", 11, "bold"))
        studname_entry.grid(row=0, column=3, padx=5, pady=7, sticky=W)

        #innear label : gender
        gen_label = Label(class_stud_frame, text="Gender :", font=("times new roman", 11, "bold"),bg="white")
        gen_label.grid(row=1, column=0, padx=7, sticky=W)
        # entry for gender
        gender_combo = ttk.Combobox(class_stud_frame, textvariable=self.var_gender,
                                  font=("times new roman", 11, "bold"), width=23, state="readonly")
        gender_combo["values"] = ("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=1, padx=5, pady=7, sticky=W)

        # innear label : DOB
        dob_label = Label(class_stud_frame, text="DOB :", font=("times new roman", 11, "bold"), bg="white")
        dob_label.grid(row=1, column=2, padx=7, sticky=W)
        # entry for gender
        dob_entry = ttk.Entry(class_stud_frame, width=25,textvariable=self.var_dob,font=("times new roman", 11, "bold"))
        dob_entry.grid(row=1, column=3, padx=5, pady=7, sticky=W)

        # innear label : phone no
        phn_label = Label(class_stud_frame, text="Phone_No :", font=("times new roman", 11, "bold"), bg="white")
        phn_label.grid(row=2, column=0, padx=7, sticky=W)
        # entry for phone no
        phn_entry = ttk.Entry(class_stud_frame, width=25,textvariable=self.var_phoneno,font=("times new roman", 11, "bold"))
        phn_entry.grid(row=2, column=1, padx=5, pady=7, sticky=W)

        # innear label : email
        em_label = Label(class_stud_frame, text="Email :", font=("times new roman", 11, "bold"), bg="white")
        em_label.grid(row=2, column=2, padx=7, sticky=W)
        # entry for email
        em_entry = ttk.Entry(class_stud_frame, width=25,textvariable=self.var_email, font=("times new roman", 11, "bold"))
        em_entry.grid(row=2, column=3, padx=5, pady=7, sticky=W)

        # innear label : address
        adr_label = Label(class_stud_frame, text="Address :", font=("times new roman", 11, "bold"), bg="white")
        adr_label.grid(row=3, column=0, padx=7, sticky=W)
        # entry for gender
        adr_entry = ttk.Entry(class_stud_frame, width=25,textvariable=self.var_address ,font=("times new roman", 11, "bold"))
        adr_entry.grid(row=3, column=1, padx=5, pady=7, sticky=W)


        #innear label : mentor name
        mename_label = Label(class_stud_frame, text="Mentor_Name :", font=("times new roman", 11, "bold"), bg="white")
        mename_label.grid(row=3, column=2, padx=7, sticky=W)
        # entry for mentorname
        mename_entry = ttk.Entry(class_stud_frame, width=25,textvariable=self.var_mentorname, font=("times new roman", 11, "bold"))
        mename_entry.grid(row=3, column=3, padx=5, pady=7, sticky=W)


        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_stud_frame,variable=self.var_radio1,text="Take Photo Sample",value="YES")
        radiobtn1.grid(row=5,column=0)


        radiobtn2 = ttk.Radiobutton(class_stud_frame,variable=self.var_radio1,text="No Photo Sample", value="NO")
        radiobtn2.grid(row=5, column=1)


#button frame0
        btn_frame=Frame(class_stud_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=180,width=720,height=35)


        #save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="orange",fg="black")
        save_btn.grid(row=0,column=0)

        #update button
        update_btn = Button(btn_frame, text="Update", command=self.Update_data,width=19, font=("times new roman", 12, "bold"), bg="orange", fg="black")
        update_btn.grid(row=0, column=1)

        #delete button
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data,width=19, font=("times new roman", 12, "bold"), bg="orange", fg="black")
        delete_btn.grid(row=0, column=2)

        #reset button
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data,width=19, font=("times new roman", 12, "bold"), bg="orange", fg="black")
        reset_btn.grid(row=0, column=3)


#button frame1
        btn1_frame = Frame(class_stud_frame, bd=2, relief=RIDGE, bg="white")#ridge gives 3-d effect to the button
        btn1_frame.place(x=5, y=215, width=720, height=35)


        #take photo sample
        takepic_btn = Button(btn1_frame,command=self.generate_dataset, text="Take Photo Sample", width=39 , font=("times new roman", 12, "bold"), bg="orange",
                           fg="black")
        takepic_btn.grid(row=0, column=0)

        # update photo sample
        updpic_btn = Button(btn1_frame, text="Update Photo Sample", width=39, font=("times new roman", 12, "bold"),
                             bg="orange",
                             fg="black")
        updpic_btn.grid(row=0, column=1)





        # right label frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        right_frame.place(x=755, y=9, width=745, height=707)

        #image
        img_right = Image.open(r"C:\Users\barot\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\images\facebook.jpg")
        img_right = img_right.resize((735, 250), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=0, y=0, width=735, height=250)


        #============== search system ======================
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                    font=("times new roman", 12, "bold"))
        search_frame.place(x=3, y=260, width=735, height=70)


        #label : search by
        search_label = Label(search_frame, text="Search By :", font=("times new roman", 11, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=7, sticky=W)


       #combobox for label
        search_combo = ttk.Combobox(search_frame, font=("times new roman", 11, "bold"), width=16, state="readonly")
        search_combo["values"] = ("Select","Enrollment No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=7, pady=12, sticky=W)


        #entry
        search_entry = ttk.Entry(search_frame, width=16, font=("times new roman", 11, "bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=7, sticky=W)


        #button

        search_btn = Button(search_frame, text="Search", width=16, font=("times new roman", 12, "bold"), bg="orange",
                            fg="black")
        search_btn.grid(row=0, column=3,padx=4)

        showall_btn = Button(search_frame, text="Show All", width=16, font=("times new roman", 12, "bold"), bg="orange",
                            fg="black")
        showall_btn.grid(row=0, column=4)

        #table frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=3, y=340, width=735, height=340)


        #scrollbar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","Course","Year","Sem","EnNo","name","gender","dob","phoneno","email","address","mentorname","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)



        self.student_table.heading("dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("EnNo",text="Enrollment No")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("phoneno",text="Phone No")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("mentorname",text="Mentor Name")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        self.student_table.column("dep",width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("EnNo", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("phoneno", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("mentorname", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



    #==============function declaration==============
    #for saving data into databse

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()== "" or self.var_EnNo.get()=="":
              messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="poojan123@",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_Course.get(),
                                                                                                        self.var_Year.get(),
                                                                                                        self.var_Sem.get(),
                                                                                                        self.var_EnNo.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_phoneno.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_mentorname.get(),
                                                                                                        self.var_radio1.get()
                                                                                                       ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)



      #=================== fetch data ==================

    def fetch_data(self ):
        conn = mysql.connector.connect(host="localhost", username="root", password="poojan123@",
                                       database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()


        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()




       #=============== get cursor =============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_Course.set(data[1])
        self.var_Year.set(data[2])
        self.var_Sem.set(data[3])
        self.var_EnNo.set(data[4])
        self.var_name.set(data[5])
        self.var_gender.set(data[6])
        self.var_dob.set(data[7])
        self.var_phoneno.set(data[8])
        self.var_email.set(data[9])
        self.var_address.set(data[10])
        self.var_mentorname.set(data[11])
        self.var_radio1.set(data[12])


    #update function
    def Update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_EnNo.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="poojan123@",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE student SET dep=%s, Course=%s,Year=%s,Sem=%s,name=%s,gender=%s,dob=%s,phoneno=%s,email=%s,address=%s,mentorname=%s,photo=%s WHERE EnNo= %s",(

                                                                                            self.var_dep.get(),
                                                                                            self.var_Course.get(),
                                                                                            self.var_Year.get(),
                                                                                            self.var_Sem.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_phoneno.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_mentorname.get(),
                                                                                            self.var_radio1.get(),
                                                                                            self.var_EnNo.get()
                                                                                                ))

                else:
                    if not Update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)



    #================== delete function ==================
    def  delete_data(self):
        if self.var_EnNo.get()=="":
            messagebox.showerror("Error","Enrollment No must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete this student",parent=self.root)
                if delete >0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="poojan123@",
                                           database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from student where EnNo=%s"
                    val=(self.var_EnNo.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


# ======================== reset ===================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_Course.set("Select Course")
        self.var_Year.set("Select Year")
        self.var_Sem.set("Select Semester")
        self.var_EnNo.set("")
        self.var_name.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phoneno.set("")
        self.var_address.set("")
        self.var_mentorname.set("")
        self.var_radio1.set("")



      #================ generate data set or take photo sample ================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_EnNo.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="poojan123@",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult: #for collection of data
                    id+=1
                my_cursor.execute("UPDATE student SET dep=%s, Course=%s,Year=%s,Sem=%s,name=%s,gender=%s,dob=%s,phoneno=%s,email=%s,address=%s,mentorname=%s,photo=%s WHERE EnNo= %s",
                  (

                    self.var_dep.get(),
                    self.var_Course.get(),
                    self.var_Year.get(),
                    self.var_Sem.get(),
                    self.var_name.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_phoneno.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_mentorname.get(),
                    self.var_radio1.get(),
                    self.var_EnNo.get()==id+1
                   ))
                conn.commit()
                self.fetch_data()
                #self.reset_data()
                conn.close()

 #============= load predefined data on face frontals from opencv ===========
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #file for object detection


                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor =1.3(by default)
                    #minimum neighbour=5(by default)

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)   #0 for web camera
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==200: #enter
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed !!!")


            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()
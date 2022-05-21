from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x792+0+0")    # first two values for length and width ,last two zeros stand for x and y axis
        self.root.title("Face Recognition System")
#variables
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_sem = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()

        # bg image
        img = Image.open(r"C:\Users\barot\OneDrive\Pictures\Saved Pictures\5fce3f19f029a525723595.jpg")
        img = img.resize((1536, 792), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1536, height=792)

        # main title
        title_lbl = Label(bg_img, text="Attendance Management System", font=("times new roman", 30, "bold"),
                          bg="white", fg="navy")
        title_lbl.place(x=0, y=0, width=1536, height=45)

        # main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1510, height=727)

        # left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",
                                font=("times new roman", 12, "bold"))
        left_frame.place(x=5, y=9, width=745, height=707)

        # image
        img_left = Image.open(
            r"C:\Users\barot\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\images\student-engagement-definition-1024x619-1.jpg")
        img_left = img_left.resize((735, 350), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=3, y=0, width=735, height=350)

        # frame : left_inside_frame
        left_inside_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE)
        left_inside_frame.place(x=3, y=360, width=735, height=320)
 #labels and entry
        # innear label :student id
        studentid_label = Label( left_inside_frame, text="Student_ID :", font=("times new roman", 11, "bold"), bg="white")
        studentid_label.grid(row=0, column=0, padx=15, sticky=W)
        # entry for en no
        studentid_entry = ttk.Entry( left_inside_frame, width=25,textvariable=self.var_id, font=("times new roman", 11, "bold"))
        studentid_entry.grid(row=0, column=1, padx=10, pady=15, sticky=W)



        # innear label :name
        studentname_label = Label(left_inside_frame, text="Student_Name :", font=("times new roman", 11, "bold"),
                                bg="white")
        studentname_label.grid(row=0, column=2, padx=15, sticky=W)
        # entry for name
        studentname_entry = ttk.Entry(left_inside_frame, width=25,textvariable=self.var_name, font=("times new roman", 11, "bold"))
        studentname_entry.grid(row=0, column=3, padx=10, pady=15, sticky=W)

        # innear label :department
        studentdep_label = Label(left_inside_frame, text="Department :", font=("times new roman", 11, "bold"),
                                bg="white")
        studentdep_label.grid(row=1, column=0, padx=15, sticky=W)
        # entry for department
        studentdep_entry = ttk.Entry(left_inside_frame, width=25, textvariable=self.var_dep,font=("times new roman", 11, "bold"))
        studentdep_entry.grid(row=1, column=1, padx=10, pady=15, sticky=W)

        # innear label :sem
        studentsem_label = Label(left_inside_frame, text="Sem :", font=("times new roman", 11, "bold"),
                                bg="white")
        studentsem_label.grid(row=1, column=2, padx=15, sticky=W)
        # entry for sem
        studentsem_entry = ttk.Entry(left_inside_frame, width=25, textvariable=self.var_sem,font=("times new roman", 11, "bold"))
        studentsem_entry.grid(row=1, column=3, padx=10, pady=15, sticky=W)

        # innear label :time
        time_label = Label(left_inside_frame, text="Time :", font=("times new roman", 11, "bold"),
                                bg="white")
        time_label.grid(row=2, column=0, padx=15, sticky=W)
        # entry for time
        time_entry = ttk.Entry(left_inside_frame, width=25,textvariable=self.var_time, font=("times new roman", 11, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=15, sticky=W)

        # innear label :Date
        Date_label = Label(left_inside_frame, text="Date :", font=("times new roman", 11, "bold"),
                                bg="white")
        Date_label.grid(row=2, column=2, padx=15, sticky=W)
        # entry for date
        Date_entry = ttk.Entry(left_inside_frame, width=25, textvariable=self.var_date,font=("times new roman", 11, "bold"))
        Date_entry.grid(row=2, column=3, padx=10, pady=15, sticky=W)

        # innear label :attendance
        attendance_label = Label(left_inside_frame, text="Attendance :", font=("times new roman", 11, "bold"),
                                bg="white")
        attendance_label.grid(row=3, column=0, padx=15, sticky=W)
        # entry for attendance
        attendance_combo = ttk.Combobox(left_inside_frame,
                                  font=("times new roman", 11, "bold"), width=23, textvariable=self.var_attendance,state="readonly")
        attendance_combo["values"] = ("Status","Present","Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=3, column=1, padx=10, pady=15, sticky=W)

        # button frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=250, width=720, height=35)

        # importcsv button
        importcsv_btn = Button(btn_frame, text="Import_CSV", command=self.importCsv,width=26, font=("times new roman", 12, "bold"),
                          bg="orange", fg="black")
        importcsv_btn.grid(row=0, column=0)

        # exportcsv button
        exportcsv_btn = Button(btn_frame, text="Export_CSV",command=self.exportCsv, width=26,
                            font=("times new roman", 12, "bold"), bg="orange", fg="black")
        exportcsv_btn.grid(row=0, column=1)

       # reset button
        reset_btn = Button(btn_frame, text="Reset", width=26,command=self.reset_data,
                           font=("times new roman", 12, "bold"), bg="orange", fg="black")
        reset_btn.grid(row=0, column=3)


        # right label frame
        right_inside_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",
                                 font=("times new roman", 12, "bold"))
        right_inside_frame.place(x=755, y=9, width=745, height=707)

        # button frame
        table_frame = Frame(right_inside_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=731, height=668)

        # scrollbar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.AttendanceReportTable = ttk.Treeview(table_frame, column=(
        "ID", "Name", "Department", "Sem", "Time", "Date", "Attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("ID", text="Student_ID")
        self.AttendanceReportTable.heading("Name", text="Student_Name")
        self.AttendanceReportTable.heading("Department", text="Department")
        self.AttendanceReportTable.heading("Sem", text="Semester")
        self.AttendanceReportTable.heading("Time", text="Time")
        self.AttendanceReportTable.heading("Date", text="Date")
        self.AttendanceReportTable.heading("Attendance", text="Attendance")
        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("ID", width=130)
        self.AttendanceReportTable.column("Name", width=130)
        self.AttendanceReportTable.column("Department", width=130)
        self.AttendanceReportTable.column("Sem", width=130)
        self.AttendanceReportTable.column("Time", width=130)
        self.AttendanceReportTable.column("Date", width=130)
        self.AttendanceReportTable.column("Attendance", width=130)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.getcursor)
 #============fetch data=============

    def fetchdata(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)

#import csv
    def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("all file","*.*")),parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchdata(mydata)
#export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("all file","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data exported to "+ os.path.basename(fln)+" Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    def getcursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_id.set(rows[0])
        self.var_name.set(rows[1])
        self.var_dep.set(rows[2])
        self.var_sem.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendance.set(rows[6])

    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_sem.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")






if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
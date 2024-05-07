from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector


class Student_Detail():
    def __init__(self,root):
        self.root = root
        self.root.title("STUDENT DETAIL")
        self.root.geometry("1080x720")
        self.root.resizable(FALSE,FALSE)

        #============variables
        self.var_dept = StringVar()
        self.var_session = StringVar()
        self.var_semester = StringVar()
        self.var_roll = StringVar()
        self.var_reg = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()

        bg_img = Image.open("assets/images/BSonoma_Mac.png")
        bg_img = bg_img.resize((1080, 720))
        self.photoimg = ImageTk.PhotoImage(bg_img)

        bg_img_label = Label(self.root, image=self.photoimg)
        bg_img_label.place(x=0, y=0, width=1080, height=720)

        title_label = Label(bg_img_label,
                            text="STUDENT DETAILS",
                            font=("arial", 20, "bold"), fg="black", bg="white")
        title_label.place(x=0, y=0, width=1080, height=30)

        main_frame = Frame(bg_img_label,bg="white")
        main_frame.place(x=0, y=80, width=1080, height=680)

        """-------------------------Left Label Begins----------------------------------"""
        #left label
        left_frame = LabelFrame(main_frame,
                                bd=2,
                                relief=RIDGE,
                                text="Student Details",
                                font=("arial", 20),
                                bg="white",
                                )
        left_frame.place(x=10, y=10, width=525, height=620)

        """                    ---Current Course Ends(Left Label)---                      """
        #current course frame
        current_course_frame = LabelFrame(left_frame,
                                          bd=2,
                                          relief=RIDGE,
                                          text="COURSE INFORMATION",
                                          font=("arial",12,"bold"),
                                          bg="white",
                                          pady=10)
        current_course_frame.place(x=5, y=18, width=510, height=120)

        #department detail
        dept_label = Label(current_course_frame,
                           #textvariable=self.var_dept,
                           text="Department",
                           font=("arial", 12),
                           bg="white")
        dept_label.grid(row=0, column=0,padx=2,pady=2,sticky=W)

        dept_combo = ttk.Combobox(current_course_frame,
                                  textvariable=self.var_dept,
                                  font=("arial", 12),
                                  width=17,
                                  state="readonly")
        dept_combo["values"] = ("Select Department","Computer Science","Artificial Engineering")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1,padx=2,pady=2,sticky=W)

        #Session detail
        Session_label = Label(current_course_frame,
                              #textvariable=self.var_session,
                              text="Session",
                              font=("arial", 12),
                              bg="white")
        Session_label.grid(row=0, column=2, padx=2, pady=2, sticky=W)

        Session_combo = ttk.Combobox(current_course_frame,
                                     textvariable=self.var_session,
                                     font=("arial", 12),
                                     width=11,
                                     state="readonly")
        Session_combo["values"] = ("Select Session","2020-24","2021-25", "2022-26", "2023-27")
        Session_combo.current(0)
        Session_combo.grid(row=0, column=3, padx=2, pady=2, sticky=W)

        #Semester detail
        Semester_label = Label(current_course_frame,
                               #textvariable=self.var_semester,
                               text="Semester",
                               font=("arial", 12),
                               bg="white")
        Semester_label.grid(row=1, column=0, padx=2, pady=2, sticky=W)

        Semester_combo = ttk.Combobox(current_course_frame,
                                      textvariable=self.var_semester,
                                      font=("arial", 12),
                                      width=11,
                                      state="readonly")
        Semester_combo["values"] = ("Select Semester", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        Semester_combo.current(0)
        Semester_combo.grid(row=1, column=1, padx=2, pady=2, sticky=W)

        """                    ---Current Course Ends(Left Label)---                      """

        """                  ---Class Information Starts(Left Label)---                   """
        #Class Information
        class_student_frame = LabelFrame(left_frame,
                                          bd=2,
                                          relief=RIDGE,
                                          text="CLASS INFORMATION",
                                          font=("arial", 12,"bold"),
                                          bg="white",
                                          pady=10)
        class_student_frame.place(x=5, y=160, width=510, height=150)

        #Roll Number
        roll_label = Label(class_student_frame,
                           #textvariable=self.var_roll,
                           text="Roll Number",
                           font=("arial", 12),
                           bg="white")
        roll_label.grid(row=0, column=0, padx=2, pady=2, sticky=W)

        roll_entry = ttk.Entry(class_student_frame,
                               textvariable=self.var_roll,
                               width=12,
                               font=("arial",12))
        roll_entry.grid(row=0, column=1, padx=2, pady=2, sticky=W)

        # Registration Number
        reg_label = Label(class_student_frame,
                          #textvariable=self.var_reg,
                          text="Reg Number",
                          font=("arial", 12),
                          bg="white")
        reg_label.grid(row=0, column=2, padx=2, pady=2, sticky=W)

        reg_entry = ttk.Entry(class_student_frame,
                              textvariable=self.var_reg,
                              width=15,
                              font=("arial", 12))
        reg_entry.grid(row=0, column=3, padx=2, pady=2, sticky=W)

        #Phone Number
        phone_label = Label(class_student_frame,
                            #textvariable=self.var_phone,
                            text="Phone Number",
                            font=("arial", 12),
                            bg="white")
        phone_label.grid(row=1, column=0, padx=2, pady=2, sticky=W)

        phone_entry = ttk.Entry(class_student_frame,
                                textvariable=self.var_phone,
                                width=12,
                                font=("arial", 12))
        phone_entry.grid(row=1, column=1, padx=2, pady=2, sticky=W)

        # Student Name
        student_name_label = Label(class_student_frame,
                            text="Student Name",
                            font=("arial", 12),
                            bg="white")
        student_name_label.grid(row=2, column=0, padx=2, pady=2, sticky=W)

        student_name_entry = ttk.Entry(class_student_frame,
                                       textvariable=self.var_name,
                                       width=12,
                                       font=("arial", 12))
        student_name_entry.grid(row=2, column=1, padx=2, pady=2, sticky=W)

        # Email
        email_label = Label(class_student_frame,
                                   text="Email",
                                   font=("arial", 12),
                                   bg="white")
        email_label.grid(row=1, column=2, padx=2, pady=2, sticky=W)

        email_entry = ttk.Entry(class_student_frame,
                                textvariable=self.var_email,
                                width=17,
                                font=("arial", 12))
        email_entry.grid(row=1, column=3, padx=2, pady=2, sticky=W)

        #DOB detail
        dob_label = Label(class_student_frame,
                            text="DOB",
                            font=("arial", 12),
                            bg="white")
        dob_label.grid(row=2, column=2, padx=2, pady=2, sticky=W)

        dob_entry = ttk.Entry(class_student_frame,
                              textvariable=self.var_dob,
                              width=12,
                              font=("arial", 12))
        dob_entry.grid(row=2, column=3, padx=2, pady=2, sticky=W)

        """                  ---Class Information Ends(Left Label)---                   """

        """                 ---Radio Button Frame Starts(Left Label)---                 """
        #Radio Button Frame
        radio_btn_frame = LabelFrame(left_frame,
                                          bd=2,
                                          relief=RIDGE,
                                          text="REGISTER IMAGES",
                                          font=("arial", 12, "bold"),
                                          bg="white",
                                          pady=10)
        radio_btn_frame.place(x=5, y=340, width=510, height=70)

        #Radio Buttons
        self.var_radio_reg = StringVar()
        reg_img_btn = ttk.Radiobutton(radio_btn_frame,
                                      variable=self.var_radio_reg,
                                         text = "Register Images",
                                         value="yes",
                                         width=22)
        reg_img_btn.grid(row=0,column = 0,padx=15,pady=5)

        null_reg_img_btn = ttk.Radiobutton(radio_btn_frame,
                                           variable=self.var_radio_reg,
                                      text="No Register Images",
                                      value="no",
                                      width=22)
        null_reg_img_btn.grid(row=0, column=1,padx=15,pady=5)
        """                 ---Radio Button Frame Ends(Left Label)---                 """

        """              ---Save/Update Button Frame Starts(Left Label)---                 """
        #Button Frame
        btn_frame = Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5, y=430, width=510, height=90)

        #Save Button
        save_btn = Button(btn_frame,
                          text="Save",
                          width = 21,
                          font=("arial", 15, "bold"),
                          bg="blue",
                          fg="white",
                          command=self.add_data)
        save_btn.grid(row=0,column=0,padx=1,pady=3)

        # Update Button
        update_btn = Button(btn_frame,
                          text="Update",
                          width=21,
                          font=("arial", 14, "bold"),
                          bg="blue",
                          fg="white",
                          command=self.update_data)
        update_btn.grid(row=0, column=1, padx=1, pady=3)

        # Delete Button
        delete_btn = Button(btn_frame,
                          text="Delete",
                          width=21,
                          font=("arial", 14, "bold"),
                          bg="blue",
                          fg="white",
                          command=self.delete_data)
        delete_btn.grid(row=1, column=0, padx=1, pady=3)

        # Reset Button
        reset_btn = Button(btn_frame,
                          text="Reset",
                          width=21,
                          font=("arial", 14, "bold"),
                          bg="blue",
                          fg="white",
                          command=self.reset_data)
        reset_btn.grid(row=1, column=1, padx=1, pady=3)

        #Button Frame 2
        btn_frame2 = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame2.place(x=5, y=530, width=510, height=40)

        # Take Photo Button
        take_photo_btn = Button(btn_frame2,
                          text="Take Photo Sample",
                          width=21,
                          font=("arial", 14, "bold"),
                          bg="blue",
                          fg="white")
        take_photo_btn.grid(row=0, column=0, padx=1, pady=3)

        # Update Photo Button
        update_photo_btn = Button(btn_frame2,
                                text="Update Photo Sample",
                                width=21,
                                font=("arial", 14, "bold"),
                                bg="blue",
                                fg="white")
        update_photo_btn.grid(row=0, column=1, padx=1, pady=3)

        """               ---Save/Update Frame Ends(Left Label)---                 """

        """--------------------------------Left Label Ends================================"""


        # right label
        right_frame = LabelFrame(main_frame,
                                bd=2,
                                relief=RIDGE,
                                text="Student Details",
                                font=("arial", 20),
                                bg="white")
        right_frame.place(x=540, y=10, width=530, height=620)

        #Search System
        search_frame = LabelFrame(right_frame,
                                  text="Search System",
                                  font=("arial", 15,"bold"),
                                  relief=RIDGE,
                                  bg="white")
        search_frame.place(x=5, y=18, width=520, height=70)

        search_label = Label(search_frame,
                            text="Search By",
                            font=("arial", 11),
                            fg="red"
                            )
        search_label.grid(row=0, column=0, padx=2, pady=2, sticky=W)

        search_combo = ttk.Combobox(search_frame,
                                  font=("arial", 12),
                                  width=11,
                                  state="readonly")
        search_combo["values"] = ("Select", "Department", "Roll No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=2, sticky=W)

        search_entry = ttk.Entry(search_frame,
                                width=12,
                                font=("arial", 12))
        search_entry.grid(row=0, column=2, padx=2, pady=2, sticky=W)

        search_btn = ttk.Button(search_frame,
                          text="Search",
                          width=10,
                          #font=("arial", 14, "bold"),
                          #bg="red",
                          #fg="white")
                          style="info.TButton"
                          )
        search_btn.grid(row=0, column=3, padx=1, pady=3)

        show_all_btn = ttk.Button(search_frame,
                            text="Show All",
                            width=10,
                            #font=("arial", 14, "bold"),
                            #bg="red",
                            #fg="#FF0000")
                            style="info.TButton"
                            )
        show_all_btn.grid(row=0, column=4, padx=1, pady=3)

        #table frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=90, width=520, height=490)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.search_table = ttk.Treeview(table_frame,
                                         columns=("reg","dept","session","roll",
                                                  "student_name",
                                                  "phone","semester",
                                                  "email","dob","sample"),
                                         xscrollcommand=scroll_x.set,
                                         yscrollcommand=scroll_y.set)
        scroll_x.pack(side = BOTTOM, fill=X)
        scroll_y.pack(side = RIGHT, fill=Y)
        scroll_x.config(command=self.search_table.xview)
        scroll_y.config(command=self.search_table.yview)

        self.search_table.heading("reg", text="Registration No", anchor=CENTER)
        self.search_table.heading("dept", text="Department", anchor=CENTER)
        self.search_table.heading("session", text="Session", anchor=CENTER)
        self.search_table.heading("roll", text="Roll No", anchor=CENTER)
        self.search_table.heading("student_name", text="Student Name", anchor=CENTER)
        self.search_table.heading("phone", text="Phone No", anchor=CENTER)
        self.search_table.heading("semester", text="Semester", anchor=CENTER)
        self.search_table.heading("email", text="Email", anchor=CENTER)
        self.search_table.heading("dob", text="Date Of Birth", anchor=CENTER)
        self.search_table.heading("sample", text="Sample", anchor=CENTER)
        self.search_table["show"] = "headings"

        self.search_table.column("reg", width=100)
        self.search_table.column("dept", width=100)
        self.search_table.column("session", width=100)
        self.search_table.column("roll", width=100)
        self.search_table.column("student_name", width=100)
        self.search_table.column("phone", width=100)
        self.search_table.column("semester", width=100)
        self.search_table.column("email", width=100)
        self.search_table.column("dob", width=100)
        self.search_table.column("sample", width=100)

        self.search_table.pack(fill=BOTH, expand=1)
        self.search_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #======================function declaration
    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_semester.get()==" Select Semester" or self.var_session.get()=="Select Session":
            return messagebox.showerror("Field Not Filled", "Please fill all fields before saving",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="9504",database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                  self.var_reg.get(),
                                  self.var_dept.get(),
                                  self.var_session.get(),
                                  self.var_roll.get(),
                                  self.var_name.get(),
                                  self.var_phone.get(),
                                  self.var_semester.get(),
                                  self.var_email.get(),
                                  self.var_dob.get(),
                                  self.var_radio_reg.get()
                              ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Details have been addded",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #===================fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="9504",database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.search_table.delete(*self.search_table.get_children())
            for i in data:
                self.search_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #=======================get cursor
    def get_cursor(self,event=""):
        cursor_focus = self.search_table.focus()
        content = self.search_table.item(cursor_focus)
        data = content["values"]

        self.var_reg.set(data[0]),
        self.var_dept.set(data[1]),
        self.var_session.set(data[2])
        self.var_roll.set(data[3]),
        self.var_name.set(data[4]),
        self.var_phone.set(data[5]),
        self.var_semester.set(data[6]),
        self.var_email.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_radio_reg.set(data[9])

    #=========================update function
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_semester.get()==" Select Semester" or self.var_session.get()=="Select Year":
            return messagebox.showerror("Field Not Filled", "Please fill all fields before saving",parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="9504", database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Department=%s,Session=%s,Roll=%s,Name=%s,Phone=%s,Semester=%s,Email=%s,DateOfBirth=%s,Radiobtn=%s where Registration=%s",(

                        self.var_dept.get(),
                        self.var_session.get(),
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_phone.get(),
                        self.var_semester.get(),
                        self.var_email.get(),
                        self.var_dob.get(),
                        self.var_radio_reg.get(),
                        self.var_reg.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To {str(es)}",parent=self.root)

    #=====================delete function
    def delete_data(self):
        if self.var_reg.get() == "":
            messagebox.showerror("Error","Registration Number Required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete","Are you sure you want to delete the data?",parent=self.root)
                if delete >0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="9504", database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE Registration=%s"
                    val=(self.var_reg.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete Success","Deleted Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To {str(es)}",parent=self.root)

    #=================reset function
    def reset_data(self):
        self.var_reg.set(""),
        self.var_dept.set("Select Department"),
        self.var_session.set("Select Session"),
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_phone.set(""),
        self.var_semester.set("Select Semester"),
        self.var_email.set(""),
        self.var_dob.set(""),
        self.var_radio_reg.set("")


if __name__ == "__main__":
    root = Tk()
    app = Student_Detail(root)
    root.mainloop()

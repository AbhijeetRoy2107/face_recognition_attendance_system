from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from PIL import Image,ImageTk
from student import Student_Detail
import os
from train import Train
from face_recognition import Face_Recognition


class Face_Detection_Attendance_System():
    def __init__(self,root):
        self.root = root
        self.root.title("Face Recognition Attendance System")
        self.root.geometry("1080x720")
        self.root.resizable(width=False, height=False)

        bg_img = Image.open("assets/images/BSonoma_Mac.png")
        bg_img = bg_img.resize((1080,720))
        self.photoimg = ImageTk.PhotoImage(bg_img)

        bg_img_label = Label(self.root,image=self.photoimg)
        bg_img_label.place(x=0,y=0,width=1080,height=720)


        title_label = Label(bg_img_label,
                            text="FACE RECOGNITION ATTENDANCE SYSTEM",
                            font=("arial",20,"bold"),fg="black",bg="white")
        title_label.place(x=0,y=0,width=1080,height=80)

        #=====================main buttons====================

        #Student details btn
        b1 = Button(bg_img_label,text="Studemt Details",command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=70)

        #See Captured Photos button
        b2 = Button(bg_img_label, text="See Captured Photos", cursor="hand2",command=self.open_img)
        b2.place(x=100, y=200, width=220, height=70)

        #Train Images Button
        b3 = Button(bg_img_label, text="Train Images", cursor="hand2",command=self.train_data)
        b3.place(x=400, y=200, width=220, height=70)

        # Recognise Images Button
        b4 = Button(bg_img_label, text="Recognise Images", cursor="hand2", command=self.face_data)
        b4.place(x=400, y=400, width=220, height=70)


    #===================button functions=================
    def open_img(self):
        os.startfile(r"assets\training_images")

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student_Detail(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

if __name__ == "__main__":
    root = Tk()
    app = Face_Detection_Attendance_System(root)
    root.mainloop()
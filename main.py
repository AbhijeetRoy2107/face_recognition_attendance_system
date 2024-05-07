from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from PIL import Image,ImageTk
from student import Student_Detail

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

        #student button
        b1 = Button(bg_img_label,text="Studemt Details",command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=70)

        b2 = Button(bg_img_label, text="Button 2", cursor="hand2")
        b2.place(x=100, y=200, width=220, height=70)


    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student_Detail(self.new_window)

if __name__ == "__main__":
    root = Tk()
    app = Face_Detection_Attendance_System(root)
    root.mainloop()
from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import cv2


class Attendance():
    def __init__(self,root):
        self.root = root
        self.root.title("VIEW ATTENDANCE")
        self.root.geometry("1080x720")
        self.root.resizable(FALSE,FALSE)

        title_label = Label(self.root,
                        text="VIEW ATTENDANCE",
                        font=("arial", 20, "bold"),
                        fg="white", bg="lightblue")
        title_label.place(x=0, y=0, width=1080, height=70)


if __name__ == "__main__":
    root = Tk()
    app = Attendance(root)
    root.mainloop()
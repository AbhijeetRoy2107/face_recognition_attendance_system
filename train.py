from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import cv2
import os
import numpy as np

#====================== LBPH Algorithm Used for Training ==========================#
class Train():
    def __init__(self,root):
        self.root = root
        self.root.title("TRAIN IMAGES")
        self.root.geometry("1080x720")
        self.root.resizable(FALSE,FALSE)

        title_label = Label(self.root,
                            text="Train Images",
                            font=("arial", 20, "bold"),
                            fg="darkblue", bg="lightblue")
        title_label.place(x=0, y=0, width=1080, height=50)

        train_btn = Button(self.root,
                          text="Train",
                          width=21,
                          font=("arial", 15, "bold"),
                          bg="blue",
                          fg="white",
                           command=self.train_classifier)
        train_btn.place(x=20, y=80, width=200, height=50)

    def train_classifier(self):
        data_dir = (r"assets\training_images")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")      #grayscale image
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)

        #================== Train the classifier ===============#
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("trained_model.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Completed")





if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()
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
from pygments.formatters import img
from time import strftime
from datetime import datetime

#=============credentials===============#
my_sql_host = "localhost"
my_sql_user = "root"
my_sql_password = "9504"
my_sql_database = "face_recognition"


class Face_Recognition():
    def __init__(self,root):
        self.root = root
        self.root.title("RECOGNISE IMAGES")
        self.root.geometry("1080x720")
        self.root.resizable(FALSE,FALSE)

        title_label = Label(self.root,
                            text="Recognise Images",
                            font=("arial", 20, "bold"),
                            fg="darkblue", bg="lightblue")
        title_label.place(x=0, y=0, width=1080, height=50)

        face_recognise_btn = Button(self.root,
                           text="Recognise Face",
                           width=21,
                           font=("arial", 15, "bold"),
                           bg="blue",
                           fg="white",
                           command=self.face_recog
                           )
        face_recognise_btn.place(x=20, y=80, width=200, height=50)
    #========================= Attendance ========================#
    def mark_attendance(self,reg,n,r,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if((reg not in name_list) and (n not in name_list) and (r not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{reg},{r},{n},{d},{dtString},{d1},Present")



    #======================== Face Recogniser ==================#
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host=my_sql_host,user=my_sql_user,password=my_sql_password,database=my_sql_database)
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Registration="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Roll from student where Registration="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Department from student where Registration="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select Registration from student where Registration=" + str(id))
                reg = my_cursor.fetchone()
                reg = "+".join(reg)

                if confidence > 77:
                    cv2.putText(img, f"Registration:{reg}",
                                (x, y - 82),
                                cv2.FONT_HERSHEY_COMPLEX,
                                0.8, (255, 255, 255),
                                3)
                    cv2.putText(img,f"Roll:{r}",
                                (x,y-55),
                                 cv2.FONT_HERSHEY_COMPLEX,
                                0.8,(255,255,255),
                                3)
                    cv2.putText(img, f"Name:{n}",
                                (x, y - 30),
                                 cv2.FONT_HERSHEY_COMPLEX,
                                0.8, (255, 255, 255),
                                3)
                    cv2.putText(img, f"Department:{d}",
                                (x, y - 5),
                                 cv2.FONT_HERSHEY_COMPLEX,
                                0.8, (255, 255, 255),
                                3)
                    self.mark_attendance(reg,n,r,d)
                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face",
                                (x, y - 5),
                                cv2.FONT_HERSHEY_COMPLEX,
                                0.8, (255, 255, 255),
                                3)

                coord = [x,y,w,y]
            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("trained_model.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Face",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition(root)
    root.mainloop()
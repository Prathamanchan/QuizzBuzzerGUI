
from Tkinter import *
import tkFont
import serial
import os

root=Tk()
root.title("Quiz Buzzer")

logo=PhotoImage(file="qbuzz.png")

frame=Frame(root,bg="white")
frame.pack()

midframe=Frame(root,bg="white")
midframe.pack(fill=BOTH,expand=1)

bottomframe=Frame(root,bg="blue")
bottomframe.pack(side=BOTTOM,fill=BOTH,expand=1)

tclass=[]

label_00=Label(midframe,width="20",height="3",bg="red",text="RED",fg="white",font="-weight bold")
label_01=Label(midframe,width="20",height="3",bg="white",text=" ",fg="black",font="-weight bold")
label_10=Label(midframe,width="20",height="3",bg="blue",text="BLUE",fg="white",font="-weight bold")
label_11=Label(midframe,width="20",height="3",bg="white",text=" ",fg="black",font="-weight bold")
label_20=Label(midframe,width="20",height="3",bg="green",text="GREEN",fg="white",font="-weight bold")
label_21=Label(midframe,width="20",height="3",bg="white",text=" ",fg="black",font="-weight bold")
label_30=Label(midframe,width="20",height="3",bg="orange",text="ORANGE",fg="white",font="-weight bold")
label_31=Label(midframe,width="20",height="3",bg="white",text=" ",fg="black",font="-weight bold")
label_40=Label(midframe,width="20",height="3",bg="yellow",text="YELLOW",fg="white",font="-weight bold")
label_41=Label(midframe,width="20",height="3",bg="white",text=" ",fg="black",font="-weight bold")
tclass.append(label_00)

tclass[0].grid(row=0,column=0)
label_01.grid(row=0,column=1)
label_10.grid(row=1,column=0)
label_11.grid(row=1,column=1)
label_20.grid(row=2,column=0)
label_21.grid(row=2,column=1)
label_30.grid(row=3,column=0)
label_31.grid(row=3,column=1)
label_40.grid(row=4,column=0)
label_41.grid(row=4,column=1)

start=Button(bottomframe,text="Display Results",font="-weight bold")
start.pack(fill=BOTH,expand=1)
#start.grid(row=0,column=0,rowspan=2,columnspan=3)

stop=Button(bottomframe,text="Clear",font="-weight bold")
stop.pack(fill=BOTH,expand=1)
#stop.grid(row=0,column=6,rowspan=2,columnspan=3)

w=Label(frame,image=logo)
w.pack()
root.geometry("450x480")
root.mainloop()


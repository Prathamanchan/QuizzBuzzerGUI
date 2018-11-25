#Never give Up


from Tkinter import *
import tkFont
import serial
import os

os.system("sudo chmod a+rw /dev/ttyUSB0")
os.system("python filewriteserial.py &")
root=Tk()
root.title("Quiz Buzzer")


#Initialise
red=0
green=0
orange=0
yellow=0
blue=0
order=[]
lst=[]
tclassn=[]
tclasstime=[]
color=[]


def arrange(order,lst,color):

	for i in range(0,5):
		for j in range(0,4):
			if(lst[i]<lst[j]):
				temp=lst[i]
				lst[i]=lst[j]
				lst[j]=temp

	for i in range(0,5):
		if red==lst[i]:
			order.append("RED")
			color.append("red")

		if blue==lst[i]:
                	order.append("BLUE")
			color.append("blue")

		if green==lst[i]:
                	order.append("GREEN")
			color.append("green")

		if orange==lst[i]:
                	order.append("ORANGE")
			color.append("orange")

		if yellow==lst[i]:
                	order.append("YELLOW")
			color.append("yellow")
	return order,lst,color

def readFile():
	f=open('actualfile.txt','r')
	linelist=f.readlines()
	count=-1
	Int=[]
	Garbage=[]
	Vat=[]
	global red,green,orange,yellow,blue
	global order,lst,tclassn,color,tclasstime
	
	for e in linelist:
		Int.append(1)
		Garbage.append(1)
		Vat.append(1)
		count=count+1

		Garbage[count] =map(float, [float(i) for i in e.split() if i.replace('.','',1).isdigit()])
		if len(Garbage[count]) != 0:  #Filter Empty Lines
                	Int[count]=Garbage[count].pop()
		print Int
		Vat[count] = [i for i in e.split() if i.isalpha() and i!='ms']  #Split Each statement
 		team=Vat[count]
		print Vat[count]

	if any("RED" in s for s in Vat):
		index=Vat.index(['RED'])
		red=Int[index]
		print(red)

	if any("YELLOW" in s for s in Vat):
        	index=Vat.index(['YELLOW'])
        	yellow=Int[index]
        	print(yellow)

	if any("GREEN" in s for s in Vat):
        	index=Vat.index(['GREEN'])
        	green=Int[index]
        	print(green)

	if any("ORANGE" in s for s in Vat):
        	index=Vat.index(['ORANGE'])
        	orange=Int[index]
        	print(orange)

	if any("BLUE" in s for s in Vat):
                index=Vat.index(['BLUE'])
                blue=Int[index]
                print(blue)
	
	
	lst=[red,blue,green,orange,yellow]
	order,lst,color=arrange(order,lst,color)
	print order
	str1="RED    "+str(red)+"ms \n"+"YELLOW  "+str(yellow)+"ms \n"+"GREEN  "+str(green)+"ms \n"+"ORANGE "+str(orange)+"ms \n"
	
	for i in range(0,5):
		tclasstime[i].config(text=str(lst[i])+" ms")
		tclassn[i].config(text=order[i])
		tclassn[i].config(bg=color[i])
	color=[]
	order=[]
	lst=[]

	f.close()

def clear():
	label_01.config(text=" ")
        label_11.config(text=" ")
        label_21.config(text=" ")
        label_31.config(text=" ")
        label_41.config(text=" ") 
	os.system("rm testfile.txt")
	os.system("python filewriteserial.py &")
	color=[]
	order=[]
	lst=[]
	print "clean"
	

logo=PhotoImage(file="qbuzz.png")

frame=Frame(root,bg="white")
frame.pack()

midframe=Frame(root,bg="white")
midframe.pack(fill=BOTH,expand=1)

bottomframe=Frame(root,bg="blue")
bottomframe.pack(side=BOTTOM,fill=BOTH,expand=1)

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

tclassn.append(label_00)
tclassn.extend([label_10,label_20,label_30,label_40])
tclasstime.append(label_01)
tclasstime.extend([label_11,label_21,label_31,label_41])


label_00.grid(row=0,column=0)
label_01.grid(row=0,column=1)
label_10.grid(row=1,column=0)
label_11.grid(row=1,column=1)
label_20.grid(row=2,column=0)
label_21.grid(row=2,column=1)
label_30.grid(row=3,column=0)
label_31.grid(row=3,column=1)
label_40.grid(row=4,column=0)
label_41.grid(row=4,column=1)

start=Button(bottomframe,text="Display Results",command=readFile,font="-weight bold")
start.pack(fill=BOTH,expand=1)
#start.grid(row=0,column=0,rowspan=2,columnspan=3)

stop=Button(bottomframe,text="Clear",command=clear,font="-weight bold")
stop.pack(fill=BOTH,expand=1)
#stop.grid(row=0,column=6,rowspan=2,columnspan=3)

w=Label(frame,image=logo)
w.pack()
root.geometry("450x480")
root.mainloop()


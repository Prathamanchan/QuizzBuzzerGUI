import serial
import os
import tkMessageBox

os.system("sudo chmod a+rw /dev/ttyUSB0")
os.system("touch testfile.txt")
file=open("testfile.txt","w")
file.close()
print("All FIne")

while True:

        ser = serial.Serial('/dev/ttyUSB0')
        ser_bytes = ser.readline()
        print(ser_bytes)

	file = open("testfile.txt","a") 
	file.write(ser_bytes)
	file.close() 


	#print("Error Could not read from port")
		

from video import processVideo1
from video2 import processVideo2
import numpy as np
import cv2
import math
import tensorflow as tensorflow
from keras.models import load_model
from firebase import firebase
import tkinter as tk
from tkinter import *

#connecting to firebase
firebase = firebase.FirebaseApplication("enter your firebase link")
#defining categories
Categories = ["Car", "not car"]
#loading model
model = load_model('cnn.h5')

#GUI chooser
locations = []
r = firebase.get('/',None)
for i in r:
	locations.append(i)
#print(locations)

#gui video chooser
root = Tk()
root.title("Select Location")
 
# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)
 
# Create a Tkinter variable
tkvar = StringVar(root)
tkvar.set(locations[0])
popupMenu = OptionMenu(mainframe, tkvar, *locations)
Label(mainframe, text="Choose a location").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

Button(root,text="Submit",command=root.destroy,bg="Lightgrey", fg="black",font=("Times New Roman", 14)).pack()

root.mainloop()
l = tkvar.get()

#main code
flag = 0
if l == "Location1":
	video = cv2.VideoCapture('location1.mp4')
elif l == "Location2":
	flag = 1
	video = cv2.VideoCapture('location2.mp4')
else:
	flag = 2

if flag != 2:
	i = 0
	frameRate = video.get(5) #frame rate
	while (video.isOpened()):
		frameId = video.get(1) #current frame number
		ret, frame = video.read()
		if (frameId % math.floor(frameRate) == 0):
			frame = cv2.resize(frame, (400,400))
			cv2.imshow('frame',frame)
			print("--------------------")
			print("Iteration: "+ str(i))
			print("--------------------")
			if flag == 0:
				processVideo1(frame,model,firebase,Categories)
			else:
				processVideo2(frame,model,firebase,Categories)
			i += 1
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		if ret == False :
			break
		
	video.release()
	cv2.destroyAllWindows()
else:
	print("Video not found!")
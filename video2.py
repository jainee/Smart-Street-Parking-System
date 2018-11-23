import numpy as np
import cv2
import math
import tensorflow as tensorflow
from keras.models import load_model
from firebase import firebase
from SelectSlot import four_point_transform,prepare

def processVideo2(imageo, model,firebase,Categories):
	imageo = cv2.resize(imageo,(1920,1080))
	coords1 = "[(30,360),(30,990),(370,990),(370,360)]"
	coords2 = "[(400,360),(400,1000),(725,1000),(725,360)]"
	coords3 = "[(770,370),(770,1015),(1095,1015),(1095,370)]"
	coords4 = "[(1130,370),(1130,1055),(1485,1055),(1485,370)]"
	coords5 = "[(1515,380),(1515,1050),(1885,1050),(1885,380)]"
	coords = [coords1,coords2,coords3,coords4,coords5]

	#read image
	#imageo = cv2.imread('test_01.jpg')

	pts = []
	for i in coords:
		pts.append(np.array(eval(i),dtype="float32"))
	  
	#save image of slots  
	x = 1
	for i in pts:
	  warped = four_point_transform(imageo, i)
	  cv2.imwrite("slot.jpg" , warped)
	  prediction = model.predict([prepare("slot.jpg")])
	  #print(prediction)
	  if prediction [0][1] > -1184435 and prediction [0][0] < 1765256.8:
	  	firebase.put('/Location2',"Slot "+str(x),False)
	  	print("Slot "+str(x)+" status: "+Categories[1])
	  	#print(Categories[1])
	  else:
	  	firebase.put('/Location2',"Slot "+str(x),True)
	  	print("Slot "+str(x)+" status: "+Categories[0])
	  	#print(Categories[0])
	  x += 1


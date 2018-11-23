import numpy as np
import cv2
import math
import tensorflow as tensorflow
from keras.models import load_model
from SelectSlot import four_point_transform, prepare

def processVideo1(imageo, model,firebase,Categories):
	imageo = cv2.resize(imageo,(1920,1080))
	#coordinates of slots in video
	coords1 = "[(130,217),(130,1027),(551,1027),(551,217)]"
	coords2 = "[(600,217),(600,1027),(963,1027),(963,217)]"
	coords3 = "[(980,217),(980,1027),(1395,1027),(1395,217)]"
	coords4 = "[(1395,217),(1395,1027),(1841,1027),(1841,217)]"

	coords = [coords1,coords2,coords3,coords4]

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
	  	firebase.put('/Location1',"Slot "+str(x),False)
	  	print("Slot "+str(x)+" status: "+Categories[1])
	  	#print(Categories[1])
	  else:
	  	firebase.put('/Location1',"Slot "+str(x),True)
	  	print("Slot "+str(x)+" status: "+Categories[0])
	  	#print(Categories[0])
	  x += 1
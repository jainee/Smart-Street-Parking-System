import numpy as np
import cv2
import tensorflow as tensorflow
from keras.models import load_model
from firebase import firebase

Categories = ["Car", "not car"]

#connecting to firebase
firebase = firebase.FirebaseApplication("https://project-14a65.firebaseio.com")

def order_points(pts):
	# initialzie a list of coordinates that will be ordered
	# such that the first entry in the list is the top-left,
	# the second entry is the top-right, the third is the
	# bottom-right, and the fourth is the bottom-left
	rect = np.zeros((4, 2), dtype = "float32")

	# the top-left point will have the smallest sum, whereas
	# the bottom-right point will have the largest sum
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]

	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
	# whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]

	# return the ordered coordinates
	return rect

def four_point_transform(image, pts):
	# obtain a consistent order of the points and unpack them
	# individually
	rect = order_points(pts)
	(tl, tr, br, bl) = rect

	# compute the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left
	# x-coordiates or the top-right and top-left x-coordinates
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))

	# compute the height of the new image, which will be the
	# maximum distance between the top-right and bottom-right
	# y-coordinates or the top-left and bottom-left y-coordinates
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))

	# now that we have the dimensions of the new image, construct
	# the set of destination points to obtain a "birds eye view",
	# (i.e. top-down view) of the image, again specifying points
	# in the top-left, top-right, bottom-right, and bottom-left
	# order
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")

	# compute the perspective transform matrix and then apply it
	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

	# return the warped image
	return warped


def prepare(filepath):
	img_size = 400
	img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
	img_resize = cv2.resize(img, (img_size,img_size))
	return img_resize.reshape(-1, 1, img_size, img_size)

model = load_model('cnn.h5')

# Define Co-ordinates of slots
coords1 = "[(15,17),(15,240),(152,240),(152,17)]"
coords2 = "[(15,251),(15,469),(151,469),(151,251)]"
coords = [coords1,coords2]

#read image
imageo = cv2.imread('test.jpg')
#kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
#imageo = cv2.filter2D(imageo, -1, kernel)
imageo = cv2.resize(imageo, (163,473))
pts = []
for i in coords:
	pts.append(np.array(eval(i),dtype="float32"))
  
#save image of slots  
x = 1
for i in pts:
  warped = four_point_transform(imageo, i)
  cv2.imwrite("slot"+str(x)+".jpg" , warped)
  prediction = model.predict([prepare("slot"+str(x)+".jpg")])
  #print(prediction)
  if prediction [0][1] < -999466.56 and prediction [0][0] > 1592352:
    print(Categories[1])
    firebase.put('/Location3',"Slot "+str(x),False)
  else:
    print(Categories[0])
    firebase.put('/Location3',"Slot "+str(x),True)
  x += 1
cv2.imshow('image',imageo)
cv2.waitKey(10000)
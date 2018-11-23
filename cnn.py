import os,cv2
import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

from keras import backend as K
from PIL import Image
from numpy import *
import keras
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD,RMSprop,adam
from keras.callbacks import ReduceLROnPlateau

from keras.preprocessing.image import ImageDataGenerator



path1 = "car_dataset"
path2 = "Grey"
img_rows = 400
img_cols = 400

listning = os.listdir(path1)
num_samp = len(listning)
print(num_samp)

for file in listning:
	im = Image.open(path1+'\\'+file)
	img = im.resize((img_rows,img_cols))
	gray = img.convert('L')
	gray.save(path2+'\\'+file,'JPEG')

imlist = os.listdir(path2)
imatrix = array([array(Image.open(path2+'\\'+im2)).flatten() for im2 in imlist],'f')
label = np.ones((num_samp,),dtype = int)
label[0:113] = 0

data, label = shuffle(imatrix,label,random_state = 5)
train_data = [data,label]





batch_size = 15
nb_classes = 2
nb_epoch = 5


(X,Y) = (train_data[0],train_data[1])

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 10)

X_train = X_train.reshape(X_train.shape[0],1,img_rows,img_cols)
X_test = X_test.reshape(X_test.shape[0],1,img_rows,img_cols)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train /= 255
X_test /= 255

Y_train = np_utils.to_categorical(Y_train,nb_classes)
Y_test = np_utils.to_categorical(Y_test,nb_classes)


keras.backend.set_image_dim_ordering('th')

model = Sequential()

# Layer 1
model.add(Convolution2D(16, 3, 3, input_shape = (1, img_rows, img_cols),border_mode='same',subsample=(1,1)))
model.add(LeakyReLU(alpha=0.1))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Layer 2
model.add(Convolution2D(32,3,3 ,border_mode='same'))
model.add(LeakyReLU(alpha=0.1))
model.add(MaxPooling2D(pool_size=(2, 2),border_mode='valid'))

# Layer 3
model.add(Convolution2D(64,3,3 ,border_mode='same'))
model.add(LeakyReLU(alpha=0.1))
model.add(MaxPooling2D(pool_size=(2, 2),border_mode='valid'))

# Layer 4
model.add(Convolution2D(128,3,3 ,border_mode='same'))
model.add(LeakyReLU(alpha=0.1))
model.add(MaxPooling2D(pool_size=(2, 2),border_mode='valid'))

# Layer 5
model.add(Convolution2D(256,3,3 ,border_mode='same'))
model.add(LeakyReLU(alpha=0.1))
model.add(MaxPooling2D(pool_size=(2, 2),border_mode='valid'))

# Layer 6
model.add(Convolution2D(512,3,3 ,border_mode='same'))
model.add(LeakyReLU(alpha=0.1))
model.add(MaxPooling2D(pool_size=(2, 2),border_mode='valid'))

# Layer 7
model.add(Convolution2D(1024,3,3 ,border_mode='same'))
model.add(LeakyReLU(alpha=0.1))

# Layer 8
model.add(Convolution2D(1024,3,3 ,border_mode='same'))
model.add(LeakyReLU(alpha=0.1))

# Layer 9
model.add(Convolution2D(1024,3,3 ,border_mode='same'))
model.add(LeakyReLU(alpha=0.1))

model.add(Flatten())

# Layer 10
model.add(Dense(256))

# Layer 11
model.add(Dense(4096))
model.add(LeakyReLU(alpha=0.1))
    
# Layer 12
model.add(Dense(1470))

model.add(Dense(2))
  
model.compile(loss='categorical_crossentropy', optimizer='rmsprop',metrics=["accuracy"])
  
model.summary()
model.get_config()
model.layers[0].get_config()
model.layers[0].input_shape			
model.layers[0].output_shape			
model.layers[0].get_weights()
np.shape(model.layers[0].get_weights()[0])
model.layers[0].trainable

print(Y_train)
print(Y_test)

#%%
# Training
hist = model.fit(X_train, Y_train, batch_size=batch_size, epochs=nb_epoch, verbose=1, validation_data=(X_test, Y_test))
model.save('cnn_ss.h5')
# Smart-Street-Parking-System
System detects available and non available slots and updates status to the android application accordingly.





I used Convolutional Nueral Network to develop this system.
First of all you have to train a model which is able to detect car. I trained this model using 122 images. Car_dataset contains them all.
cnn.py contains code to train model after running that code you will be able to find .h5 file. Trained model has near equal to 1 accuracy. 

![screenshot 155](https://user-images.githubusercontent.com/43346518/48930687-3d35f500-ef18-11e8-91d5-9a9284f54bbc.png)



I have attached android application code. Configure firebase, use realtime database and construct a tree shown below in firebase and connect firebase with android application.
![screenshot 171](https://user-images.githubusercontent.com/43346518/48930536-29d65a00-ef17-11e8-9a8e-84a3e922b4a6.png)
## Application Screen shots
![image](https://user-images.githubusercontent.com/43346518/48930792-d36a1b00-ef18-11e8-8148-180d610e908d.png)
![image](https://user-images.githubusercontent.com/43346518/48930810-e0870a00-ef18-11e8-93a7-7c5d9512a3b6.png)

After selecting location

![image](https://user-images.githubusercontent.com/43346518/48930845-14622f80-ef19-11e8-94d8-c2e5bb85949a.png)



There are two videos i used. Run Main.py file, choose video to run from gui.
![screenshot 172](https://user-images.githubusercontent.com/43346518/48930606-acf7b000-ef17-11e8-9859-27f4a32f6991.png)

## Video frame and adroid application status
![image](https://user-images.githubusercontent.com/43346518/48930726-69517600-ef18-11e8-8a1b-4c38ba29c824.png)
![image](https://user-images.githubusercontent.com/43346518/48930728-6e162a00-ef18-11e8-90cd-e65f63b8fd48.png)


So, all changes will be reflected to android application.

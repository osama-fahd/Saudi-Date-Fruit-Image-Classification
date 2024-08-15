#Fruit Types
There are many date fruit types in Saudi Arabia, but the dataset consists of data fruit images corresponding to 9 types of fruit dates as the
following: Ajwa, Galaxy, Medjool, Meneifi, NabtatAli, Rutab, Shaishe, Sokari, Sugaey.
![image](https://github.com/user-attachments/assets/a95b9886-d323-4edd-b2ff-7ff45a2271a4)

#The Used Model
The used model to tackle this problem is Convolutional Neural Network (CNN). 

#THE PLATFORM 
	I used google colab notebook  
 
#SOME DETAIL OF SOME STEPS
 	First, I imported some libraries from TensorFlow library. And then I unzipped the file and uploaded it in google colab. And after that I did some modifications, and I split it into 80% training and 20% validation. 
DATA PREPROCESSING AND AUGMENTATION DETAILS 
	I normalized the pixel values to be between [0, 1], using tf.keras.layers.Rescaling.
	I used Data Augmentation to reduce the risk of overfitting.
o	I used ImageDataGenerator from Keras to apply data augmentation.


#DETAILS OF MY CNN
1.	Rescaling layer: This layer normalizes the pixel values of the input images to the range [0, 1].
2.	Data augmentation layer: This layer applies random transformations to the input images, such as horizontal and vertical flips and rotations.
3.	Conv2D layer (first): This is the first convolutional layer with 8 filters, each with a kernel size of 3x3. It uses the ReLU activation function and 'same' padding.
4.	MaxPooling2D layer (first): This is the first max pooling layer with a default pool size of 2x2.
5.	Conv2D layer (second): This is the second convolutional layer with 16 filters, each with a kernel size of 3x3. It also uses the ReLU activation function.
6.	MaxPooling2D layer (second): This is the second max pooling layer, also with a default pool size of 2x2.
7.	Dropout layer (first): This layer randomly sets a fraction (20%) ,which helps prevent overfitting.
8.	Conv2D layer (third): This is the third convolutional layer with 32 filters, each with a kernel size of 3x3. It uses the ReLU activation function.
9.	MaxPooling2D layer (third): This is the third max pooling layer, also with a default pool size of 2x2.
10.	 Dropout layer (second): This layer randomly sets a fraction (20%).
11.	Conv2D layer (fourth): This is the fourth convolutional layer with 64 filters, each with a kernel size of 3x3. It uses the ReLU activation function.
12.	MaxPooling2D layer (fourth): This is the fourth max pooling layer, also with a default pool size of 2x2.
13.	Dropout layer (third).
14.	Flatten layer.
15.	Dense layer (first): This is the first fully connected layer with 256 units and a ReLU activation function.
16.	Dropout layer (fourth).
17.	Dense layer (second): This is the output layer with 9 units and a softmax activation function.

#THE USED OPTIMIZER AND NUMBER OF EPOCHS
I used RMSprop (Root Mean Square Propagation), and I put the learning rate = 0.001.
I used 35 epochs.

#PLOTS OF LOSS AND ACCURACY 
 
#DATASET SAMPLES COUNT PER LABEL CHARTS 
 
#CLASSIFICATION REPORT AND CONFUSION MATRIX 
 
#EVALUATION RESULT

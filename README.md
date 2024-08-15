# Fruit Types
There are many date fruit types in Saudi Arabia. Still, the dataset consists of data fruit images corresponding to 9 types of fruit dates the
following: Ajwa, Galaxy, Medjool, Meneifi, NabtatAli, Rutab, Shaishe, Sokari, and Sugaey.
![image](https://github.com/user-attachments/assets/a95b9886-d323-4edd-b2ff-7ff45a2271a4)

# The Used Model
The model used to tackle this problem is the Convolutional Neural Network (CNN). 

# THE PLATFORM 
I used Google Colab Notebook.  
 
# SOME DETAILS OF SOME STEPS
First, I imported some libraries from the TensorFlow library. Then I unzipped the file and uploaded it to Google Colab. After that, I split the Training Data into 80% training and 20% validation. 

# DETAILS OF MY CNN
1.	Conv2D layer: This is the third convolutional layer with 32 filters, each with a kernel size of 3x3. It uses the ReLU activation function.
2.	MaxPooling2D layer (third): This is the third max pooling layer, also with a default pool size of 2x2.
3.	Conv2D layer: This is the fourth convolutional layer with 64 filters, each with a kernel size of 3x3. It uses the ReLU activation function.
4.	MaxPooling2D layer: This is the fourth max pooling layer, also with a default pool size of 2x2.
5.	Dropout layer: This layer randomly sets a fraction (20%).
6.	Conv2D layer: This is the fourth convolutional layer with 128 filters, each with a kernel size of 3x3. It uses the ReLU activation function.
7.	MaxPooling2D layer: This is the fourth max pooling layer, also with a default pool size of 2x2.
8.	Dropout layer.
9.	Flatten layer.
10.	Dense layer: This is the first fully connected layer with 256 units and a ReLU activation function.
11.	Dropout layer: with a fraction (50%).
12.	Dense layer: This is the output layer with 9 units and a softmax activation function.


# THE USED OPTIMIZER AND NUMBER OF EPOCHS
I used ADAM, and I put the learning rate = 0.001.
I used 15 epochs.

# PLOTS OF LOSS AND ACCURACY 
 ![image](https://github.com/user-attachments/assets/1ddb8185-00da-4d2c-aa8a-56d5d1c9afbd)

# DATASET SAMPLES COUNT PER LABEL CHARTS 
 ![image](https://github.com/user-attachments/assets/81251626-512a-40d4-8f2f-d6151ab3c30e)
![image](https://github.com/user-attachments/assets/97f1961e-3ba0-437d-a29c-a36726002ea5)

# CLASSIFICATION REPORT AND CONFUSION MATRIX 
 ![image](https://github.com/user-attachments/assets/2632ed30-e7d9-4a07-842f-830320722bca)
![image](https://github.com/user-attachments/assets/a4f12a62-54f0-46d6-b82f-d6e1ac55ad33)

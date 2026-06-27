import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense
import matplotlib.pyplot as plt
import numpy as np

# Load MNIST Dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("Training Images:", x_train.shape)
print("Testing Images:", x_test.shape)

# Normalize
x_train = x_train / 255.0
x_test = x_test / 255.0

# Reshape
x_train = x_train.reshape(-1,28,28,1)
x_test = x_test.reshape(-1,28,28,1)

print("New Shape:", x_train.shape)

# Build CNN Model
model = Sequential()

model.add(Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)))
model.add(MaxPooling2D((2,2)))

model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D((2,2)))

model.add(Flatten())

model.add(Dense(128,activation='relu'))

model.add(Dense(10,activation='softmax'))

model.summary()

# Compile
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train
history = model.fit(
    x_train,
    y_train,
    epochs=5,
    validation_split=0.2
)

# Test
loss,accuracy=model.evaluate(x_test,y_test)

print("Accuracy :",accuracy*100)

# Predict Sample
prediction=model.predict(x_test)

print("Predicted Digit :",np.argmax(prediction[0]))
print("Actual Digit :",y_test[0])

# Display Image
plt.imshow(x_test[0].reshape(28,28),cmap="gray")
plt.title("Predicted : {}".format(np.argmax(prediction[0])))
plt.show()

# Save Model
model.save("model.h5")

print("Model Saved Successfully")
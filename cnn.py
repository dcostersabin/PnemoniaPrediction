import os
import numpy as np
# import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.layers import Flatten
from keras.models import load_model

BASE = os.getcwd()
MODEL_DIR = BASE + '/Models/myModel'
PREDICTION_IMAGE = ''
TRAINING_DATA = BASE + '/Dataset/train/'
TESTING_DATA = BASE + '/Dataset/test/'
VALIDATION_DATASET = BASE + '/val/'
EPOCH = 50


def get_steps_per_epoches():
    TRAINING_DATA_NO = 0
    TESTING_DATA_NO = 0
    for dirs in os.listdir(TRAINING_DATA):
        no_of_files = len(os.listdir(TRAINING_DATA + dirs))
        TRAINING_DATA_NO += no_of_files

    for dirs in os.listdir(TESTING_DATA):
        no_of_files = len(os.listdir(TESTING_DATA + dirs))
        TESTING_DATA_NO += no_of_files

    return [TRAINING_DATA_NO, TESTING_DATA_NO]


def runModel():
    # making directory for the model
    if os.path.exists(BASE + '/Models/'):
        os.remove(BASE + '/Models/')
    os.makedirs(BASE + '/Models/')
    # initializing the neural network
    classifier = Sequential()
    # adding a convolution layer to the neural network
    classifier.add(Convolution2D(64, (3, 3), input_shape=(150, 150, 3), activation='relu'))
    # adding pooling layer using maxpooling
    classifier.add(MaxPooling2D(pool_size=(2, 2)))
    # adding another convolution layer
    classifier.add(Convolution2D(64, (3, 3), input_shape=(150, 150, 3), activation='relu'))
    # adding another max pooling layer for conv2D
    classifier.add(MaxPooling2D(pool_size=(2, 2)))
    # adding another layer of convolution layer
    classifier.add(Convolution2D(64, (3, 3), input_shape=(150, 150, 3), activation='relu'))
    # adding another layer of max pooling
    classifier.add(MaxPooling2D(pool_size=(2, 2)))
    # adding last layer of convolutional 2D layer
    classifier.add(Convolution2D(64, (3, 3), input_shape=(3, 3), activation='relu'))
    # adding another pooling layer
    classifier.add(MaxPooling2D(pool_size=(2, 2)))
    # adding flattening layer for giving inputs to the neural network
    classifier.add(Flatten())
    # adding an extra dense layer
    classifier.add(Dense(units=512, activation='relu'))
    # adding another layer of dense
    classifier.add(Dense(units=128, activation='relu'))
    # adding the final layer for the output
    classifier.add(Dense(units=1, activation='sigmoid', ))
    # compiling the neural network
    classifier.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
    # fitting the images using keras library
    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

    test_datagen = ImageDataGenerator(rescale=1. / 255)

    training_set = train_datagen.flow_from_directory(
        TRAINING_DATA,
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary')

    testing_set = test_datagen.flow_from_directory(
        TESTING_DATA,
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary')

    number = get_steps_per_epoches()

    classifier.fit_generator(
        training_set,
        steps_per_epoch=number[0],
        epochs=EPOCH,
        validation_data=testing_set,
        validation_steps=number[1])
    # saving the model in the folder after training
    classifier.save(MODEL_DIR)


def prediction():
    # loading the trained model
    classifier = load_model(MODEL_DIR)
    # transforming the given images
    test_image = image.load_img(PREDICTION_IMAGE)
    # converting the image to array
    test_image = image.img_to_array(test_image)
    # adding new dimension to the image array for processing
    test_image = np.expand_dims(test_image, axis=0)
    # predicting the given image
    result = classifier.predict(test_image)
    # displaying the output
    print("The Prediction Made is", result)


def main():
    # checking if the model already exists in the directory
    if os.path.exists(MODEL_DIR):
        print("Model Already Exists Do You Want To Train Model Again? Y/N")
        choice = input("Yes(Y) Or No")
        if choice == 'Y' or choice == 'y':
            runModel()

        print("Model Already Exists Performing The Prediction On The GivYen Image")
        prediction()
    else:
        print("No Trained Models Run Training")
        choice = input("Y/N")
        if choice == "Y":
            runModel()
        else:
            print("EXITING NOW........")


if __name__ == '__main__':
    main()

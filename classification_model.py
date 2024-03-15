import streamlit as st
import tensorflow as tf
import cv2 as cv
import numpy as np


class ClassificationModel():
    def __init__(self, path):
        self.model = tf.keras.models.load_model(path)
        self.labels_names = ['Accessories', 'Artifacts', 'Beauty', 'Fashion', 'Games', 'Home', 'Nutrition',
                             'Stationary']

    def predict(self, img):
        img = cv.resize(img, (256, 256))
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img = tf.cast(img, tf.float32) / 255.0
        img = tf.expand_dims(img, axis=0)
        prediction = self.model(img)
        probabilities = tf.nn.softmax(prediction)
        return self.labels_names[np.argmax(probabilities.numpy())]


if __name__ == '__main__':
    model_path = 'model_file.h5'
    model=ClassificationModel(model_path)
    img = cv.imread('sample1.webp')
    print(model.predict(img))
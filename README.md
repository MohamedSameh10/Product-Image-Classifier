# Product-Classifier

## Overview
This repository contains the implementation of a model designed for product classification.

## Data Collection
To gather data, screenshots of products from the Slash application were captured. Additionally, to increase the dataset, I employed data augmentation techniques. However, after experimentation, I decided to discard the augmented data to enhance model performance. Furthermore, web scraping was used to gather images representing various product categories available on Slash: Accessories, Artifacts, Nutrition, Beauty, Home, Fashion, Games, and Stationary.
[Used Data](https://drive.google.com/drive/folders/1DJIJ4A8ayHFxJ09wF62oXbVVroKz7AzW?usp=drive_link)

## Model Architecture
The model architecture is based on transfer learning, using the Inception neural network as a feature extractor. A classification layer was added on top of the pre-trained Inception model to tailor it to the specific classification task.

## Performance Metrics
The model exhibited strong performance metrics on the testing data, achieving an accuracy of 0.97 and a loss of 0.06. Additionally, the average F1-score on the testing data was 0.97, indicating robust performance across different classes.

## Web App
To enable the use of the model, I created a web app using Streamlit.
[Link](https://pr0ductimageclassifier.streamlit.app/)

## Demo Video
Below is a video demonstrating the model in action within the web app. This includes the model being tested on images sourced from Amazon for the first time. It's important to note that no images from the Amazon website were used during the training of the model.
[Link](https://drive.google.com/file/d/1q3MH4Oqhjx3J8q1-DkrjlgJABjuDyiuP/view?usp=sharing)

## -------
For optimal performance, the dataset could have been further refined and expanded. Unfortunately, due to time constraints caused by personal issues, I was unable to dedicate more time to gathering a larger number of images or refining the dataset. These additional steps could have made the model more knowledgeable.


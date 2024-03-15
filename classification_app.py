import streamlit as st
import cv2 as cv
import numpy as np
from classification_model import ClassificationModel

if __name__=='__main__':
    model_path = 'model_file.h5'
    model = ClassificationModel(model_path)

    st.title('Product Image Classifier')
    st.write('')

    file=st.file_uploader('',type=["jpg", "jpeg", "png"])

    if file is not None:
        image = cv.imdecode(np.fromstring(file.read(), np.uint8), cv.IMREAD_COLOR)

        prediction = model.predict(image)

        st.image(image, channels="BGR", caption="Uploaded Image.", use_column_width=True)

        st.write(prediction)
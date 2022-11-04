import numpy as np
import os
from tensorflow.keras.utils import img_to_array, load_img

from keras.applications.inception_v3 import (
    InceptionV3,
    decode_predictions,
    preprocess_input,
)

execution_path = os.getcwd()


def getFiles(path):
    image_list = []
    for file in os.listdir(path):
        if file.endswith(".jpg"):
            image_list.append(file)
    return image_list


model = InceptionV3(weights='imagenet')

for filename in getFiles(execution_path):
    original = load_img(filename, target_size=(299, 299))
    numpy_image = img_to_array(original)
    image_batch = np.expand_dims(numpy_image, axis=0)

    # model prediction
    processed_image = preprocess_input(image_batch.copy())
    predictions = model.predict(processed_image)
    label = decode_predictions(predictions)
    print(label)

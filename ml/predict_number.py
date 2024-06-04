import keras
from keras.utils import load_img, img_to_array
import numpy as np
import sys

def predict_array (model, img_array):
    output = model.predict(img_array)
    return np.argmax(output)

def predict (model_filename, image_filename):
    model = keras.models.load_model(model_filename)
    image = load_img(image_filename, color_mode="grayscale", target_size=(28, 28))
    arr = img_to_array(image)
    arr /= 255
    arr = arr.reshape(1, 28, 28, 1)
    return predict_array(model, arr)

if __name__ == "__main__":
    print(predict(sys.argv[1], sys.argv[2]))
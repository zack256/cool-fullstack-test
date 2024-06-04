import keras
from keras.utils import load_img, img_to_array
import numpy as np
import sys

def predict_number(image_filename):
    model = keras.models.load_model("model.keras")
    image = load_img(image_filename, color_mode="grayscale", target_size=(28, 28))
    arr = img_to_array(image)
    arr /= 255
    arr = arr.reshape(1, 28, 28, 1)
    output = model.predict(arr)
    return np.argmax(output)

if __name__ == "__main__":
    print(predict_number(sys.argv[1]))
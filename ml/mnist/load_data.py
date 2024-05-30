import numpy as np
from keras.utils import to_categorical
import os

DATA_DIRECTORY = "data"

TRAINING_IMAGES_FILENAME = "train-images.idx3-ubyte"
TRAINING_LABELS_FILENAME = "train-labels.idx1-ubyte"
TESTING_IMAGES_FILENAME = "t10k-images.idx3-ubyte"
TESTING_LABELS_FILENAME = "t10k-labels.idx1-ubyte"

TRAINING_SET_SIZE = 60 * 1000
TESTING_SET_SIZE = 10 * 1000

def load_images_data(filename, set_size, offset=16):
    file_path = os.path.join(DATA_DIRECTORY, filename)
    with open(file_path, "rb") as fi:
        all_bytes = fi.read()
        all_numbers = list(all_bytes[offset:])
        data_x = np.array(all_numbers).reshape((set_size, 28, 28, 1))
        data_x = data_x.astype("float32") / 255.0
    return data_x

def load_labels(filename, offset=8):
    file_path = os.path.join(DATA_DIRECTORY, filename)
    with open(file_path, "rb") as fi:
        all_bytes = fi.read()
        all_numbers = list(all_bytes[offset:])
        data_y = np.array(all_numbers)
        data_y = to_categorical(data_y)
    return data_y

def load_data():
    training_x = load_images_data(TRAINING_IMAGES_FILENAME, TRAINING_SET_SIZE)
    testing_x = load_images_data(TESTING_IMAGES_FILENAME, TESTING_SET_SIZE)
    training_y = load_labels(TRAINING_LABELS_FILENAME)
    testing_y = load_labels(TESTING_LABELS_FILENAME)
    return training_x, testing_x, training_y, testing_y
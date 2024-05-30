# Based on https://machinelearningmastery.com/how-to-develop-a-convolutional-neural-network-from-scratch-for-mnist-handwritten-digit-classification/

import load_data
import define_model

def train_model(write_filename=None):
    training_x, testing_x, training_y, testing_y = load_data.load_data()
    model = define_model.define_model()
    model.fit(
        x=training_x,
        y=training_y,
        batch_size=32,
        epochs=10,
        verbose=0
    )
    if write_filename:
        model.save(write_filename)
    return model
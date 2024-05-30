from keras import Sequential, Input
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.optimizers import SGD


def define_model(
        learning_rate=0.01,
        momentum=0.9,
        num_filters=32,
        dense_layer_units=100
):

    model = Sequential()
    model.add(Input(shape=(28, 28, 1)))
    model.add(Conv2D(
        filters=num_filters,
        kernel_size=(3, 3),
        activation="relu",
        kernel_initializer="he_uniform"
    ))
    model.add(MaxPooling2D(
        pool_size=(2, 2)
    ))
    model.add(Flatten())
    model.add(Dense(
        units=dense_layer_units,
        activation="relu",
        kernel_initializer="he_uniform"
    ))
    model.add(Dense(
        units=10,
        activation="softmax"
    ))

    optimizer = SGD(
        learning_rate=learning_rate,
        momentum=momentum
    )

    model.compile(
        optimizer=optimizer,
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model
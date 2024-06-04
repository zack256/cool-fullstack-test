from sklearn.model_selection import KFold
import matplotlib.pyplot as plt
import numpy as np
import sys

import load_data
import define_model

def evaluate_model(
        data=None,
        num_folds=5
):
    
    if data is None:
        training_x, testing_x, training_y, testing_y = load_data.load_data()
        data_x = training_x
        data_y = training_y
    else:
        data_x, data_y = data

    kf = KFold(
        n_splits=num_folds,
        shuffle=True,
        random_state=1
    )

    accuracies = []
    histories = []

    for train_indices, validation_indices in kf.split(data_x):
        model = define_model.define_model()
        train_x, validation_x = data_x[train_indices], data_x[validation_indices]
        train_y, validation_y = data_y[train_indices], data_y[validation_indices]
        history = model.fit(
            x=train_x,
            y=train_y,
            batch_size=32,
            epochs=10,
            validation_data=(validation_x, validation_y),
            verbose=0
        )
        _, accuracy = model.evaluate(
            x=validation_x,
            y=validation_y,
            verbose=0
        )
        print("Accuracy:", accuracy * 100)
        accuracies.append(accuracy)
        histories.append(history)
    
    return accuracies, histories

def summarize_diagnostics(histories, write_filename):
    for c, history in enumerate(histories):
        plt.subplot(2, 1, 1)
        plt.title("Cross Entropy Loss")
        plt.plot(history.history["loss"], color="blue", label="train")
        plt.plot(history.history["val_loss"], color="orange", label="test")
        plt.subplot(2, 1, 2)
        plt.title("Classification Accuracy")
        plt.plot(history.history["accuracy"], color="blue", label="train")
        plt.plot(history.history["val_accuracy"], color="orange", label="test")
    plt.savefig(write_filename)
    plt.close()

def summarize_performance(accuracies, write_filename):
    print(f"Accuracy: mean={np.mean(accuracies) * 100}, std={np.std(accuracies) * 100}, n={len(accuracies)}")
    plt.boxplot(accuracies)
    plt.savefig(write_filename)
    plt.close()

if __name__ == "__main__":
    accuracies, histories = evaluate_model()
    summarize_diagnostics(histories, sys.argv[1])
    summarize_performance(accuracies, sys.argv[2])

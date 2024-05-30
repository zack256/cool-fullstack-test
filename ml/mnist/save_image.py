import sys
import matplotlib.pyplot as plt
import numpy as np

TRAIN_IMAGES_FILENAME = "train-images.idx3-ubyte"
TEST_IMAGES_FILENAME = "t10k-images.idx3-ubyte"

def save_image(read_filename, write_filename, image_idx):

    bytes_offset = 16
    image_width = 28
    image_height = 28
    image_size = image_width * image_height

    with open(read_filename, "rb") as fi:
        all_images_bytes = fi.read()
    
    selected_image_bytes = all_images_bytes[bytes_offset + image_size * image_idx : bytes_offset + image_size * (image_idx + 1)]

    image = np.array(list(selected_image_bytes)).reshape((image_width, image_height))

    plt.imsave(write_filename, image, cmap="Greys", vmin=0, vmax=255)

def save_train_image(write_filename, image_idx):
    return save_image(TRAIN_IMAGES_FILENAME, write_filename, image_idx)

def save_test_image(write_filename, image_idx):
    return save_image(TEST_IMAGES_FILENAME, write_filename, image_idx)

def main():
    save_image(sys.argv[1], sys.argv[2], int(sys.argv[3]))

if __name__ == "__main__":
    main()
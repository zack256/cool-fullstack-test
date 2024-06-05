import keras
from keras.utils import load_img, img_to_array
import numpy as np
import sys
import boto3
import os

def predict_number(model, image_path):
    image = load_img(image_path, color_mode="grayscale", target_size=(28, 28))
    arr = img_to_array(image)
    arr /= 255
    arr = arr.reshape(1, 28, 28, 1)
    output = model.predict(arr)
    return np.argmax(output)

def test():
    s3 = boto3.client("s3")
    bucket_name = os.environ["BUCKET_NAME"]
    objects = s3.list_objects_v2(Bucket=bucket_name)
    if "Contents" in objects:
        model = keras.models.load_model("model.keras")
        for object in objects["Contents"]:
            object_name = object["Key"]
            save_file_path = os.path.join(os.getcwd(), "downloads", object_name)
            with open(save_file_path, "wb") as fi:
                s3.download_fileobj(bucket_name, object_name, fi)
            prediction = predict_number(model, save_file_path)
            print(object_name, "->", prediction)

if __name__ == "__main__":
    # print(predict_number(sys.argv[1]))
    test()
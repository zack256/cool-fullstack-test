import keras
from keras.utils import load_img, img_to_array
import numpy as np
import boto3
import os
from pymongo import MongoClient

def get_abs_path_from_rel_path(*rel_paths):
    return os.path.join(os.path.dirname(__file__), *rel_paths)

def predict_number(model, image_path):
    image = load_img(image_path, color_mode="grayscale", target_size=(28, 28))
    arr = img_to_array(image)
    arr /= 255
    arr = arr.reshape(1, 28, 28, 1)
    output = model.predict(arr)
    return int(np.argmax(output))

def mongo_testing():
    mongo_server_host = os.environ["MONGO_HOST"]
    mongo_server_port = os.environ["MONGO_PORT"]
    mongo_db_name = os.environ["MONGO_DB_NAME"]
    bucket_name = os.environ["BUCKET_NAME"]
    mongo_server_uri = f"mongodb://{mongo_server_host}:{mongo_server_port}"
    client = MongoClient(mongo_server_uri)
    database = client[mongo_db_name]
    collection = database["files"]
    unprocessed = list(collection.find({"processed": False}))
    if unprocessed:
        keys = [doc["key"] for doc in unprocessed]
        s3 = boto3.client("s3")
        model = keras.models.load_model(get_abs_path_from_rel_path("model.keras"))
        for key in keys:
            save_file_path = get_abs_path_from_rel_path("downloads", key)
            with open(save_file_path, "wb") as fi:
                s3.download_fileobj(bucket_name, key, fi)
            prediction = predict_number(model, save_file_path)
            update_info = collection.update_one(
                {
                    "key": key
                },
                {
                    "$set": {
                        "processed": True,
                        "result": prediction
                    }
                }
            )
            os.remove(save_file_path)
            s3.delete_object(Bucket=bucket_name, Key=key)

if __name__ == "__main__":
    # predict_all_images_in_s3_bucket()
    mongo_testing()
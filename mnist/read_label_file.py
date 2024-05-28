import sys

LABEL_FILES_MAGIC_NUMBER = 2049

def read_label_file(filename):

    with open(filename, "rb") as fi:
        file_bytes = fi.read()

    labels = []

    magic_number = int.from_bytes(file_bytes[:4], "big")
    if magic_number != LABEL_FILES_MAGIC_NUMBER:
        raise Exception("Magic number doesn't match!")

    num_labels = int.from_bytes(file_bytes[4:8], "big")
    for i in range(num_labels):
        labels.append(file_bytes[i + 8])
    
    return labels

if __name__ == "__main__":
    labels = read_label_file(sys.argv[1])
    print(labels)
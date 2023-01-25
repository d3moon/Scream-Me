import os

def read_private_key(filepath):
    if not os.path.isfile(filepath):
        print("[ERROR] The file does not exist.")
        return None
    with open(filepath, 'rb') as f:
        key = f.read()
        key = key.decode()
    return key

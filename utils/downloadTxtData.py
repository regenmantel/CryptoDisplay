import urllib.request
import os.path

def download_txt_file(url, save_path):
    try:
        if os.path.isfile(save_path):
            print(f"File already exists.");
        else:
            urllib.request.urlretrieve(url, save_path)
            print(f"File downloaded and saved to {save_path}.")
    except Exception as e:
        print(f"Error: {e}")


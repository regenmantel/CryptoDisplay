import urllib.request
import os.path

def download_php_file(url, save_path):
    if os.path.isfile(save_path):
        print(f"File already exists.");
    else:
        urllib.request.urlretrieve(url, save_path)
        print(f"File downloaded and saved to {save_path}.")

url = "http://www.die-staemme.de/backend/get_servers.php"
save_path = "data/files/servers/servers.php"

#if __name__ == "__main__":
download_php_file(url, save_path)


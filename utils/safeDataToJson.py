import json
from tkinter import filedialog
from utils.deserializeData import data_list

def save_as_json(data, default_extension=".json"):
    file_path = filedialog.asksaveasfilename(defaultextension=default_extension, filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file)
        print(f"Data has been saved to {file_path}")
        
def saveAs():
    decoded_data = {key.decode(): value.decode() for key, value in data_list}
    save_as_json(decoded_data)
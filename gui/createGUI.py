import tkinter as tk
from tkinter import ttk
from utils.deserializeData import *
from utils.downloadTxtData import *
from utils.safeDataToJson import saveAs
from utils.readPlayerFile import *

def on_selected_server(event):
    selected_server_value = combo_box_servers.get()
    label_server.config(text=f"Selected server: {selected_server_value}")
    combo_box_player.set('')
    combo_box_player['values'] = read_player_file(f"data/files/player/{selected_server_value}_players.txt")

def on_selected_player(event):
    selected_player_value = combo_box_player.get()
    label_player.config(text=f"Selected player: {selected_player_value}")
    
def button_click_JSON():
    saveAs()

def button_click_DL():
    url = f"https://{combo_box_servers.get()}.die-staemme.de/map/player.txt"
    save_path = f"data/files/player/{combo_box_servers.get()}_players.txt"
    download_txt_file(url, save_path)    

app = tk.Tk()
app.title("dsInfo")
app.resizable(width=False, height=False)
app.minsize(width=200, height=100)

#Label Title Combobox Server
label_server_title = tk.Label(app, text="Server")
label_server_title.pack(pady=1)

#Combo Box Server
extracted_values = [item[0].decode() for item in data_list]
options = extracted_values
combo_box_servers = ttk.Combobox(app, values=options)
combo_box_servers.pack(padx=0, pady=0)
combo_box_servers.bind("<<ComboboxSelected>>", on_selected_server)

#Label Selected Server
label_server = tk.Label(app, text="")
label_server.pack(pady=0)

#Label Player
label_player_title = tk.Label(app, text="Player")
label_player_title.pack(pady=0)

#Combo Box Player
combo_box_player = ttk.Combobox(app)
combo_box_player.pack(padx=0, pady=0)
combo_box_player.bind("<<ComboboxSelected>>", on_selected_player)

#Label Selected Player
label_player = tk.Label(app, text="")
label_player.pack(pady=0)

button_json_dl = tk.Button(app, text="Save to JSON", command=button_click_JSON)
button_json_dl.pack(side="bottom", anchor="e", padx=8, pady=8)

button_txt_dl = tk.Button(app, text="DL", command=button_click_DL)
button_txt_dl.pack(side="bottom", anchor="e", padx=8, pady=8)

def run():
    app.mainloop()
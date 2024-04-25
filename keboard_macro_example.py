import tkinter as tk
from tkinter import ttk, simpledialog
import keyboard
import time
import threading
import configparser
import os
import ctypes

def is_any_key_pressed():
    return any(keyboard.is_pressed(key) for key in keys_list)

def handle_keyboard_input():
    global stop_flag, n_pressed, pressed_keys

    while not stop_flag:
        new_pressed_keys = set(key for key in keys_list if keyboard.is_pressed(key))

        newly_pressed_keys = new_pressed_keys - pressed_keys

        for key in newly_pressed_keys:
            keyboard.press(special_key)
            
        for key in pressed_keys - new_pressed_keys:
            keyboard.release(special_key)
        pressed_keys = new_pressed_keys

        time.sleep(0.001)

def update_status_label(text):
    status_label.config(text=text)

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    update_style()
    update_labels()

def update_style():
    if dark_mode:
        root.configure(bg='#1e1e1e')
        style.configure('TButton', background='#292929', foreground='white', font=('Arial', 14))
        style.configure('TLabel', background='#1e1e1e', foreground='white', font=('Arial', 14))
    else:
        root.configure(bg='white')
        style.configure('TButton', background='grey', foreground='black', font=('Arial', 14))
        style.configure('TLabel', background='grey', foreground='black', font=('Arial', 14))

def start_macro():
    global stop_flag, n_pressed, pressed_keys
    stop_flag = False
    n_pressed = False
    pressed_keys = set()
    status_label.config(text="Macro On Run")

    macro_thread = threading.Thread(target=handle_keyboard_input)
    macro_thread.start()

def stop_macro():
    global stop_flag
    stop_flag = True
    status_label.config(text="Macro OFF")

def set_keys():
    global keys_list
    config = load_config()
    new_keys = simpledialog.askstring(language_dict['set_keys_title'], language_dict['set_keys_prompt'])
    if new_keys:
        keys_list = new_keys.split()[:5]
        config['DEFAULT']['keys'] = ' '.join(keys_list)
        save_config(config)

def set_n_key():
    global special_key
    config = load_config()
    new_special_key = simpledialog.askstring(language_dict['set_n_key_title'], language_dict['set_n_key_prompt'])
    if new_special_key:
        special_key = new_special_key
        config['DEFAULT']['special_key'] = special_key
        save_config(config)

def load_keys():
    config = load_config()
    try:
        keys = config['DEFAULT']['keys']
        keys_list = keys.split()
        special_key = config['DEFAULT'].get('special_key', 'n')
        return keys_list, special_key
    except (configparser.NoSectionError, KeyError):
        return ['a', 's', 'j', 'k', 'l'], 'n'

def show_current_keys():
    config = load_config()
    keys = config['DEFAULT'].get('keys', 'a s j k l')
    special_key_text = config['DEFAULT'].get('special_key', 'n')
    update_status_label(language_dict['normal_keys'] + keys + "\n" + language_dict['special_key'] + special_key_text)
    root.after(10000, clear_status_label)

def clear_status_label():
    update_status_label("")

def change_language():
    global current_language, language_dict
    config = load_config()
    if current_language == 'english':
        current_language = 'spanish'
        language_dict = spanish_dict
    else:
        current_language = 'english'
        language_dict = english_dict
    config['DEFAULT']['language_pred'] = current_language
    save_config(config)
    update_labels()

def update_labels():
    language_button.config(text=language_dict['language_button'])
    start_button.config(text=language_dict['start_button'])
    stop_button.config(text=language_dict['stop_button'])
    set_keys_button.config(text=language_dict['set_keys_button'])
    set_special_key_button.config(text=language_dict['set_special_key_button'])
    show_keys_button.config(text=language_dict['show_keys_button'])
    update_status_label(language_dict['macro_off'])

def load_config():
    config = configparser.ConfigParser()
    if os.path.exists("set-up_keys.ini"):
        config.read("set-up_keys.ini")
        if 'language_pred' not in config['DEFAULT']:
            config['DEFAULT']['language_pred'] = 'english'
            save_config(config)
    else:
        config['DEFAULT'] = {}
        config['DEFAULT']['language_pred'] = 'english'
        config['DEFAULT']['special_key'] = 'n'
        config['DEFAULT']['keys'] = 'a s j k l'
        save_config(config)
    return config

def save_config(config):
    config_file_path = "set-up_keys.ini"
    with open(config_file_path, "w") as configfile:
        config.write(configfile)
    return config_file_path

keys_list, special_key = load_keys()
keys_set = set(keys_list)
n_pressed = False
config = load_config()
config_file_path = save_config(config)

english_dict = {
    'language_button': 'EN',
    'start_button': 'Start Macro',
    'stop_button': 'Stop Macro',
    'set_keys_button': 'Set Keys',
    'set_special_key_button': 'Set Special Key',
    'show_keys_button': 'Show Actual Keys',
    'macro_off': 'Macro OFF',
    'macro_on': 'Macro On Run',
    'set_keys_title': 'Set Keys',
    'set_keys_prompt': 'Enter up to 5 new keys (separated by spaces):',
    'set_n_key_title': 'Set Special Key',
    'set_n_key_prompt': 'Enter a new key for strump key:',
    'normal_keys': 'Normal Keys: ',
    'special_key': 'Special Key: ',
}

spanish_dict = {
    'language_button': 'ES',
    'start_button': 'Iniciar Macro',
    'stop_button': 'Detener Macro',
    'set_keys_button': 'Configurar Teclas',
    'set_special_key_button': 'Configurar Tecla Especial',
    'show_keys_button': 'Mostrar Teclas Actuales',
    'macro_off': 'Macro APAGADO',
    'macro_on': 'Macro En Ejecución',
    'set_keys_title': 'Configurar Teclas',
    'set_keys_prompt': 'Ingrese hasta 5 nuevas teclas (separadas por espacios):',
    'set_n_key_title': 'Configurar Tecla Especial',
    'set_n_key_prompt': 'Ingrese una nueva tecla para la tecla especial:',
    'normal_keys': 'Teclas Normales: ',
    'special_key': 'Tecla Especial: ',
}

language_dict = english_dict

current_language = 'english'

dark_mode = True 
root = tk.Tk()
style = ttk.Style(root)
root.tk_setPalette(background='#1e1e1e', foreground='white')
style.theme_use('clam')

hwnd = ctypes.windll.kernel32.GetConsoleWindow()
if hwnd != 0:
    ctypes.windll.user32.SetWindowLongW(hwnd, -20, ctypes.windll.user32.GetWindowLongW(hwnd, -20) | 0x00080000)

root.title("Key Macro")
root.geometry("230x320")
root.resizable(False, False)

language_button = ttk.Button(root, command=change_language, text=language_dict['language_button'])
start_button = ttk.Button(root, text=language_dict['start_button'], command=start_macro)
stop_button = ttk.Button(root, text=language_dict['stop_button'], command=stop_macro)
set_keys_button = ttk.Button(root, text=language_dict['set_keys_button'], command=set_keys)
set_special_key_button = ttk.Button(root, text=language_dict['set_special_key_button'], command=set_n_key)
show_keys_button = ttk.Button(root, text=language_dict['show_keys_button'], command=show_current_keys)
status_label = ttk.Label(root, text=language_dict['macro_off'])
additional_text = ttk.Label(root, text="@Frosh_30")
language_button.pack(side=tk.TOP, anchor=tk.NE)
start_button.pack()
stop_button.pack()
set_keys_button.pack()
set_special_key_button.pack()
show_keys_button.pack()
status_label.pack(side=tk.BOTTOM, fill=tk.X)
additional_text.pack(pady=18)

root.mainloop()

import tkinter as tk
from tkinter import ttk
import keyboard
import time
import threading

def is_any_key_pressed():
    return any(keyboard.is_pressed(key) for key in ['a', 's', 'j', 'k', 'l'])

def start_macro():
    global n_pressed, stop_flag
    stop_flag = False
    n_pressed = False
    status_label.config(text="Macro On Run")
    while not stop_flag:
        if is_any_key_pressed():
            if not n_pressed:
                time.sleep(0.001)
                if is_any_key_pressed():
                    keyboard.press('n')
                    n_pressed = True
        else:
            if n_pressed:
                keyboard.release('n')
                n_pressed = False
        time.sleep(0.0001)
        root.update()

def stop_macro():
    global stop_flag
    stop_flag = True
    status_label.config(text="Macro OFF")
n_pressed = False
stop_flag = False

root = tk.Tk()
root.title("Macro Example")

root.geometry("200x150")
root.configure(bg='black')

style = ttk.Style()
style.configure('TButton', background='grey', foreground='black', font=('Arial', 12))
style.configure('TLabel', background='grey', foreground='black', font=('Arial', 12))

start_button = ttk.Button(root, text="Start Macro", command=start_macro, style='TButton')
start_button.pack(pady=10)

stop_button = ttk.Button(root, text="Stop Macro", command=stop_macro, style='TButton')
stop_button.pack(pady=5)

status_label = ttk.Label(root, text="Macro OFF", style='TLabel')
status_label.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
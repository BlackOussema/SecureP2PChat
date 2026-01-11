import socket
import threading
from cryptography.fernet import Fernet

key = input("Enter the encryption key from the server: ").encode()
cipher = Fernet(key)

host = input("Enter server IP address: ")
port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive_messages():
    while True:
        try:
            encrypted_msg = client.recv(1024)
            if not encrypted_msg:
                break
            msg = cipher.decrypt(encrypted_msg).decode()
            print(f"Server says: {msg}")
        except:
            break

def send_messages():
    while True:
        msg = input()
        encrypted_msg = cipher.encrypt(msg.encode())
        try:
            client.send(encrypted_msg)
        except:
            break

recv_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

recv_thread.start()
send_thread.start()

recv_thread.join()
send_thread.join()

client.close()

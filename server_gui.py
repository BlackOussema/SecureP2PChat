import socket
import threading
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import scrolledtext

class ChatServerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Encrypted Chat Server")

        self.chat_area = scrolledtext.ScrolledText(master, state='disabled', width=50, height=20)
        self.chat_area.pack(padx=10, pady=10)

        self.entry_msg = tk.Entry(master, width=40)
        self.entry_msg.pack(side='left', padx=(10,0), pady=(0,10))

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(side='left', padx=10, pady=(0,10))

        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"Encryption key (share with clients): {self.key.decode()}\n")
        self.chat_area.config(state='disabled')

        self.host = '0.0.0.0'
        self.port = 12345

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)

        self.clients = []

        self.running = True

        threading.Thread(target=self.accept_clients, daemon=True).start()

    def accept_clients(self):
        self.print_message(f"Server running on port {self.port}, waiting for connections...")
        while self.running:
            try:
                conn, addr = self.server.accept()
                self.clients.append(conn)
                self.print_message(f"New connection from {addr}")
                threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True).start()
            except:
                break

    def handle_client(self, conn, addr):
        while self.running:
            try:
                encrypted_msg = conn.recv(1024)
                if not encrypted_msg:
                    break
                msg = self.cipher.decrypt(encrypted_msg).decode()
                self.print_message(f"[{addr}] says: {msg}")
            except:
                break
        self.print_message(f"Connection from {addr} closed.")
        conn.close()
        if conn in self.clients:
            self.clients.remove(conn)

    def send_message(self):
        msg = self.entry_msg.get()
        if msg:
            encrypted_msg = self.cipher.encrypt(msg.encode())
            for client in self.clients:
                try:
                    client.send(encrypted_msg)
                except:
                    pass
            self.print_message(f"You: {msg}")
            self.entry_msg.delete(0, tk.END)

    def print_message(self, msg):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, msg + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

    def close(self):
        self.running = False
        self.server.close()
        for client in self.clients:
            client.close()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatServerGUI(root)
    root.protocol("WM_DELETE_WINDOW", gui.close)
    root.mainloop()

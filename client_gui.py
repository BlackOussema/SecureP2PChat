import socket
import threading
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import scrolledtext
from tkinter import simpledialog

class ChatClientGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Encrypted Chat Client")

        self.chat_area = scrolledtext.ScrolledText(master, state='disabled', width=50, height=20)
        self.chat_area.pack(padx=10, pady=10)

        self.entry_msg = tk.Entry(master, width=40)
        self.entry_msg.pack(side='left', padx=(10,0), pady=(0,10))

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(side='left', padx=10, pady=(0,10))

        key = simpledialog.askstring("Encryption Key", "Enter encryption key from server:")
        host = simpledialog.askstring("Server IP", "Enter server IP address:")
        port = 12345

        self.cipher = Fernet(key.encode())

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

        self.running = True

        threading.Thread(target=self.receive_messages, daemon=True).start()

    def receive_messages(self):
        while self.running:
            try:
                encrypted_msg = self.client.recv(1024)
                if not encrypted_msg:
                    break
                msg = self.cipher.decrypt(encrypted_msg).decode()
                self.print_message(f"Server: {msg}")
            except:
                break
        self.print_message("Connection closed.")
        self.client.close()

    def send_message(self):
        msg = self.entry_msg.get()
        if msg:
            encrypted_msg = self.cipher.encrypt(msg.encode())
            try:
                self.client.send(encrypted_msg)
                self.print_message(f"You: {msg}")
                self.entry_msg.delete(0, tk.END)
            except:
                pass

    def print_message(self, msg):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, msg + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

    def close(self):
        self.running = False
        self.client.close()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatClientGUI(root)
    root.protocol("WM_DELETE_WINDOW", gui.close)
    root.mainloop()

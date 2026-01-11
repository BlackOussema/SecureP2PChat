<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Encryption-Fernet%20(AES)-green.svg" alt="Encryption">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

<h1 align="center">🔐 SecureP2PChat</h1>

<p align="center">
  <strong>Encrypted Peer-to-Peer Chat Application</strong>
</p>

<p align="center">
  A secure, end-to-end encrypted chat application with both CLI and GUI interfaces.<br>
  Built with Python using Fernet (AES-128) symmetric encryption.
</p>

---

## ✨ Features

- **End-to-End Encryption** - All messages encrypted with Fernet (AES-128-CBC)
- **Symmetric Key Exchange** - Secure key sharing between peers
- **Multi-Client Support** - Server handles multiple simultaneous connections
- **Dual Interface** - Both command-line and graphical user interfaces
- **Real-Time Messaging** - Instant message delivery with threading
- **Cross-Platform** - Works on Windows, Linux, and macOS

---

## 🔒 Security

### Encryption Details
- **Algorithm**: Fernet (AES-128-CBC with HMAC)
- **Key Generation**: Cryptographically secure random key
- **Message Authentication**: HMAC-SHA256 for integrity
- **Timestamp Validation**: Prevents replay attacks

### Security Considerations
- Keys should be exchanged through a secure channel
- Each session generates a new encryption key
- Messages are encrypted before transmission
- No plaintext data stored or logged

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/BlackOussema/SecureP2PChat.git
cd SecureP2PChat

# Install dependencies
pip install cryptography
```

### Running the Server

```bash
# Command-line interface
python server.py

# Graphical interface
python server_gui.py
```

The server will display an encryption key - share this securely with clients.

### Running the Client

```bash
# Command-line interface
python client.py

# Graphical interface
python client_gui.py
```

Enter the server IP and encryption key when prompted.

---

## 📖 Usage

### Server Setup

1. Start the server:
   ```bash
   python server.py
   ```

2. Note the encryption key displayed:
   ```
   Encryption key (share with client): gAAAAABk...
   Server running on port 12345. Waiting for connections...
   ```

3. Share the key securely with clients (in person, encrypted email, etc.)

### Client Connection

1. Start the client:
   ```bash
   python client.py
   ```

2. Enter the encryption key from the server

3. Enter the server's IP address

4. Start chatting securely!

---

## 🖥️ Interfaces

### Command-Line Interface (CLI)

**Server (`server.py`)**
- Displays connection notifications
- Shows decrypted messages from clients
- Type messages to broadcast to all clients

**Client (`client.py`)**
- Enter encryption key and server IP
- Send and receive encrypted messages
- Simple text-based interface

### Graphical Interface (GUI)

**Server GUI (`server_gui.py`)**
- Visual connection management
- Message history display
- Easy key copying

**Client GUI (`client_gui.py`)**
- User-friendly connection dialog
- Chat window with message history
- Send button and Enter key support

---

## 📁 Project Structure

```
SecureP2PChat/
├── server.py           # CLI server
├── server_gui.py       # GUI server (Tkinter)
├── client.py           # CLI client
├── client_gui.py       # GUI client (Tkinter)
└── README.md
```

---

## 🔧 Configuration

### Default Settings

| Setting | Value | Description |
|---------|-------|-------------|
| Port | 12345 | Server listening port |
| Host | 0.0.0.0 | Server bind address |
| Buffer | 1024 | Message buffer size |

### Customization

Edit the server/client files to change:

```python
# Change port
port = 12345  # Modify this value

# Change buffer size
encrypted_msg = conn.recv(1024)  # Increase for larger messages
```

---

## 🔐 How It Works

### Key Exchange Flow

```
1. Server generates Fernet key
2. Server displays key to admin
3. Admin shares key with client (out-of-band)
4. Client enters key to connect
5. All messages encrypted with shared key
```

### Message Flow

```
Client                          Server
  |                               |
  |-- Encrypt(message, key) ---->|
  |                               |-- Decrypt(message, key)
  |                               |-- Display message
  |                               |
  |<-- Encrypt(response, key) ---|
  |-- Decrypt(response, key)     |
  |-- Display response           |
```

---

## 📋 Requirements

```
cryptography>=3.4.0
```

For GUI:
```
tkinter (usually included with Python)
```

---

## ⚠️ Security Disclaimer

**This application is for educational purposes.**

- Do NOT use for highly sensitive communications
- Key exchange should be done through secure channels
- Consider using established protocols (Signal, etc.) for production
- No forward secrecy - compromised key exposes all messages

### Recommendations for Production

1. Implement proper key exchange (Diffie-Hellman)
2. Add user authentication
3. Implement forward secrecy
4. Use TLS for transport layer
5. Add message persistence with encryption at rest

---

## 🤝 Contributing

Contributions are welcome! Ideas:

- Implement Diffie-Hellman key exchange
- Add file transfer capability
- Create mobile app version
- Add user authentication
- Implement group chat

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**Ghariani Oussema**
- GitHub: [@BlackOussema](https://github.com/BlackOussema)
- Role: Cyber Security Researcher & Full-Stack Developer
- Location: Tunisia 🇹🇳

---

<p align="center">
  Made with ❤️ in Tunisia 🇹🇳
</p>

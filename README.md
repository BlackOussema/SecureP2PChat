# SecureP2PChat

SecureP2PChat is a peer-to-peer encrypted chat application with a graphical user interface, designed to provide secure and private communication over the internet.

#Features

- End-to-end encryption using the `cryptography` library (Fernet).
- Direct peer-to-peer communication without relying on a central server.
- User-friendly graphical interface built with `Tkinter`.
- Compatible with Linux and Windows systems (requires Python 3).

 #Requirements

- Python 3.6 or newer
- 'cryptography` library
- 'tkinter` (usually included with Python)

#Installation and Usage

## 1. Set up a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate    # On Linux / Kali Linux
# or
.\venv\Scripts\activate     # On Windows PowerShell

2. Install required libraries
pip install cryptography
3. Run the server
python server_gui.py
The server window will display an encryption key. Share this key with anyone you want to chat with.

4. Run the client
python client_gui.py
Enter the encryption key provided by the server.

Enter the server’s IP address (you can find your public IP at https://whatismyipaddress.com/).

Start chatting securely.

If the application doesn’t run due to missing libraries, make sure your virtual environment is activated and the dependencies are installed as described above.

Remember to forward port 12345 on your router to allow incoming connections to the server.

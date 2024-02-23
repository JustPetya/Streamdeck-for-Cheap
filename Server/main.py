import os
import socket
import socketserver
import ssl
from page.CustomHandler import CustomHandler
from required.get_pip import get_pip
from setup.check_backend import check_backend

# try:
#     import pyautogui
# except ImportError:
#     print("\"pyautogui\" not found")
# try:
#     from pynput.keyboard import Listener
# except ImportError:
#     print("\"pynput\" not found")
# # try:
# #     import pygame
# # except ImportError:
# #     print("\"pygame\" not found")
# try:
#     import keyboard
# except ImportError:
#     print("\"keyboard\" not found")

sys = "simple"
if os.name in ("nt", "dos"):
    sys = "dos"


def main():
    # retrieving data for pip update
    auto_update = check_backend.usr()
    if auto_update:
        get_pip.run_update()
    else:
        pass

    cert = check_backend.certificate()
    # defining specifics for http and https
    if cert:
        PORT = 8443

        # Set up SSL context
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain(certfile="requires/cert.pem", keyfile="requires/key.pem")
        # place your certificate and key inside the required-directory and replace the existing files,
        # you can easily create a ssl certificate using OpenSSL

        # Start server ssl-certified
        with socketserver.TCPServer(("0.0.0.0", PORT), CustomHandler) as httpsd:
            IPAddr = socket.gethostbyname(socket.gethostname())  # gather Host-IP
            print(f"Serving on port {PORT}, website is hosted under " + IPAddr + f":{PORT}")
            httpsd.socket = ssl_context.wrap_socket(httpsd.socket, server_side=True)

            try:
                httpsd.serve_forever()
            except KeyboardInterrupt:
                print("\nServer shutting down...")
                httpsd.server_close()
    elif not cert:
        PORT = 8000

        # Start server unencrypted
        with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
            IPAddr = socket.gethostbyname(socket.gethostname())
            print(f"Serving on port {PORT}, website is hosted under " + IPAddr + f":{PORT}")

            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nServer shutting down...")
                httpd.server_close()
    else:
        print("Sorry there was an error, please check if settings.ini got correct data!")
        exit("0")


if __name__ == "__main__":
    if sys == "dos":
        os.system("cls")
    else:
        os.system("clear")
    main()

from setup.get_settings import check_backend as backend
# from page.page import CustomHandler as handler
import ssl
import http.server
import mimetypes
import os
import socket
import socketserver

try:
    import pyautogui

    _imports = False
except ImportError:
    print("\"pyautogui\" not found")
    _imports = True
try:
    from pynput.keyboard import Listener

    _imports = False
except ImportError:
    print("\"pynput\" not found")
    _imports = True
try:
    import pygame

    _imports = False
except ImportError:
    print("\"pygame\" not found")
    _imports = True
try:
    import keyboard

    _imports = False
except ImportError:
    print("\"keyboard\" not found")
    _imports = True

sys = "simple"
if os.name in ("nt", "dos"):
    sys = "dos"


def main():
    # retrieving data for pip update
    auto_update = backend.usr()
    if sys == "simple" & auto_update & _imports:
        os.system("python3 required/get_pip.py")
    elif sys == "dos" & auto_update & _imports:
        os.system("python required/get_pip.py")
    else:
        pass

    # TODO: move that shit to page/page.py
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header("Access-Control-Allow-Origin", "*")  # Allow requests from any origin
            super().end_headers()

        pygame.mixer.init()
        hotkeys = {}

        def do_GET(self):
            # Extract the path from the URL
            path = self.path
            # Remove the leading slash to get the file name without the extension
            file_name = os.path.splitext(os.path.basename(path))[0]

            # Check if the request is for instructions
            if path.startswith("/instructions"):
                # Extract instructions from the URL query parameters
                instructions = path.split("?")[1]

                # discord
                if instructions == 'discord_mute':
                    pyautogui.press('f15')
                elif instructions == 'discord_deafen':
                    pyautogui.press('f16')
                elif instructions == 'discord_end-stream':
                    pyautogui.press('f14')
                elif instructions == 'discord_leave':
                    pyautogui.press('f17')
                # filmora
                elif instructions == 'filmora_cut':
                    keyboard.press_and_release('ctrl+b')
                # spotify
                elif instructions == 'music_previous':
                    pyautogui.press('prevtrack')
                elif instructions == 'music_pause':
                    pyautogui.press('playpause')
                elif instructions == 'music_next':
                    pyautogui.press('nexttrack')
                # obs
                elif instructions == 'obs_startrecord':
                    pyautogui.press('f18')
                elif instructions == 'obs_stoprecord':
                    pyautogui.press('f19')
                elif instructions == 'obs_pauserecord':
                    pyautogui.press('ctrl+alt+\\')
                elif instructions == 'obs_startstream':
                    pyautogui.press('f20')
                elif instructions == 'obs_stopstream':
                    pyautogui.press('f21')
                elif instructions == 'obs_pausestream':
                    pyautogui.press('ctrl+shift+\\')
                elif instructions == 'obs_mutemic':
                    pyautogui.press('f22')
                elif instructions == 'obs_unmutemic':
                    pyautogui.press('f23')
                elif instructions == 'obs_screen':
                    keyboard.press_and_release('ctrl+shift+right')
                elif instructions == 'obs_krita':
                    keyboard.press_and_release('ctrl+alt+right')
                elif instructions == 'obs_game':
                    keyboard.press_and_release('ctrl+shift+left')
                elif instructions == 'obs_fullcam':
                    pyautogui.press('f24')
                elif instructions == 'obs_discord':
                    keyboard.press_and_release('ctrl+alt+down')
                # screenshot
                elif instructions == 'screenshot':
                    keyboard.press_and_release('print_screen')
                # voice changer
                elif instructions == 'vc':
                    keyboard.press_and_release('ctrl+alt+v')
                # error
                else:
                    # If the instruction doesn't match any predefined actions, serve a 404 error
                    self.send_error(404, "Action not found")
                actions_to_sounds = {
                    # Mom and Dad
                    "fart": "fart.wav",
                    "food": "food.wav",
                    "down": "down.wav"
                }

                if instructions in actions_to_sounds:
                    sound_file = actions_to_sounds[instructions]
                    sound_path = os.path.join(os.getcwd(), 'page/wav', sound_file)
                    if os.path.exists(sound_path):
                        sound_effect = pygame.mixer.Sound(sound_path)
                        sound_effect.play()

                # Send the response back to the client
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()

            elif path == "/":
                self.path = "/page/index.html"
                super().do_GET()
            elif path.startswith("/page/img/"):
                # Serve images from the 'img' folder
                img_path = os.path.join(os.getcwd(), 'page/img', os.path.basename(path))
                if os.path.exists(img_path) and os.path.isfile(img_path):
                    # If the requested image file exists, serve it with the appropriate content type
                    content_type, _ = mimetypes.guess_type(img_path)
                    self.send_response(200)
                    self.send_header("Content-type", content_type)
                    self.end_headers()

                    with open(img_path, 'rb') as img_file:
                        # Read and send the image content to the client
                        self.wfile.write(img_file.read())
                else:
                    # If the requested image file doesn't exist, serve a 404 error
                    self.send_error(404, "Image not found")
            elif path.startswith("/page/wav/"):
                # Serve sound files from the 'wav' folder
                sound_file_path = os.path.join(os.getcwd(), 'page/wav', os.path.basename(path))
                if os.path.exists(sound_file_path) and os.path.isfile(sound_file_path):
                    # If the requested sound file exists, serve it with the appropriate content type
                    content_type, _ = mimetypes.guess_type(sound_file_path)
                    self.send_response(200)
                    self.send_header("Content-type", content_type)
                    self.end_headers()

                    with open(sound_file_path, 'rb') as sound_file:
                        # Read and send the sound content to the client
                        self.wfile.write(sound_file.read())
                else:
                    # If the requested sound file doesn't exist, serve a 404 error
                    self.send_error(404, "Sound not found")
            else:
                html_file_path = os.path.join(os.getcwd(), 'page/html', f"{file_name}.html")
                if os.path.exists(html_file_path):
                    # Serve the sub-file from the html folder
                    self.path = f"/page/html/{file_name}.html"
                    super().do_GET()
                else:
                    # If the requested file doesn't exist, serve a 404 error page
                    self.send_error(404, "File not found")

        def do_POST(self):
            # Handle POST requests if needed
            pass

    cert = backend._certificate()
    # defining specifics for http and https
    if cert:
        PORT = 8443

        # TODO: let page/page.py handle everything regarding html and javascript

        # Set up SSL context
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain(certfile="requires/cert.pem", keyfile="requires/key.pem")
        # place your certificate and key inside the required-directory and replace the existing files, you can easily
        # create a ssl certificate using OpenSSL

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

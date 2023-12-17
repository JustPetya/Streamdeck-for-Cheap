"""
Author: Dustin Rex
Contact: 
    - E-mail: Dustin.Rex@pm.me
    - Discord User: itspetya
    - Discord Server: https://discord.gg/XE8YfAg56x
      Join my discord for new releases!
License: MIT License (as-is)

Feel free to write me with any questions, on my discord you can also look into the faq.
Also, if you want to support me or everyone else on the discord post useful codes into the channel.
"""



ImpError = 0
try:
    from datetime import datetime
except ImportError:
    ImpError = ImpError + 1
try:
    import http.server
except ImportError:
    ImpError = ImpError + 1
#try:
#    import ssl
#except ImportError:
#    ImpError = ImpError + 1
try:
    import socketserver
except ImportError:
    ImpError = ImpError + 1
try:
    import subprocess
except ImportError:
    ImpError = ImpError + 1
try:
    import time
except ImportError:
    ImpError = ImpError + 1
try:
    import os
except ImportError:
    ImpError = ImpError + 1
try:
    import sys
except ImportError:
    ImpError = ImpError + 1
try:
    import mimetypes
except ImportError:
    ImpError = ImpError + 1
# checking for errors
if ImpError == 0:
    print("There were NON errors.")
    time.sleep(3)
elif ImpError > 0:
    print("There were " + ImpError + " errors importing default projects, do you want to continue?\nContinue [Y], Quit [N]\n\nThe script might not work!")
    h8bWdC3h = input(">").lower()
    if h8bWdC3h.startswith("y"):
        main()
    elif h8bWdC3h.startswith("n"):
        os._exit(0)
    else:
        os._exit()
else:
    print("Something went wrong!")
    os._exit()

try:
    import pyautogui
except ImportError:
    input("The project \"pyautogui\" is is not installed on this system, do you want to install it?\nInstall? [ENTER]\n\nIf this Error keeps appearing reinstall that project or reinstall \"python3\"!\nRestart after the script closed!")
    os.system('python -m pip install pyautogui')
    pass
try:
    from pynput.keyboard import Listener
except ImportError:
    input("The project \"pynput\" is is not installed on this system, do you want to install it?\nInstall? [ENTER]\n\nIf this Error keeps appearing reinstall that project or reinstall \"python3\"!\nRestart after the script closed!")
    os.system('python -m pip install pynput')
    pass
try:
    import pygame
except ImportError:
    input("The project \"pygame\" is is not installed on this system, do you want to install it?\nInstall? [ENTER]\n\nIf this Error keeps appearing reinstall that project or reinstall \"python3\"!\nRestart after the script closed!")
    os.system('python -m pip install pygame')
    pass
try:
    import keyboard
except ImportError:
    input("The project \"keyboard\" is is not installed on this system, do you want to install it?\nInstall? [ENTER]\n\nIf this Error keeps appearing reinstall that project or reinstall \"python3\"!\nRestart after the script closed!")
    os.system('python -m pip install keyboard')
    pass


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#defines
def ClearAll():
    command = "clear"
    if os.name in ("nt", "dos"): #use "cls" on windows or dos
        command = "cls"
    os.system(command) 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    # Define the port on which you want to run the server
    # http
    PORT = 8000
    # https
    #HTTPS_PORT = 8443

    pygame.mixer.init()
    hotkeys = {}

    # Define a custom request handler to process incoming requests
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header("Access-Control-Allow-Origin", "*")  # Allow requests from any origin
            super().end_headers()

        def do_GET(self):
            path = self.path
            # Remove the leading slash to get the file name without the extension
            file_name = os.path.splitext(os.path.basename(path))[0]

            # Check if the request is for instructions
            if path.startswith("/instructions"):
                # Extract instructions from the URL query parameters
                instructions = path.split("?")[1]

                # some examples for the deck
                # discord
                if instructions == 'discord_mute':
                    pyautogui.press('f13')
                elif instructions == 'discord_deafen':
                    pyautogui.press('f14')
                elif instructions == 'discord_end-stream':
                    pyautogui.press('f15')
                elif instructions == 'discord_leave':
                    pyautogui.press('f16')
                # spotify
                elif instructions == 'music_previous':
                    pyautogui.press('prevtrack')
                elif instructions == 'music_pause':
                    pyautogui.press('playpause')
                elif instructions == 'music_next':
                    pyautogui.press('nexttrack')
                # error
                else:
                    # If the instruction doesn't match any predefined actions, serve a 404 error
                    self.send_error(404, "Action not found")
                actions_to_sounds = {
                    # sounds here (wav and mp3 are best)
                    'sound': ('sound.wav'),
                }
                
                # get sound instruction
                if instructions in actions_to_sounds:
                    sound_file = actions_to_sounds[instructions]
                    sound_path = os.path.join(os.getcwd(), 'wav', sound_file)
                    if os.path.exists(sound_path):
                        sound_effect = pygame.mixer.Sound(sound_path)
                        sound_effect.play()

                # Send the response back to the client
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()

            elif path == "/":
                self.path = "/index.html"
                super().do_GET()
            elif path.startswith("/img/"):
                # Serve images from the 'img' folder
                img_path = os.path.join(os.getcwd(), 'img', os.path.basename(path))
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
            elif path.startswith("/wav/"):
                # Serve sound files from the 'wav' folder
                sound_file_path = os.path.join(os.getcwd(), 'wav', os.path.basename(path))
                if os.path.exists(sound_file_path) and os.path.isfile(sound_file_path):
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
                html_file_path = os.path.join(os.getcwd(), 'html', f"{file_name}.html")
                if os.path.exists(html_file_path):
                    # Serve the sub-file from the html folder
                    self.path = f"/html/{file_name}.html"
                    super().do_GET()
                else:
                    # If the requested file doesn't exist, serve a 404 error page
                    self.send_error(404, "File not found")

                
        def do_POST(self):
            # Handle POST requests if needed
            pass

    # Set up the server with the custom request handler
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"Serving on port {PORT}")

        # Set up SSL context
        #ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        #ssl_context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

        # Start the server and keep it running (only if https/ssl)
        #with socketserver.TCPServer(("0.0.0.0", 8443), CustomHandler) as httpsd:
            #print(f"Serving on HTTPS port 8443")
            #httpsd.socket = ssl_context.wrap_socket(httpsd.socket, server_side=True)
        
        # change from httpd to httpsd if you want a ssl cerified connection
        try:
            httpd.serve_forever()
            #httpsd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer shutting down...")
            httpd.server_close()
            #httpsd.server_close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    ClearAll()
    main()

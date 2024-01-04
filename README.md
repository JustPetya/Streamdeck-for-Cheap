# Streamdeck for Cheap
## How to use!
First of all, this is not the best script you will find out there nor the most optimized, but it is definetive the cheapest one, you only need a PC as a server you want to have a streamdeck for and a phone, like I do a RaspberryPi Zero 2 W and a screen or any other device that has a screen and the power to run a browser that you can use.
It is also important that port 8000 is open in the netwok and all devices connected to this Streamdeck are in the same network. That's just for security, you can of cause also open it to all networks or recode it so you use it as a form of hotspot.

My code is written for http, so without an ssl certificate.
If you want to use the deck as https you have to command out the following lines:
```py
# line 110
PORT = 8000

# line 236
httpd.serve_forever()

# line 240
httpd.server_close()
```
And uncommand these lines:
```py
# line 25
try:
    import ssl
except ImportError:
    ImpError = ImpError + 1

# line 112
HTTPS_PORT = 8443

# line 226
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# for the certificate you have to paste your cert.pem and key.pam inside of the folder, the main.py script is in
ssl_context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

with socketserver.TCPServer(("0.0.0.0", 8443), CustomHandler) as httpsd:
    print(f"Serving on HTTPS port 8443")
    httpsd.socket = ssl_context.wrap_socket(httpsd.socket, server_side=True)

# line 237
httpsd.serve_forever()

# line 241
httpsd.server_close()
```

## Structure
---
>IDK if it's needed in a project so small like this one but here a structure section for you!
###### Sever (important for all)
- server/check.py | 
Is installing everything from requrements.md if it isn't allready.
- server/main.py |
The server and the interpretation of html files, audio playback and display of images.

###### Client (ignore every "Client" in PI02 if you manually open the website on use)
- PI02/check.py | 
Is installing everything from requrements.md if it isn't allready.
- PI02/main.py | 
The stuff that is controlling everything.
- PI02/util.py | 
Things like loggin (not in use) and starting the machine the server is on.
- PI02/browser.py | 
Start of the Chromium-Browser.

## WORKING ON
### TODO:
##### Server


##### Client


### FIXME:
##### Server


##### Client


### NOTES:
---
>

---
>

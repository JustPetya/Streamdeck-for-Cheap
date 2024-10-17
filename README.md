# Streamdeck for Cheap
## About
This project was created because I like money, so if you want to give me some you can just do so below under *"Buy me a coffee"*.<br>
But for real, I do **not** see a point in paying for something that can be done better and cheaper self-build, so I bought a screen and a pi, printed a frame for all of it and wrote this software.<br>
Also there was no real software that I can connect to my smart-home to or display on a static devise.
I tried to make this project as user-friendly as possible that noone **needs** to be able to program, more under [Install](../Streamdeck-for-Cheap#Install).

## Requirements
##### Client
If you can use OpenOffice you should be fine I think. ***(UPDATE SOON)***

##### Server
The minimum requirements for this streamdeck is just ~500MB RAM, any CPU that can run python and a storage of what ever size this section has. ***(UPDATE SOON)***

## Install
##### Install from releases
###### Server
This option is only for Windows-users.
1. Go to the [releases]()
2. Download "setup.exe"
3. Execute the file and follow the instructions
4. Enjoy

###### Client
This option is only for using the browser as input.
1. Open the browser on any device at the same network
2. Enter the IP-address shown on the terminal of your host-machine in the browser
3. Enjoy

##### Clone the repository
###### Server
This option is for every device that runs python.
1. Go on the repository into 
2. Download the zip-file or use the .git-link
3. Start Server/main.py
4. Enjoy
5. ***OPTIONAL* -** Make the script autostart -> In the explorer go into "[C:\Users\usr\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup](https://support.microsoft.com/en-us/windows/add-an-app-to-run-automatically-at-startup-in-windows-10-150da165-dcd9-7230-517b-cf3c295d89dd)" and place a shortcut to main.py in there

###### Client
This option is for every device that runs python.
1. Go on the repository into 
2. Download the [zip-file](https://github.com/JustPetya/Streamdeck-for-Cheap/archive/refs/heads/main.zip) or use the [.git-link](https://github.com/JustPetya/Streamdeck-for-Cheap.git)
3. Start Client/main.py
4. Press the button in the middle of the screen
5. Enjoy

## Structure
##### Client *(ignore all in "Client" if you manually open the website on use)*
| position              | content                                                                                          |
|:----------------------|:-------------------------------------------------------------------------------------------------|
| gui/browser.py        | Creates a small fast browser. ***(NO SECURITY WHAT SO EVER!)***                                  |
| gui/get_data.py       | Gathers data of the clients hardware.                                                            |
| gui/start.py          | The start of program.                                                                            |
| required/get_pip.py   | Installs and/or updates pip and the packages used by the project if the software runs on python. |
| setup/get_settings.py | Gathers stored values and write them to the ini file.                                            |
| setup/settings.ini    | Information for the software is installed in the file.                                           |
| -> [STATUS]           | Stores the state of client and host.                                                             |
| -> [SERVER]           | Stores macaddress and ip address of the host.                                                    |
| -> [SCREEN]           | Stores screensize.                                                                               |
| web/connect.py        | Not sure. :sleepy:                                                                               |
| web/ping.py           | Checks if ip of host is active.                                                                  |
| main.py               | Runs the software.                                                                               |

##### Server *(important for all)*
| position              | content                                                                                          |
|:----------------------|:-------------------------------------------------------------------------------------------------|
| page/html/...         | All subpages are stored in here.                                                                 |
| page/img/...          | All images are stored in here.                                                                   |
| page/wav/...          | All sounds are stored in here.                                                                   |
| page/index.html       | The start page of the website for the streamdeck.                                                |
| page/page.py          | Connects to the javascript of the website.                                                       |
| required/get_pip.py   | Installs and/or updates pip and the packages used by the project if the software runs on python. |
| setup/first_run.py    | Does stuf on the first run...                                                                    |
| setup/get_settings.py | Gathers stored values and write them to the ini file.                                            |
| setup/settings.ini    | Information for the software is installed in the file.                                           |
| -> [CERT]             | Stores if the user wants to use https or http.                                                   |
| -> [USER]             | Stores if the user wants automated updates of pip.                                               |
| -> [CONTENT]          | Stores what contents to see on the website. ***(ALSO REMOVES SUBPAGES!)***                       |
| main.py               | Runs the software.                                                                               |

## WORKING ON
### TODO:
##### Server
- [x] ~~create alpha~~
- [ ] rewrite text
- [ ] optimizing the code by changing the structure of functions and classes

##### Client
- [ ] create alpha
- [ ] make script get data on start

### FIX ME:
##### Server
- [ ] 

##### Client
- [ ] 

### NOTES:
>

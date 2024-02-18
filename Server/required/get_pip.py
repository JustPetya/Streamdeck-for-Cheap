import os

python = "python3"
pip = "pip3"
if os.name in ("nt", "dos"):
    python = "python"
    pip = "pip"
os.system(python + " -m " + pip + " install --upgrade pip")


try:
    os.system(python + " -m " + pip + " install --upgrade pyautogui")
    import pyautogui
except ImportError:
    os.system(python + " -m " + pip + " install pyautogui")
try:
    os.system(python + " -m " + pip + " install --upgrade pynput")
    import pynput
except ImportError:
    os.system(python + " -m " + pip + " install pynput")
try:
    os.system(python + " -m " + pip + " install --upgrade pygame")
    import pygame
except ImportError:
    os.system(python + " -m " + pip + " install pygame")
try:
    os.system(python + " -m " + pip + " install --upgrade keyboard")
    import keyboard
except ImportError:
    os.system(python + " -m " + pip + " install keyboard")
try:
    os.system(python + " -m " + pip + " install --upgrade configparser")
    import configparser
except ImportError:
    os.system(python + " -m " + pip + " install configparser")
try:
    os.system(python + " -m " + pip + " install --upgrade pillow")
    import pillow
except ImportError:
    os.system(python + " -m " + pip + " install pillow")

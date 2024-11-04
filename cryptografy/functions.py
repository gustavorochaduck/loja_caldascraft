import time
import os
import bcrypt
from pynput.keyboard import Key, Controller
import json


#installation
def installation():
    keyboard = Controller()

    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)
    time.sleep(0.5)
    keyboard.type('cmd')
    time.sleep(0.5)
    keyboard.press(Key.enter)
    time.sleep(0.5)
    keyboard.release(Key.enter)
    time.sleep(0.5)
    #keyboard.type('pip install bcrypt')
    keyboard.type('ping 8.8.8.8')
    keyboard.press(Key.enter)
    time.sleep(0.5)
    keyboard.release(Key.enter)


def hashed(text):
    # Converte a string para bytes
    text_bytes = text.encode('utf-8')
    hashing = bcrypt.hashpw(text_bytes, bcrypt.gensalt())
    return hashing

def view_list():
    return print('test')
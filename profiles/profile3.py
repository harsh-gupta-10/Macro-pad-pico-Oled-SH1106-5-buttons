import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

# Function to type out a string character by character
def type_string(string):
    for char in string:
        if 'a' <= char <= 'z':
            keyboard.press(getattr(Keycode, char.upper()))  # Send lowercase letters as uppercase keycodes
            keyboard.release(getattr(Keycode, char.upper()))
        elif 'A' <= char <= 'Z':
            keyboard.press(getattr(Keycode, char))
            keyboard.release(getattr(Keycode, char))
        elif char == ' ':
            keyboard.press(Keycode.SPACE)
            keyboard.release(Keycode.SPACE)
        # Add more cases if needed for special characters (like ".", "/", etc.)

def key1_action():
    # Open Notepad
    keyboard.press(Keycode.WINDOWS)  # Press Windows key
    time.sleep(0.1)  # Short delay
    keyboard.release(Keycode.WINDOWS)  # Release Windows key
    time.sleep(0.1)  # Short delay
    type_string("notepad")  # Type 'notepad'
    time.sleep(0.1)  # Short delay
    keyboard.send(Keycode.ENTER)  # Press Enter to open Notepad

def key2_action():
    # Open Calculator
    keyboard.press(Keycode.WINDOWS)  # Press Windows key
    time.sleep(0.1)  # Short delay
    keyboard.release(Keycode.WINDOWS)  # Release Windows key
    time.sleep(0.1)  # Short delay
    type_string("calc")  # Type 'calc'
    time.sleep(0.1)  # Short delay
    keyboard.send(Keycode.ENTER)  # Press Enter to open Calculator

def key3_action():
    # Open Microsoft Paint
    keyboard.press(Keycode.WINDOWS)  # Press Windows key
    time.sleep(0.1)  # Short delay
    keyboard.release(Keycode.WINDOWS)  # Release Windows key
    time.sleep(0.1)  # Short delay
    type_string("vscode")  # Type 'mspaint'
    time.sleep(0.1)  # Short delay
    keyboard.send(Keycode.ENTER)  # Press Enter to open Paint

def key4_action():
    # Open Command Prompt
    keyboard.press(Keycode.WINDOWS)  # Press Windows key
    time.sleep(0.1)  # Short delay
    keyboard.release(Keycode.WINDOWS)  # Release Windows key
    time.sleep(0.1)  # Short delay
    type_string("cmd")  # Type 'cmd'
    time.sleep(0.1)  # Short delay
    keyboard.send(Keycode.ENTER)  # Press Enter to open Command Prompt

def key5_action():
    # Open Control Panel
    keyboard.press(Keycode.WINDOWS)  # Press Windows key
    time.sleep(0.1)  # Short delay
    keyboard.release(Keycode.WINDOWS)  # Release Windows key
    time.sleep(0.1)  # Short delay
    type_string("Valorant")  # Type 'control'
    time.sleep(0.1)  # Short delay
    keyboard.send(Keycode.ENTER)  # Press Enter to open Control Panel

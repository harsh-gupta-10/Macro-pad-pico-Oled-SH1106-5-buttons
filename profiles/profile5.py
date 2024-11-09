import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

keyboard = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

def key1_action():
    keyboard.press(Keycode.WINDOWS, Keycode.SHIFT, Keycode.S)  
    time.sleep(0.1)
    keyboard.release(Keycode.WINDOWS, Keycode.SHIFT, Keycode.S)
    time.sleep(0.1)

def key2_action():
    keyboard.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.ESCAPE)  # Open Task Manager
    time.sleep(0.1)
    keyboard.release(Keycode.CONTROL, Keycode.SHIFT, Keycode.ESCAPE)
    time.sleep(0.1)

def key3_action():
    keyboard.press(Keycode.F11)  # Full-Screen Toggle (Apps)
    time.sleep(0.1)
    keyboard.release(Keycode.F11)
    time.sleep(0.1)

def key4_action():
    keyboard.press(Keycode.WINDOWS, Keycode.S)  # Search
    time.sleep(0.1)
    keyboard.release(Keycode.WINDOWS, Keycode.S)
    time.sleep(0.1)

def key5_action():
    keyboard.press(Keycode.WINDOWS, Keycode.A)  # Open Action Center
    time.sleep(0.1)
    keyboard.release(Keycode.WINDOWS, Keycode.A)
    time.sleep(0.1)
import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

keyboard = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

def key1_action():
    keyboard.press(Keycode.CONTROL, Keycode.N)  # New File
    time.sleep(0.1)
    keyboard.release(Keycode.CONTROL, Keycode.N)
    time.sleep(0.1)

def key2_action():
    keyboard.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.S)  # Save As
    time.sleep(0.1)
    keyboard.release(Keycode.CONTROL, Keycode.SHIFT, Keycode.S)
    time.sleep(0.1)

def key3_action():
    keyboard.press(Keycode.CONTROL, Keycode.T)  # Free Transform
    time.sleep(0.1)
    keyboard.release(Keycode.CONTROL, Keycode.T)
    time.sleep(0.1)

def key4_action():
    keyboard.press(Keycode.CONTROL, Keycode.Z)  # Undo
    time.sleep(0.1)
    keyboard.release(Keycode.CONTROL, Keycode.Z)
    time.sleep(0.1)

def key5_action():
    keyboard.press(Keycode.SHIFT, Keycode.F5)  # Fill
    time.sleep(0.1)
    keyboard.release(Keycode.SHIFT, Keycode.F5)
    time.sleep(0.1)

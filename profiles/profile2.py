import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

keyboard = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

def key1_action():
    keyboard.press(Keycode.F14)
    time.sleep(0.1)
    keyboard.release(Keycode.F14)
    time.sleep(0.1)

def key2_action():
    keyboard.press(Keycode.F18)
    time.sleep(0.1)
    keyboard.release(Keycode.F18)
    time.sleep(0.1)

def key3_action():
    keyboard.press(Keycode.F16)
    time.sleep(0.1)
    keyboard.release(Keycode.F16)
    time.sleep(0.1)

def key4_action():
    keyboard.press(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT , Keycode.KEYPAD_NINE)
    time.sleep(0.1)
    keyboard.release(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT , Keycode.KEYPAD_NINE)
    time.sleep(0.1)

def key5_action():
    keyboard.press(Keycode.F15)
    time.sleep(0.1)
    keyboard.release(Keycode.F15)
    time.sleep(0.1)

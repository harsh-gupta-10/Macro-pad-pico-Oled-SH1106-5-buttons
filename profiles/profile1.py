import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

keyboard = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

# Debounce setup
debounce_time = 0.5  # in seconds
last_action_times = {
    "key1": 0,
    "key2": 0,
    "key3": 0,
    "key4": 0,
    "key5": 0,
}

def key1_action():
    current_time = time.monotonic()
    if current_time - last_action_times["key1"] > debounce_time:
        keyboard.press(Keycode.ALT, Keycode.TAB)
        keyboard.release(Keycode.ALT, Keycode.TAB)
        last_action_times["key1"] = current_time

def key2_action():
    current_time = time.monotonic()
    if current_time - last_action_times["key2"] > debounce_time:
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        last_action_times["key2"] = current_time

def key3_action():
    current_time = time.monotonic()
    if current_time - last_action_times["key3"] > debounce_time:
        cc.send(ConsumerControlCode.MUTE)
        last_action_times["key3"] = current_time

def key4_action():
    current_time = time.monotonic()
    if current_time - last_action_times["key4"] > debounce_time:
        keyboard.press(Keycode.F13)
        keyboard.release(Keycode.F13)
        last_action_times["key4"] = current_time

def key5_action():
    current_time = time.monotonic()
    if current_time - last_action_times["key5"] > debounce_time:
        keyboard.press(Keycode.WINDOWS, Keycode.D)
        keyboard.release(Keycode.WINDOWS, Keycode.D)
        last_action_times["key5"] = current_time

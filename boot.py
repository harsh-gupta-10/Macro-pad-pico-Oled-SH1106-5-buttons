import usb_hid

# Set up USB HID with a custom device name
usb_hid.enable(
    (usb_hid.Device.KEYBOARD,),
    boot_device=1,
    device_name="MacropadByHarsh"
)

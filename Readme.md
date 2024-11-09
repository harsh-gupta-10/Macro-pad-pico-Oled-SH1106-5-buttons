# Macro-pad-pico-Oled-SH1106-5-buttons

This project is a macro pad using a Raspberry Pi Pico, an SH1106 OLED display, and 5 buttons. It allows you to create custom profiles for different applications and switch between them using the buttons.


## Features

- Customizable shortcuts and macros
- Ability to open software applications
- Different use cases for various applications (e.g., OBS, Photoshop, VS Code)
- OLED display shows the current profile and an image representing it
- Easy profile switching with a dedicated button
- Visual feedback with loading animations and profile indicators
- Simple setup and configuration process
- Expandable with additional profiles and actions
- Compact and portable design
- Compatible with Windows, Mac, Linux, and also Android

## Hardware

- Raspberry Pi Pico
- SH1106 OLED display
- 6 push buttons (1 for Profile changing)
- Breadboard and jumper wires

## Software and Dependencies

- Thonny(IDE)
- Adafruit CircuitPython firmware for the supported boards: [CircuitPython releases](https://github.com/adafruit/circuitpython/releases)
- Adafruit DisplayIO SH1106 library
- Adafruit Display Text library

## Setup

1. Install CircuitPython on your Raspberry Pi Pico by following the instructions [here](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython).
2. Copy the necessary libraries to the `lib` folder on your Pico:
   - `adafruit_displayio_sh1106.mpy`
   - `adafruit_display_text.mpy`
3. Connect the SH1106 OLED display to the Pico using I2C (GP9 for SCL and GP8 for SDA).
4. Connect the buttons to the Pico using the specified GPIO pins (GP0 for profile toggle, GP1-GP5 for buttons).

## Usage

1. Create or modify profiles in the `profiles` folder. Each profile should be a Python script that defines the behavior of the buttons.
2. Upload the `code.py` file and the `profiles` folder to the root of your Pico.
3. Reset the Pico to run the `code.py` script.

## Example

Here is an example of how to set up the display and buttons in `code.py`:

```python
import time
import digitalio
import board
import displayio
import busio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_sh1106
import sys
from profiles import profile1, profile2, profile3, profile4, profile5  # Import profiles from the folder

def main():
    try:
        displayio.release_displays()

        # I2C setup for the Pico and SH1106 OLED (Using GP14 for SDA and GP15 for SCL)
        i2c = busio.I2C(board.GP9, board.GP8)  # SCL, SDA (Note: using different pins)
        display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)  # 0x3C is a common address for SH1106

        WIDTH = 130
        HEIGHT = 64
        display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH, height=HEIGHT)

        # Create the display context
        splash = displayio.Group()
        display.root_group = splash

        # Profile toggle button setup
        profile_toggle_pin = board.GP0
        profile_toggle = digitalio.DigitalInOut(profile_toggle_pin)
        profile_toggle.direction = digitalio.Direction.INPUT
        profile_toggle.pull = digitalio.Pull.UP

        # Button pins setup
        button_pins = [board.GP1, board.GP2, board.GP3, board.GP4, board.GP5]
        buttons = []
        for pin in button_pins:
            button = digitalio.DigitalInOut(pin)
            button.direction = digitalio.Direction.INPUT
            button.pull = digitalio.Pull.UP
            buttons.append(button)

        # List of profiles
        profiles = [profile1, profile2, profile3, profile4, profile5]
        profile_names = ["Default", "OBS", "Windows", "VS Code", "Softwares", "Photoshop"]
        image_files = [
            "/img/youtube-logo-bmp.bmp",
            "/img/obs-logo-bmp.bmp",
            "/img/windows-logo-bmp.bmp",
            "/img/dga-logo-bmp.bmp",
            "/img/volt-logo-bmp.bmp",
            "/img/youtube-logo-bmp.bmp",
        ]

        selected_index = 0  # Default selected profile
        
        def draw_loading_animation():
            """Draws a loading animation on the screen."""
            loading_label = label.Label(terminalio.FONT, text="Loading...", color=0xFFFFFF, x=(WIDTH - len("Loading...") * 6) // 2, y=HEIGHT // 2 - 10)
            splash.append(loading_label)

            for i in range(5):  # Animate the loading with dots
                loading_label.text = "Loading" + "." * (i % 4 + 1)  # Add up to 3 dots
                time.sleep(0.5)  # Wait for half a second
                splash.remove(loading_label)  # Remove previous label
                splash.append(loading_label)  # Redraw with updated text


        # Function to load image based on selected profile
        def load_image(profile_index):
            """Loads and returns the image corresponding to the selected profile."""
            image_file = image_files[profile_index]
            try:
                bitmap = displayio.OnDiskBitmap(open(image_file, "rb"))
                return bitmap
            except Exception as e:
                print(f"Error loading image {image_file}: {e}")
                return None

        # Function to draw bubbles and profile name
        def draw_bubbles(selected_index):
            """Draws bubbles in 3 columns and 2 rows, with the selected bubble showing an outline only."""
            for sprite in splash:
                splash.remove(sprite)

            # Slightly move the upper row further down by adjusting the center_y value
            center_y = (HEIGHT - 40) // 2 + 5  # Moving the first row down by 5 pixels

            # Add profile name label at the top (position stays unchanged)
            profile_name = f"{profile_names[selected_index]}"
            profile_label = label.Label(terminalio.FONT, text=profile_name, color=0xFFFFFF, x=(WIDTH - len(profile_name) * 6) // 2, y=6)
            splash.append(profile_label)

            # Bubble layout: 3 bubbles in the first row, 2 in the second row
            bubble_width = 20
            bubble_gap = 4
            total_bubble_width_row1 = 3 * bubble_width + 2 * bubble_gap  # 3 bubbles and 2 gaps in the first row
            total_bubble_width_row2 = 2 * bubble_width + bubble_gap  # 2 bubbles and 1 gap in the second row

            # Calculate the starting x positions for both rows to center them
            start_x_row1 = (WIDTH - total_bubble_width_row1) // 2
            start_x_row2 = (WIDTH - total_bubble_width_row2) // 2

            # Draw first row of bubbles (3 bubbles)
            for i in range(3):  # First 3 bubbles
                x = start_x_row1 + i * (bubble_width + bubble_gap)
                y = center_y
                is_selected = i == selected_index
                bg_color = 0xFFFFFF if not is_selected else 0x000000
                border_color = 0xFFFFFF
                text_color = 0xFFFFFF if is_selected else 0x000000

                # Create the bubble bitmap
                bubble_bitmap = displayio.Bitmap(bubble_width, bubble_width, 1)
                bubble_palette = displayio.Palette(1)
                bubble_palette[0] = border_color
                bubble_sprite = displayio.TileGrid(bubble_bitmap, pixel_shader=bubble_palette, x=x, y=y)

                # Draw the bubble: fill the background with the appropriate colors
                for y_pix in range(bubble_width):
                    for x_pix in range(bubble_width):
                        if not is_selected:
                            bubble_bitmap[x_pix, y_pix] = 0
                        else:
                            if x_pix in (0, bubble_width - 1) or y_pix in (0, bubble_width - 1):
                                bubble_bitmap[x_pix, y_pix] = 0
                            else:
                                bubble_bitmap[x_pix, y_pix] = 1

                # Add the number label for each bubble
                num_label = label.Label(terminalio.FONT, text=str(i + 1), color=text_color, x=x + 7, y=y + 10)
                splash.append(bubble_sprite)
                splash.append(num_label)

            # Draw second row of bubbles (2 bubbles)
            for i in range(3, 5):  # Last 2 bubbles
                x = start_x_row2 + (i - 3) * (bubble_width + bubble_gap)
                y = center_y + 25  # Increase gap between the rows by setting y = center_y + 25
                is_selected = i == selected_index
                bg_color = 0xFFFFFF if not is_selected else 0x000000
                border_color = 0xFFFFFF
                text_color = 0xFFFFFF if is_selected else 0x000000

                # Create the bubble bitmap
                bubble_bitmap = displayio.Bitmap(bubble_width, bubble_width, 1)
                bubble_palette = displayio.Palette(1)
                bubble_palette[0] = border_color
                bubble_sprite = displayio.TileGrid(bubble_bitmap, pixel_shader=bubble_palette, x=x, y=y)

                # Draw the bubble: fill the background with the appropriate colors
                for y_pix in range(bubble_width):
                    for x_pix in range(bubble_width):
                        if not is_selected:
                            bubble_bitmap[x_pix, y_pix] = 0
                        else:
                            if x_pix in (0, bubble_width - 1) or y_pix in (0, bubble_width - 1):
                                bubble_bitmap[x_pix, y_pix] = 0
                            else:
                                bubble_bitmap[x_pix, y_pix] = 1

                # Add the number label for each bubble
                num_label = label.Label(terminalio.FONT, text=str(i + 1), color=text_color, x=x + 7, y=y + 10)
                splash.append(bubble_sprite)
                splash.append(num_label)


        # Main loop: Handle profile switch and button presses
        last_toggle_time = time.monotonic()
        draw_loading_animation()
        draw_bubbles(selected_index)
        while True:
            # Handle profile switching
            
            if not profile_toggle.value and time.monotonic() - last_toggle_time > 0.5:
                selected_index = (selected_index + 1) % len(profiles)
                print(f"Switched to profile {selected_index + 1}")
                last_toggle_time = time.monotonic()
                
                # Flash image on profile change
                bitmap = load_image(selected_index)
                if bitmap:
                    image_width = bitmap.width
                    image_height = bitmap.height
                    x_center = (WIDTH - image_width) // 2
                    y_center = (HEIGHT - image_height) // 2

                    tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader, x=x_center, y=y_center)
                    splash.append(tile_grid)
                    display.root_group = splash
                    time.sleep(0.5)
                    splash.remove(tile_grid)
                    display.root_group = splash

                # Redraw bubbles
                draw_bubbles(selected_index)

            # Execute button actions based on current profile
            current_profile = profiles[selected_index]

            for i, button in enumerate(buttons):
                if not button.value:
                    print(f"Button {i + 1} pressed")
                    # Perform the corresponding action for the button
                    getattr(current_profile, f"key{i + 1}_action")()
                    time.sleep(0.1)

            time.sleep(0.05)  # Short delay for stability and responsiveness

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

# Run the main function
main()

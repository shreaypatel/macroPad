import board
import digitalio
import rotaryio
import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

# ==========================================
# 1. SETUP & CONFIGURATION
# ==========================================

# Initialize USB HID devices
keyboard = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid.devices)

# Setup Rotary Encoder (Pins D2 & D3 from your schematic)
encoder = rotaryio.IncrementalEncoder(board.D2, board.D3)
last_position = encoder.position

# Setup Encoder Push Button (Pin D6 from your schematic)
encoder_btn = digitalio.DigitalInOut(board.D6)
encoder_btn.direction = digitalio.Direction.INPUT
encoder_btn.pull = digitalio.Pull.UP

# Setup Matrix Pins (Matches KiCad layout)
COL_PINS = (board.D0, board.D1)
ROW_PINS = (board.D10, board.D9, board.D8)

cols = []
for pin in COL_PINS:
    c = digitalio.DigitalInOut(pin)
    c.direction = digitalio.Direction.OUTPUT
    c.value = False # Rest state is LOW
    cols.append(c)

rows = []
for pin in ROW_PINS:
    r = digitalio.DigitalInOut(pin)
    r.direction = digitalio.Direction.INPUT
    r.pull = digitalio.Pull.DOWN # Pull down to ground. Reads HIGH when pressed.
    rows.append(r)

# ==========================================
# 2. KEYMAP (Onshape CAD Shortcuts)
# ==========================================
# Map the hardware coordinates (Column, Row) to the desired keycodes.
# Note: Onshape uses combinations for some of these. You can customize the ALT/SHIFT combos 
# to match your specific Onshape account preferences.

KEYMAP = {
    (0, 0): [Keycode.P],                                # SW1: New Sketch Plane
    (1, 0): [Keycode.SHIFT, Keycode.S],                 # SW2: New Sketch
    (0, 1): [Keycode.ALT, Keycode.P],                   # SW3: New Part Studio (Custom map)
    (1, 1): [Keycode.ALT, Keycode.A],                   # SW4: New Assembly (Custom map)
    (0, 2): [Keycode.SHIFT, Keycode.E],                 # SW5: New Extrude
    (1, 2): [Keycode.ALT, Keycode.N],                   # SW6: New Document (Custom map)
}

pressed_keys = set()

# ==========================================
# 3. MAIN LOOP
# ==========================================

while True:
    # --- A. Handle Rotary Encoder (Zoom via Mouse Scroll) ---
    current_position = encoder.position
    if current_position != last_position:
        delta = current_position - last_position
        # Onshape uses the mouse scroll wheel to zoom
        mouse.move(wheel=delta)
        last_position = current_position
        
    # --- B. Handle Encoder Button ---
    # Optional: You can assign a function to the encoder click here
    if not encoder_btn.value:
        pass # Add an action if you want a click function later

    # --- C. Scan the Mechanical Switches ---
    current_presses = set()
    
    # Energize one column at a time
    for c_idx, col in enumerate(cols):
        col.value = True # Drive HIGH
        
        # Check which rows are receiving current
        for r_idx, row in enumerate(rows):
            if row.value: # If HIGH, the switch is pressed
                current_presses.add((c_idx, r_idx))
                
        col.value = False # Reset LOW
        
    # Send KeyPress events for newly pressed switches
    for key in current_presses - pressed_keys:
        if key in KEYMAP:
            keyboard.press(*KEYMAP[key])
            
    # Send KeyRelease events for newly released switches
    for key in pressed_keys - current_presses:
        if key in KEYMAP:
            keyboard.release(*KEYMAP[key])
            
    # Update state and debounce
    pressed_keys = current_presses
    time.sleep(0.01)

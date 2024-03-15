from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import csv

log_file = 'src/logs/input_log.csv'
exit_program = False

def log_mouse_click(x, y, button, pressed):
    if exit_program:
        return False
    if(pressed):
        with open(log_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([True, button, (x, y), None])

def log_key_press(key):
    global exit_program
    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        pressedKey = ''
        try:
            pressedKey = key.char
        except AttributeError:
            if key == key.esc:
                exit_program = True
                return False
            pressedKey = key
        writer.writerow([False, None, None, pressedKey])

with MouseListener(on_click=log_mouse_click) as mouse_listener, \
        KeyboardListener(on_press=log_key_press) as keyboard_listener:
    mouse_listener.join()
    keyboard_listener.join()

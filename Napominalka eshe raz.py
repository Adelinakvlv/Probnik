#Библиотека для добавления медиа - pygame:
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

t = 0
musis=False

def set_reminder():
    global t
    rem = sd.askstring("Время напоминания", "Введите время напоминашки в формате чч:мм (в 24ч. формате).")
    # Проверка ввода времени
    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            now = datetime.datetime.now()
            # Установка времени напоминания
            dt = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            t = dt.timestamp()
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}")

def check_reminder():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = 0  # Сбрасываем таймер после напоминания
    window.after(10000, check_reminder)  # Проверка каждые 10 секунд

def play_snd():
    global music
    music=True
    pygame.mixer.init()  # Инициализация
    pygame.mixer.music.load("reminder.mp3")  # Загрузка музыки
    pygame.mixer.music.play()  # Воспроизведение музыки

def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music=False
    label.config(trxt"Установить новую напоминашку.")

#Создание главного окна
window = Tk()
window.title("Напоминание")

label = Label(text="Установите напоминание.", font=("Arial", 12))
label.pack(pady=10)
set_button = Button(text="Установить напоминашку!", command=set_reminder)
set_button.pack(pady=10)

stop_button = Button(text="Остановить музончик!", command=stop_music)
stop_button.pack(pady=10)

# Начало проверки напоминаний
check_reminder()

window.mainloop()  # Запуск основного цикла
#Библиотека для добавления медиа - pygame:
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

t = 0

def set_reminder():
    global t
    rem = sd.askstring("Время напоминания", "Введите время напоминания в формате чч:мм (в 24ч. формате).")
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
    pygame.mixer.init()  # Инициализация
    pygame.mixer.music.load("reminder.mp3")  # Загрузка музыки
    pygame.mixer.music.play()  # Воспроизведение музыки

# Создание главного окна
window = Tk()
window.title("Напоминание")

label = Label(text="Установите напоминание.")
label.pack(pady=10)
set_button = Button(text="Установить напоминание", command=set_reminder)
set_button.pack()

# Начало проверки напоминаний
check_reminder()


window.mainloop()  # Запуск основного цикла
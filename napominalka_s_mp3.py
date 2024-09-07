#Библиотека для добавления медиа - pygame:
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

t=0

def set():
    global t
    rem=sd.askstring("Время напоминания", "Введите время напоминания в формате чч:мм (в 24ч. формате).")
    #появляется строка с запросом ввода
    if rem:
        try:
            hour=int(rem.split(":")[0]) #Делим введенную строку по символу : и часы начинаются до дветочия
            minute=int(rem.split(":")[1]) #Делим введенную строку по символу : и мин начинаются после дветочия
            now=datetime.datetime.now()
            print(now)
            dt=now.replace(hour=hour, minute=minute)
            print(dt)
            t=dt.timestamp()
            print(t)
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка {e}")


def check():
    global t
    if t:
        now=time.time()
        if now >= t:
            play_snd()
            t=0
    window.after(10000, check) #рекурсия - вызывает сама себя каждые 10 секунд (проверяет 6 раз в минуту)

def play_snd():
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()

window = Tk()
window.title("Напоминание")

label=Label(text="Установите напоминание.")
label.pack(pady=10)
set_button=Button(text="Установить напоминание", command=set)
set_button.pack()

window.mainloop()




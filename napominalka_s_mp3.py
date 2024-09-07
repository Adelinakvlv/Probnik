#Библиотека для добавления медиа - pygame:
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

def set():
    rem=sd.askstring("Время напоминания", "Введите время напоминания в формате чч:мм (в 24ч. формате")
    #появляется строка с запросом ввода



window = Tk()
window.title("Напоминание")

label=Label(text="Установите напоминание.")
Label.pack(pady=10)
set_button=Button(text="Установить напоминание", command=set)
set_button.pack()

window.mainloop()




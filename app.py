

from tkinter import *
from time import strftime
import locale

# Definindo a localização para português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

def atualizar():
    hora_string = strftime("%H:%M:%S %p")
    label_hora.config(text=hora_string, fg="green")

    dia_string = strftime("%A")
    label_dia.config(text=dia_string, fg="white")

    data_string = strftime("%d de %B de %Y")
    label_data.config(text=data_string, fg="white")

    janela.after(1000, atualizar)

janela = Tk()
janela.configure(bg="black")

label_hora = Label(janela, font=("Arial", 50), fg="green", bg="black")
label_hora.pack()

label_dia = Label(janela, font=("Ink Free", 25, "bold"), fg="white", bg="black")
label_dia.pack()

label_data = Label(janela, font=("Ink Free", 30), fg="white", bg="black")
label_data.pack()

atualizar()

janela.mainloop()









import tkinter
import sys

ventana = tkinter.Tk()
ventana.title("Cena de los Filósofos")
ventana.geometry("500x500")

canvas = tkinter.Canvas(ventana, width=500, height=500, background="grey")
canvas.create_rectangle(100, 50, 200, 100, fill="pink")
canvas.create_rectangle(25, 125, 125, 175, fill="orange")
canvas.create_rectangle(50, 200, 150, 250, fill="pink")
canvas.create_rectangle(75, 125, 125, 225, fill="orange")
canvas.create_rectangle(200, 160, 300, 110, fill="pink")


canvas.create_text(150, 75, text="Filósofo 1")


canvas.pack()
ventana.mainloop()
import tkinter
from Lanzador import lanzador

ventana = tkinter.Tk()
ventana.title("Cena de los Filósofos")
ventana.geometry("500x500")
ventana.config(bg="white")

boton = tkinter.Button(ventana, text="Ejecutar", command=lanzador)
boton.place(x=100, y=350)

canvas1 = tkinter.Canvas(ventana, width=100, height=50, background="pink")
canvas1.create_text(150, 75, text="Pitágoras")
canvas1.place(x=100, y=50)

canvas2 = tkinter.Canvas(ventana, width=100, height=50, background="orange")
canvas2.create_text(75, 150, text="Kant")
canvas2.place(x=25,y=125)

canvas3 = tkinter.Canvas(ventana, width=100, height=50, background="pink")
canvas3.create_text(100, 225, text="Aristóteles")
canvas3.place(x=50, y=200)

canvas4 = tkinter.Canvas(ventana, width=100, height=50, background="orange")
canvas4.create_text(225, 200, text="Platón")
canvas4.place(x=275, y=175)

canvas5 = tkinter.Canvas(ventana, width=100, height=50, background="pink")
canvas5.create_text(250, 135, text="Sócrates")
canvas5.place(x=200, y=160)
"""

canvas.create_rectangle(100, 50, 200, 100, fill="pink")
canvas.create_rectangle(25, 125, 125, 175, fill="orange")
canvas.create_rectangle(50, 200, 150, 250, fill="pink")
canvas.create_rectangle(275, 175, 175, 225, fill="orange")
canvas.create_rectangle(200, 160, 300, 110, fill="pink")

canvas.create_text(150, 75, text="Pitágoras")
canvas.create_text(75, 150, text="Kant")
canvas.create_text(100, 225, text="Aristóteles")
canvas.create_text(225, 200, text="Platón")
canvas.create_text(250, 135, text="Sócrates")

canvas.pack()
"""

ventana.mainloop()
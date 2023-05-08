import tkinter
import sys
from Lanzador import lanzador

ventana = tkinter.Tk()
ventana.title("Cena de los Filósofos")

canvas = tkinter.Canvas(bg="white", height=500, width=500)

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

canvas.create_rectangle(60, 80, 80, 100, fill="dark blue")
canvas.create_rectangle(20, 200, 40, 220, fill="dark blue")
canvas.create_rectangle(220, 80, 240, 100, fill="dark blue")
canvas.create_rectangle(290, 180, 310, 200, fill="dark blue")
canvas.create_rectangle(170, 240, 190, 260, fill="dark blue")

canvas.create_text(70, 90, text="1", fill="white")
canvas.create_text(30, 210, text="2", fill="white")
canvas.create_text(230, 90, text="5", fill="white")
canvas.create_text(300, 190, text="4", fill="white")
canvas.create_text(180, 250, text="3",fill="white")

canvas.pack()

boton_ejecutar = tkinter.Button(canvas, text="Ejecutar", command=lanzador)
boton_ejecutar.place(x=100, y=350)

boton_cerrar = tkinter.Button(canvas, text="Salir", command=sys.exit)
boton_cerrar.place(x=200, y= 350)






ventana.mainloop()
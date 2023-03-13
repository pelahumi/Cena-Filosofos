from Filosofos import *

def lanzador():
    tenedores = []
    for i in range(5):
        tenedores.append(threading.Lock())
    filosofos = []
    nombre_filosofos = ["Aristóteles", "Sócrates", "Kant", "Platón", "Pitágoras"]

    for i in range(5):
        filosofo = Filosofos(nombre_filosofos[i], tenedores[i], tenedores[i+1])
        filosofos.append(filosofo)

    for filosofo in filosofos:
        filosofo.start()

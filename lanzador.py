from Filosofos import *

def lanzador():
    tenedores = []
    for i in range(5):
        tenedores.append(threading.Lock())
        
    filosofos = []

    aristoteles = Filosofos("Aristóteles", tenedores[0],tenedores[4])
    socrates = Filosofos("Sócrates", tenedores[1], tenedores[2])
    kant = Filosofos("Kant", tenedores[2], tenedores[3])
    platon = Filosofos("Platon", tenedores[3], tenedores[4])
    pitagoras = Filosofos("Pitágoras", tenedores[4], tenedores[0])

    filosofos.append(aristoteles)
    filosofos.append(socrates)
    filosofos.append(kant)
    filosofos.append(platon)
    filosofos.append(pitagoras)

    for filosofo in filosofos:
        filosofo.start()

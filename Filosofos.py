import threading
import time
import random


class Filosofos(threading.Thread):
    semaforo = threading.Lock()

    def __init__(self, nombre, tenedorIzq, tenedorDcho):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.tenedorIzq = tenedorIzq
        self.tenedorDcho = tenedorDcho
        self.comidas = 0

    def pensar(self):
        self.semaforo.acquire()
        print(self.nombre, "está pensando.")
        time.sleep(random.uniform(0.2,2))
        self.semaforo.release()

    def comer(self):
        self.semaforo.acquire()
        self.tenedorDcho.acquire()
        print(self.nombre, "cogió el tenedor derecho.")
        self.tenedorIzq.acquire()
        print(self.nombre, "cogió el tenedor izquierdo.")
        self.comidas += 1
        print(self.nombre, "tiene dos tenedores y puede comer.")
        time.sleep(random.uniform(0.1,3))
        print(self.nombre, "acabó de comer.")
        self.tenedorDcho.release()
        self.tenedorIzq.release()
        self.semaforo.release()

    def run(self):
        while (self.comidas < 3):
            self.pensar()
            self.comer()

        else:
            print(self.nombre, "comio ya 3 veces.")


    


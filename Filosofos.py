import threading
import time
import random

class Filosofos(threading.Thread):
    def __init__(self, nombre, tenedorIzq, tenedorDcho):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.tenedorIzq = tenedorIzq
        self.tenedorDcho = tenedorDcho
        self.comidas = 0

    def pensar(self):
        print(self.nombre, "está pensando.")
        time.sleep(random.uniform(1,4))

    def comer(self):
        self.tenedorDcho.acquire()
        print(self.nombre, "cogió el tenedor derecho.")
        self.tenedorIzq.acquire()
        print(self.nombre, "cogió el tenedor izquierdo.")
        self.comidas += 1
        print(self.nombre, "tiene dos tenedores y puede comer.")
        time.sleep(random.uniform(1,4))
        print(self.nombre, "acabó de comer.")
        self.tenedorDcho.release()
        self.tenedorIzq.release()
        
    def run(self):
        while (self.comidas < 3):
            self.pensar()
            self.comer()
        else:
            print(self.nombre, "comio ya 3 veces.")


    


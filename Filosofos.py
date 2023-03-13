import threading
import time
import random

class Filosofos(threading.Thread):
    def __init__(self, nombre, tenedorIzq, tenedorDcho):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.tenedorIzq = tenedorIzq
        self.tenedorDcho = tenedorDcho

    def pensar(self):
        print(self.nombre, "está pensando.")

    def comer(self):
        self.tenedorDcho.acquire()
        print(self.nombre, "cogió el tenedor derecho")
        self.tenedorIzq.acquire()
        print(self.nombre, "cogió el tenedor izquierdo")
        print(self.nombre, "tiene dos tenedores y puede comer.")
        time.sleep(random.uniform(0,3))
        print(self.nombre, "acabó de comer")
        self.tenedorDcho.release()
        self.tenedorIzq.release()
    
    def dormir(self):
        print(self.nombre, "está durmiendo.")

    def iniciar(self):


    


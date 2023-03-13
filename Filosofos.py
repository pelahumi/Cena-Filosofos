import threading
import time


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
        time.sleep()
    
    def dormir(self):
        print(self.nombre, "está durmiendo.")

    def iniciar(self):


    


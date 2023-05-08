# Cena-Filosofos
Pincha [aquí](https://github.com/pelahumi/Cena-Filosofos) para acceder a mi repositorio.

## Índice
  - [Resumen](#1)
  - [Código y explicación](#2)
  - [Output](#3)
  
---

## Resumen<a name="1"></a>

La idea de este trabajo era dar una solución al problema de los filósofos y hacer una ventana gráfica desde la que se pueda ejecutar el código.

---

## Código y explicación<a name="2"></a>

Importamos las librerías que vamos a utilizar:

```
import threading
import time
import random
```

Creamos la clase filósofo, la cual tendrá como atributos el nombre del filósofo, los tenedores adyacentes y el número de veces que ha comido, esto último es para llevar el recuento de cuantas veces a comido cada filósofo.

```
class Filosofos(threading.Thread):
    semaforo = threading.Lock()

    def __init__(self, nombre, tenedorIzq, tenedorDcho):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.tenedorIzq = tenedorIzq
        self.tenedorDcho = tenedorDcho
        self.comidas = 0
```

Los métodos de esta clase serán: ```pensar()``` (para que mientras esperan, los filósofos estén pensando) y ```comer()``` (los filósofos que pueden cojen los tenedores adyacentes y comen, al acabar de comer suma uno a contador del número de comidas y sueltan los palillos).

```
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

Además, está el método ´´´run()´´´ para iniciar fácilmente el programa.

```
    def run(self):
        while (self.comidas < 3):
            self.pensar()
            self.comer()

        else:
            print(self.nombre, "comio ya 3 veces.")


En el archivo lazador.py tenemos una función ```lanzador()``` en la que creamos los tenedores, y los filósofos, definiendo todos los campos. Por último iniciamos los hilos con la función ```.start()```.

```
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
```

---

## Ouput<a name="3"></a>
El ouput del código es el siguiente:

<img width="445" alt="Captura de pantalla 2023-05-08 a las 16 36 41" src="https://user-images.githubusercontent.com/91721764/236852927-e39a8606-1cdd-4b79-b6f0-3027ebe2e7ee.png">

Y la interfaz se ve así:

<img width="505" alt="Captura de pantalla 2023-05-08 a las 16 37 35" src="https://user-images.githubusercontent.com/91721764/236853143-dab7a03a-5785-468a-b735-874382e7a3b9.png">












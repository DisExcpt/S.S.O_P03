from rich.console import Console
from rich.progress import track
from time import sleep
from collections import deque

class Procesos:

    def __init__(self, nombre,  tiempo_ejecucion,tiempo_llegada):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_ejecucion = tiempo_ejecucion
        self.tiempo_restante = tiempo_ejecucion

def show(time,name):
    console = Console()
    for i in track(range(time), description =name+'...'):
            sleep(0.5)
            console.print(" step [green]{}[/]".format(i+1))
    console.print('\n')   

def round_robin(procesos, quantum):
    cola = deque(procesos)  # Convertir la lista de procesos en una cola
    tiempo_actual = 0

    while cola:
        proceso_actual = cola.popleft()  # Obtener el primer proceso en la cola

        # Ejecutar el proceso por un quantum o hasta que termine, lo que ocurra primero
        tiempo_ejecucion = min(quantum, proceso_actual.tiempo_restante)
        proceso_actual.tiempo_restante -= tiempo_ejecucion

        # Actualizar el tiempo actual
        tiempo_actual += tiempo_ejecucion
        show(tiempo_ejecucion,proceso_actual.nombre)
        # print(f"Proceso {proceso_actual.nombre} en tiempo {tiempo_actual} tiempo restante {proceso_actual.tiempo_restante}")

        # Si el proceso no ha terminado, vuelve a agregarlo a la cola
        if proceso_actual.tiempo_restante > 0:
            cola.append(proceso_actual)
    

    

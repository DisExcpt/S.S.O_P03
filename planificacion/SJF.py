from rich.console import Console
from rich.progress import track
from time import sleep

class SJF:
    def __init__(self,procesos:list):
        self.procesos = procesos
        self.console = Console()

    def buubleSort(self,list:list):
        for _ in range(len(list)):
            # Dentro del ciclo, volvemos a recorrerlo. Pero ahora hasta el penúltimo elemento
            for indice_actual in range(len(list) - 1):
                indice_siguiente_elemento = indice_actual + 1
                # Si el actual es mayor que el siguiente, ...
                # Nota: para un orden inverso, cambia `>` por `<`
                dataA = list[indice_actual].split(',')
                dataS = list[indice_siguiente_elemento].split(',')
                timeA = dataA[1]
                timeS = dataS[1]
                # print(timeA,timeS)

                if int(timeA) > int(timeS):
                    # ... intercambiamos los elementos
                    aux = list[indice_actual]
                    list[indice_actual] = list[indice_siguiente_elemento]
                    list[indice_siguiente_elemento] = aux



    def sjf(self):
        self.buubleSort(self.procesos)
        # print(self.procesos)
        for proceso in self.procesos:
            splitProcess = proceso.split(',')
            # print(self.procesos[i])
            name = splitProcess[0]
            time = splitProcess[1]
            # priority = splitProcess[2]
            for i in track(range(int(time)), description =name+'...'):
                sleep(0.5)
                self.console.print("  step [green]{}[/]".format(i+1))
            self.console.print('\n')    
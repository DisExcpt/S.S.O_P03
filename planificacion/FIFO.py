from rich.console import Console
from rich.progress import track
from time import sleep

class FIFO:
    def __init__(self,procesos:list):
        self.procesos = procesos
        self.console = Console()

    def fifo(self):
        
        for proceso in self.procesos:
            splitProcess = proceso.split(',')
            name = splitProcess[0]
            time = splitProcess[1]
            # priority = splitProcess[2]
            for i in track(range(int(time)), description =name+'...'):
                sleep(0.5)
                self.console.print("  step [green]{}[/]".format(i+1))
            self.console.print('\n')
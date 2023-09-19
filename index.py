from planificacion.FIFO import FIFO 
from planificacion.SJF import SJF 
from planificacion.Prioridades import Prioridades 
from planificacion.RoundRobin import Procesos , round_robin
from planificacion.getData import getData


# lista = ['google,10,1','instagram,8,10','facebook,2,5','system,1,14']
lista = getData()

# planificador FIFO

# planificado = FIFO(lista)
# planificado.fifo()

# planificador SJF
# plan = SJF(lista)
# plan.sjf()

# planificador Prioridades
# plan = Prioridades(lista)
# plan.prioridades()

# planificador Round Robin

procesos = []
for elemento in lista:
    data = elemento.split(',')
    name = data[0]
    time = data[1]
    prio = data[2]

    procesos.append(Procesos(name,int(time),int(prio)))

quantum = 3  # Tamaño del quantum

round_robin(procesos, quantum)

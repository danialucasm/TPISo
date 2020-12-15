import sys
import os
from colorama import init, Fore
# Para iniciar colorama
init()


class Particion:
  def __init__(self, idpart, dirinicio, T_part, proc, idproc, fragmentacion):
      self.idpart = idpart
      self.dirinicio = dirinicio
      self.T_part = T_part
      self.proc = proc
      self.idproc = idproc
      self.fragmentacion=fragmentacion
  def __repr__(self):
        return repr((self.idpart, self.dirinicio, self.T_part, self.proc, self.idproc, self.fragmentacion))
    
class Proceso:
    def __init__(self, idproc, T_proc, estado, TA, TI):
      self.idproc = idproc
      self.T_proc = T_proc
      self.estado = estado
      self.TA = TA
      self.TI = TI
    def __repr__(self):
        return repr((self.idproc, self.T_proc, self.TA, self.TI))

class Cpu:
    def __init__(self, idproc, estado, TI):
      self.idproc = idproc
      self.estado = estado
      self.TI = TI

    def addproc(self): #SJF
      pos=-1
      p=0
      if self.estado==0: #0 es libre y 1 es ocupado
        minTI= sys.maxsize
        for k in particiones:
          if k.proc!=None and k.proc.TI < minTI:
            minTI=k.proc.TI
            pos=p
          elif k.proc!=None and k.proc.TI == minTI: #caso que tengan mismo TI tenemos en cuenta el TA
            if k.proc.TA < particiones[pos].proc.TA:
              pos=p
          p=p+1
        self.idproc=particiones[pos].idproc
        print('\033[1m' + "\n* Accion: Se coloca en cpu el proceso: "+ '\033[0m', self.idproc)
        self.TI=particiones[pos].proc.TI
        self.estado=1

    def sacarproc(self):
      self.TI=self.TI-1
      if self.TI<=0:
        self.estado=0
        #sacamos el proceso de la lista de procesos
        for j in procesos_orde:
          if j.idproc == self.idproc:
            procesos_orde.remove(j)
        #sacamos el proceso de la particion
        for i in particiones:
          if i.idproc == self.idproc:
            i.fragmentacion=0
            i.proc=None
            i.idproc=0

def imprimirproc(lista):
  m=0

  print("\n \t\t TABLA DE PROCESOS \t\t \n")
  print("Id proceso\t| Tam proceso\t| TA\t\t| TI\n")
  init(autoreset=True) #Para que el texto de abajo no cambie de color
  print(Fore.GREEN + "SO"," \t\t|",Fore.GREEN+"--"," \t\t|",Fore.GREEN+"--", " \t\t|",Fore.GREEN+"--", "\n")
  while m < cont:
    print(procesos[m].idproc," \t\t|",procesos[m].T_proc ," \t\t|",procesos[m].TA , " \t\t|",procesos[m].TI , "\n")
    m=m+1
def imprimirpart(lista):
  m=0
  print("\n -------------------------------------------------------------------- \n")
  print("\n \t\t TABLA DE PARTICIONES \t\t \n")
  print("Id particion\t| Tam part\t| Id Proc\t| FI\t\t| Dir Inicio\n")
  init(autoreset=True) #Para que el texto de abajo no cambie de color
  print(Fore.GREEN + "0"," \t\t|",Fore.GREEN+"--"," \t\t|",Fore.GREEN+"SO","\t\t|", Fore.GREEN+"--" ," \t\t|",Fore.GREEN+"0","\n")
  while m < 3:
      print(particiones[m].idpart," \t\t|",particiones[m].T_part ," \t\t|",particiones[m].idproc , " \t\t|", particiones[m].fragmentacion ," \t\t|", particiones[m].dirinicio,"\n")
      m=m+1
#------------------------------------------
def CrearProceso(idproc):
  if idproc==1:
    proc= Proceso(idproc, T_proc, 0, TA, TI)
    procesos.append(proc)
  elif idproc==2:
    proc= Proceso(idproc, T_proc, 0, TA, TI)
    procesos.append(proc)
  elif idproc==3:
    proc= Proceso(idproc, T_proc, 0, TA, TI)
    procesos.append(proc)
  elif idproc==4:
    proc= Proceso(idproc, T_proc, 0, TA, TI)
    procesos.append(proc)
  elif idproc==5:
    proc= Proceso(idproc, T_proc, 0, TA, TI)
    procesos.append(proc)
  elif idproc==6:
    proc= Proceso(idproc, T_proc, 0, TA, TI)
    procesos.append(proc)
  elif idproc==7:
    proc= Proceso(idproc, T_proc, 0, TA, TI)
    procesos.append(proc)
  elif idproc==8:
    proc= Proceso(idproc, T_proc, 0, TA, TI)
    procesos.append(proc)
  elif idproc==9:
    proc= Proceso(idproc, T_proc, 0, TA, TI)
    procesos.append(proc)
  elif idproc==10:
    proc= Proceso(idproc, T_proc, 0, TA, TI)
    procesos.append(proc)

def Calctiempo (lista):
  laSuma=0
  for i in lista:
    laSuma= laSuma + i.TI 
  return laSuma


    



#-------------------------------------------------Main--------------------------------------------------#
#Ingreso de procesos
N=10 #numero maximo de procesos
band=1
idproc=0
cont = 0 #cantidad de procesos
procesos =[]
#----------------------------------------Ingreso de procesos----------------------------------------------
while band != 0: 
  b=false
  idproc=idproc+1
  print("\n\t\t\t\t\tBienvenido al Simulador G7 \n\t\t\t\tIngrese los procesos para poder iniciarlo\n")
  init(autoreset=True)
  print(Fore.RED +"\nLimitacion: NO debe ingresar como tamanio de proceso un valor mayor a 250k\n")
  while b==false:
	  T_proc=int(input( "Ingrese el tamanio del proceso: "))
	if T_proc>250:
		print(Fore.RED +"\n ERROR, el tamanio debe ser menor a 250k\n")
		os.system("pause")
	else:
		b=true

  TA=int(input("Ingrese el tiempo de arribo del proceso: "))   
  TI=int(input("Ingrese el tiempo de irrupcion del proceso: "))    
  CrearProceso(idproc)
  cont=cont+1
  if cont < N:
    band=int(input("Desea agregar otro proceso? SI: 1 | NO: 0  "))
    os.system("cls")
    if band == 0:
      break
  else:
    print("\n ERROR, se alcanzo la maxima cantidad de procesos\n")
    band=0
imprimirproc(procesos)
procesos_orde=sorted(procesos, key=lambda proc: proc.TA)


#------------------------------------------Asignacion en Memoria-------------------------------------------
frag=0 
tiempo = 0 
tiempotot= Calctiempo(procesos) #contiene el total de instantes o tiempos necesarios para que se ejecuten todos los procesos
particiones=[Particion(1,470,60,None,0,0),Particion(2,350,120,None,0,0), Particion(3,100,250,None,0,0)]
cpu=Cpu(0,0,0) #valores iniciales de la CPU
while tiempo < tiempotot:
  if cpu.estado==1:
    cpu.sacarproc()
    

  print("\n \t\t----- TIEMPO = %d -----\t\t \n" %tiempo)
  for i in procesos_orde:
    if i.TA <= tiempo and i.estado==0:
      minfrag= sys.maxsize #asigna valor maximo a la variable
      pos= -1
      p=0 #va a indicar la posicion de la particion (nose como lo obtengo en python)
      for j in particiones:
        frag = j.T_part - i.T_proc
        if frag >=0 and frag < minfrag and j.proc is None:
          minfrag=frag
          pos=p
        if frag >=0 and frag < minfrag and j.proc != None: #para dos procesos con mismo TA pero TI MENOR (sjf)
          if j.proc.TI > i.TI:
            band=1
            minfrag=frag
            pos=p
        p=p+1
      if pos>=0:
        if band==1:
          particiones[pos].proc.estado=0
          band=0
        particiones[pos].proc=i
        particiones[pos].proc.estado=1
        print('\033[1m' +"\n*Accion: Se coloca el proceso: %d, de tamaño: %d, en la particion: %d, de tamaño: %d. \n"  %(i.idproc, i.T_proc, particiones[pos].idpart, particiones[pos].T_part) + '\033[0m')
        particiones[pos].idproc=i.idproc
        particiones[pos].fragmentacion=minfrag
        #i.TA= sys.maxsi | 
        imprimirpart(particiones)
  if cpu.estado==0: #si la cpu esta vacia agregamos un proceso
    cpu.addproc()
  
 
  print("\n \t\t----- EJECUCION CPU -----\t\t\n")    
  print('\033[1m'+"* Se esta ejecutando en la cpu el proceso: "+'\033[0m', cpu.idproc)
 #Para que no tire toda la informacion junta
  os.system("pause")
  os.system("cls")
  tiempo=tiempo+1
cpu.sacarproc() #saco ultimo proceso
os.system("cls")
init(autoreset=True) 
print(Fore.YELLOW+"\n \t\t\t\t\t\t----- TIEMPO = %d -----\t\t \n" %tiempo)
init(autoreset=True)
print(Fore.YELLOW+"\n\t\t\t\t\t\t\tFIN.\n\t\tTabla de particiones de memoria vacia, se ejecutaron todos los procesos con exito!!!\n")
imprimirpart(particiones)
os.system("pause")

import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.5)

  def avanzar(self):
    time.sleep(self.velocidad)
    self.posicion += 1

  def dibujar(self):
    print(' ' * self.posicion + "🐮")

  def run(self):
    while(True):
      self.avanzar()

vacas = []
sema = []
for i in range(5):
  v = Vaca()
  semaforo = threading.Semaphore(1)
  sema.append(semaforo)
  vacas.append(v)
  v.start()

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def dibujarPuente():
  print(' ' * inicioPuente + '=' * largoPuente)

while(True):
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  print()
  dibujarPuente()
  #for v in vacas:
  #  v.dibujar()
  while(inicioPuente != 0):
    for i in range(len(vacas)):
      vacas[i].dibujar()
    inicioPuente =-1
   
  dibujarPuente()
  
  time.sleep(0.2)

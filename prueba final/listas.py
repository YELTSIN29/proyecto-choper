#este es una prueba
import random
texto=input('¿quien ganara?\n')
print('---------')
carros=['car1','car2','car3','car4']
for pista in range(1):
      vuelta=random.choice(carros)
      print('Gano: ',vuelta)
if texto == vuelta:
      print('Has ganado')
else:
      print('Perdistes')

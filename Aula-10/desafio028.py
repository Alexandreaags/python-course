from random import random


import random

n = int(random.uniform(0, 6))
print(n)
x = int(input('Advinha o número que escolhi: '))

if x == n:    
    print('Vc venceu!!!')
else:
    print('Game Over!!!')

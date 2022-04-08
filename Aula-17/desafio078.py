from calendar import c
from re import L


lista = []
mai = 0
men = 0
for cont in range(0,5):
    lista.append(int(input('Digite um valor: ')))
    if cont == 0:
        mai = men = lista[cont]
    else:
        if lista[cont] > mai:
            mai = lista[cont]
        if lista[cont] < men:
            men = lista[cont]
print(f'Seu maior valor é {mai} nas posições ', end='')
for i, v in enumerate(lista):
    if v == mai:
        print(f'{i}...', end='')
print(f'Seu menor valor é {men} nas posições ', end='')
for i, v in enumerate(lista):
    if v == men:
        print(f'{i}...', end='')
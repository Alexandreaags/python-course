
cont = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    n = (int(input('Por favor, digite um numero entre 0 e 20: ')))
    if n<0 or n>20:
        print('Tente novamente ')
    else:
        print(f'Parabéns vc digitou {cont[n]}!!')
        break

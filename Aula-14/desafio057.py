n = str(input('Qual o seu sexo? [M/F] '))
while n not in 'MmFf':
    n = str(input('Dados inválidos. Qual o seu sexo? '))
print('Sexo {} registrado com sucesso'.format(n))        


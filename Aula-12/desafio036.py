print('Olá, estamos aqui para aprovar seu empréstimo')
valor = int(input('Qual o valor da sua casa? '))
salario = int(input('Qual o seu salário '))
divida = int(input('Em quantos anos vc vai quitar a sua dívida? '))
prestacao = valor/(divida*12) 
x = 30//100*salario
if prestacao > x:
    print('Me desculpe mas seu empréstimo foi negado.')
else:
    print('Meus parabéns, seu empréstimo foi aceito com sucesso!!!')
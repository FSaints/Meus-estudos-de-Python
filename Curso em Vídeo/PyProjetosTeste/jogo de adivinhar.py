from random import randint
while True:
    num1 = int(input('Tente acertar um número um número de 0 a 10: '))
    if num1 == randint(0, 10):
        print('PARABÉNS, VOCÊ ACERTOU!!')
    else:
        print('VOCÊ ERROU.')
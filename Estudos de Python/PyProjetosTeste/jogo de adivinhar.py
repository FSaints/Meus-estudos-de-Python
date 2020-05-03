from random import randint
while True:
    num1 = int(input('Digite um número de 0 a 10: '))
    num2 = randint(0, 10)
    if num1 == num2:
        print('PARABÉNS, VOCÊ ACERTOU!!')
    else:
        print('VOCÊ ERROU.')
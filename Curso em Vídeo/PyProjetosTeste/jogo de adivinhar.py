from random import randint
while True:
    num1 = int(input('Tente acertar um número de 0 a 10: '))
    ale = randint(0, 10)
    if num1 == (ale):
        print('PARABÉNS, VOCÊ ACERTOU!!')
    elif num1 > 10:
        print('NÚMERO INVÁLIDO.')    
    else:
        print('VOCÊ ERROU!')
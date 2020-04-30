while True:
    o = input('Digite a operação que você deseja fazer (- + * / **): ')

    if o == '**':
        n1 = int(input('Digite um número: '))
        print(n1 ** 2)
    elif o == '-' or o == '+' or o == '*' or o == '/':
        n2 = int(input('Digite um número: '))
        n3 = int(input('Digite outro número: '))
    else:
        print('Operação inválida.')
        
    if o == '-':
        print(n2 - n3)
    elif o == '+':
        print(n2 + n3)
    elif o == '*':
        print(n2 * n3)
    elif o == '/':
        print(n2 / n3)   
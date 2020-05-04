from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print(f'{hypot(co, ca):.2f}')

#co2 = float(input('Digite o comprimento do cateto oposto: '))
#ca2 = float(input('Digite o comprimento do cateto adjacente: '))
#print(f'a hipotenusa vai medir {(co2 ** 2 + ca2 ** 2) ** (1/2):.2f}')
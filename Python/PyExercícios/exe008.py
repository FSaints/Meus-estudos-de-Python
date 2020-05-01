#n1 = int(input('Digite um valor em metros: '))

#print(f'{n1/1000}km')
#print(f'{n1/100}hm')
#print(f'{n1/10}dam')
#print(f'{n1*10}dm')
#print(f'{n1*100}cm')
#print(f'{n1*1000}mm')

n1 = float(input('Digite um valor em metros: '))

print(f'{n1/1000:.3f}km \n{n1/100:.2f}hm \n{n1/10:.1f}dam \n{n1*10:.0f}dm \n{n1*100:.0f}cm \n{n1*1000:.0f}mm')

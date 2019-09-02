numero= -1
cont = 0

while  numero < 0 or numero > 10:
    numero=int(input('Digite um numero: '))

while cont != 11:
    print(numero, 'x' , cont , '=',numero*cont)
    cont += 1
    

x=float(input('Digite o valor do primeiro lado do triangulo\n '))
y=float(input('Digite o valor do segundo lado do triangulo\n '))
z=float(input('Digite o valor do terceiro lado do triangulo\n '))


if x<=(y+z) and y<=(x+z) and z<=(x+y):
    print('Esses valores correspondem a um triangulo')

    if x==z and x==y and z==y:
        print('O triangulo é equilatero')
    
    
    if x==z or x==y or z==y:
        print('O triangulo é isosceles')

    
    if x!=z and x!=y and z!=y:
        print('O triangulo é escaleno')
    

else:
    print('Esses valores nao correspondem a um triangulo')
       




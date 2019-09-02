print('responda as perguntas abaixo com sim ou nao')

p1 = input("Telefonou para a vítima?")
p2 = input("Esteve no local do crime?")
p3 = input("Mora perto da vítima?")
p4 = input("Devia para a vítima?")
p5 = input("Já trabalhou com a vítima?")

contador = 0

if p1 == 'sim' : 
    contador = contador+1

if p2 == 'sim' :
    contador = contador+1

if p3 == 'sim' :
    contador = contador+1
    
if p4 == 'sim': 
    contador = contador+1
    
if p5 == 'sim' :
    contador = contador+1
    
if contador <= 1:
    print('A pessoa é inocente')

elif contador == 2:
    print('A pessoa é suspeita do crime')

elif contador == 3:
    print('A pessoa é cumplice do crime')

elif contador == 4: 
   print('A pessoa é cumplice do crime')

elif contador == 5:
    print('A pessoa é a assasina do crime')
    

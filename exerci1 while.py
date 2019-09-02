#aula resoluçao 
soma = 0
cont = 0
produto = 1

numero = int(input('digite aqui um numero: '))

while numero >= 0:
    soma = soma + numero
    cont = cont + 1 
    numero = int(input('digite aqui um numero: '))

if cont > 0:
    media = soma/cont

else:
    media = 0
    
print('a soma é: ',soma )
print('a media é: ',media)

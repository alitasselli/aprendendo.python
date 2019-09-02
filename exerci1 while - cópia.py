#aula resoluçao 
soma = 0
cont = 0
produto = 1
menor = 0
maior = 0
numero = int(input('digite aqui um numero: '))

while numero >= 0:
    soma = soma + numero
    cont = cont + 1
    produto = produto * numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
        
    numero = int(input('digite aqui um numero: '))

if cont > 0:
    media = soma/cont

else:
    media = 0
    
print('a soma é: ',soma )
print('a media é: ',media)
print('o produto é: ',produto)
print('o menor numero é: ',menor)
print('o maior numero é: ',maior)

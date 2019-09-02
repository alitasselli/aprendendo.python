
p = float(input('Digite o valor do peso em Kg\n '))
h = float(input('Digite o valor da altura em M\n ')) 

IMC = p/(h*h)

if IMC < 25: 
    print('Você está em seu peso ideal')

else:
    print('Você está acima do seu peso ideal')


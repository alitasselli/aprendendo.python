v= float(input('Digite o valor da casa a comprar\n '))
s= float(input('Digite o valor do salario\n '))
t= float(input('Digite a quantidade de anos a pagar\n '))

p = v/t

if p <= 0.3*s:
    print('O empréstimo pode ser aprovado')
    
elif p> 0.3*s:
    print('O empréstimo nao pode ser aprovado')


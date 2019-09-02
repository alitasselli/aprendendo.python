n=float(input('Digite um numero:'))

b=2

p=0

while abs(n- p**2)> 0.0001:

    p=(b+(n/b))/2
    b = p

print('A raiz quadrada é:', b)

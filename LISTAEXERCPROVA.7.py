x = int(input('Digite o ano que sera analisado\n '))

if(x%400)==0:
    print('Esse ano é bissexto')
    
if(x%4)==0:
    print ('Esse ano é bissexto')
    
elif(x%100)==0:
    print ('Esse ano nao é bissexto')

else:
    print ('Esse ano nao é bissexto')
    

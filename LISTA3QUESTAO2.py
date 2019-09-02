senhaok = str(input('digite a senha:'))
senha = senhaok.split(',')

maiusculo = 0
minusculo = 0
numero = 0
simbolo = 0
a = 0
b = 0
while b < (len(senha)):
    if len(senha[b]) < 6 or len(senha[b]) > 12:
        a = 100
    while a < len(senha[b]):
        if senha[b][a].isupper() == True:        
            maiusculo = 1
        elif senha[b][a].islower() == True:
            minusculo = 1
        elif senha[b][a] == '$' or senha[b][a] == '#' or senha[b][a]== '@':
            simbolo = 1
        elif senha[b][a].isdigit() == True:
            numero = 1
        a += 1
        
    if maiusculo == 1 and minusculo == 1 and numero == 1 and simbolo == 1:
        print('a senha', senha[b],  'esta de acordo com o padrao')
              
    b += 1
    a = 0
    maiusculo = 0
    minusculo = 0
    simbolo = 0
    numero = 0

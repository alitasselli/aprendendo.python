palavra = input('Digite uma palavra:\n')

invertida = ""

indice = len(palavra)-1

while indice >=0:
    invertida = invertida + palavra[indice]
    indice = indice-1

print (invertida)



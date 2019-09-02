#usando lista
#exercicio media de 7 notas
 #append e adicionar um item novo na lista

notas=[]
cont=1

while cont<=7:
	notas.append(float(input("Digite a nota do aluno"+str(cont)+":\n")))            
	cont = cont+1

cont2=0
soma=0

while cont2< len(notas):
    soma=soma+notas[cont2]
    cont2=cont2+1

media=soma/len(notas)

print(notas)
print(media)

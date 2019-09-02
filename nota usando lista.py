#usando lista
#exercicio media de 7 notas
 #append e adicionar um item novo na lista

notas=[]
cont=1

while cont<=7:
	notas.append(float(input("Digite a nota do aluno"+str(cont))))            
	cont = cont+1

print(notas)
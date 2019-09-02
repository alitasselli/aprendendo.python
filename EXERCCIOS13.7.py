linhas = []

texto=input('Digite um texto: ')


while texto:
	linhas.append(texto)
	texto=input('Digite um texto: ')

arq = open ('qualquer.txt' , 'w')

arq.writelines(linhas)

arq.close()




	

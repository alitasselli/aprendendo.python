linhas = []

texto=input('Digite um texto')


while texto:
	linhas.append(texto)
	texto=input('Digite um texto: ')

for l in linhas:
	print(l)
	

def mais_frequente(List): 
    contador = 0
    num = List[0] 
      
    for i in bairros: 
        frequencia_atual = bairros.count(i) 
        if(frequencia_atual> contador): 
            contador = frequencia_atual 
            num = i 
  
    return num

with open ('acidentes2017.csv','r', encoding = 'utf8') as f:
	bairros = []

	for linha in f:
		bairros.append(linha.split(';')[4].replace('"',''))

print(mais_frequente(bairros))


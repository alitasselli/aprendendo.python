def mais_frequente(List):
    counter = 0
    num = List[0]
    
    for i in List:
        curr_frequency=List.count(i)
        
        if(curr_frequency>counter):
            counter=curr_frequency
            num=i
        return num,counter
with open ('acidentes2017.csv','r',encoding='utf8') as f:
        bairros = []

        for linha in f:

bairros.append(linha.split(';')[4].replace('"',' '))  

print (mais_frequente(bairros))



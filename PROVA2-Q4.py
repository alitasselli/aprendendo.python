#questao prova icaro

nome = input ('digite o nome: \n')

nomes= nome.split(" ")

ultimo = nomes[-1].upper()
primeiro = nomes[0].title()

i=1
meio= ""

while i < len(nomes) -1:
    nome_atual=nome[i]
    primeira_letra=nome_atual[0]


print(ultimo+',',primeiro ,meio.strip())

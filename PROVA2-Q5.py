#questao britney

letra = "oh baby,baby Oh baby,baby,baby Ah,yeah,yeah Oh baby,baby How I was supposed to know"

letra= letra.lower().replace(',','')

palavras =letra.split()

i =0

palavra_max = ""
count_max= 0

while i < len(palavras):
    palavra_atual=palavras[i]
    count_atual=0

    j=0
    while j< len(palavras):
                 if palavra_atual==palavras[j]:
                     count_atual= count_atual+1
                 j= j+1

if count_atual > count_max:
                 count_max=count_atual
                 palavramax=palavra_atual

i=i+1

print(palavra_max, " apareceu", count_max, "vezes")

letra = 'like Baby baby baby ohh Baby baby like nooo'

letra=letra.lower()

palavras=letra.split()

letra_sem_repeticao= ''

i=0
while 1< len(palavras):
    if palavras[i] not in letra_sem_repeticao:

        letra_sem_repeticao = letra_sem_repeticao + palavras[i] + ''

print (letra_sem_repeticao.strip())



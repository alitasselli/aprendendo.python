mov=1
x=0
y=0

while mov != [""]:

    mov=input('Digite o movimento a ser relizado:')
    mov=mov.split(" ")
    
    if mov[0] == "CIMA":
        y+=int(mov[1])
    elif mov[0] == "BAIXO":
        y-=int(mov[1])
    elif mov[0] == "DIREITA":
        x+=int(mov[1])
    elif mov[0] ==  "ESQUERDA":
        x-=int(mov[1])

dist= round((x**2+y**2)**(1/2))

print ("a distancia entre os pontos e", dist)

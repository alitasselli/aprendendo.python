ma=int(input('digite a nota de matematica de Ana\n'))
mm=int(input('digite a nota de matematica de Mari\n'))
pa=int(input('digite a nota de portugues de Ana\n'))
pm=int(input('digite a nota de portugues de Mari\n'))
fa=int(input('digite a nota de fisica de Ana\n'))
fm=int(input('digite a nota de fisica de Mari\n'))
ia=int(input('digite a nota de ingles de Ana\n'))
im=int(input('digite a nota de ingles de Mari\n'))

medaA= ((ma+pa+fa+ia)/4)
medaM= ((mm+pm+fm+im)/4)

medpA=((ma*4+pa+fa*3+ia*2)/10)
medpM=((mm*4+pm+fm*3+im*2)/10)



print('A media aritmetica de Ana e de Mari sao respectivamente:', medaA,'e', medaM)
print ('A media ponderada de Ana e de Mari sao respectivamente:',medpA ,'e', medpM)


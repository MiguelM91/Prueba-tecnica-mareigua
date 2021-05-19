#Cree un programa que sea capaz de escribir los números del 1 al 100

numeros= []

for i in range(1,101):
    if i%3==0 and i%5!=0:
        numeros.append("{}: mare".format(i))
    elif i%5==0 and i%3!=0:
        numeros.append("{}: igua".format(i))
    elif i%3==0 and i%5== 0:
        numeros.append("{}: mareigua".format(i))
    else:
        numeros.append(i)

print(numeros)









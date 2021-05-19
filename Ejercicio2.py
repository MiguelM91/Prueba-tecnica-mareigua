#  Escriba una función que encuentre el entero más grande en un arreglo de enteros positivos
matriz = []
numero = int(input("Ingresar numero para agregar a la lista, Digite 0 si desea finalizar):\n"))
while numero!=0:
    matriz.append(numero)
    numero=int(input("Ingrese otro número:"))
ordenada = sorted(matriz)
mayor = ordenada[-1]
print("El numero mayor es {}".format(mayor))

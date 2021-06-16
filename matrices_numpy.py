import numpy as np
print("Multiplicacion de matrices con numpy")

print("Ingrese las dimesiones de la primera matriz")
a=int(input("Filas:"))
b=int(input("Columnas:"))
print("Segunda matriz")
d=int(input("Filas:"))
while(d!=b):
    print("Para multiplicar las matrices la fila de la segunda columna debera tener el mismo valor que la columna de la primera matriz")
    d = int(input("Ingrese un valor de filas valido: "))
c=int(input("Columnas:"))

valores1=list(map(int, input("Ingrese los numeros de la matriz 1 separados por un espacio. Cantidad de numeros a ingresar " + str((a*b)) +" ").split()))
matriz1=np.array(valores1).reshape(a,b)
print()
print("Primera matriz")
print(matriz1)

valores2=list(map(int, input("Ingrese los numeros de la matriz 2 separados por un espacio. Cantidad de numeros a ingresar " + str((b*c))+" ").split()))
matriz2=np.array(valores2).reshape(b,c)
print()
print("Segunda matriz")
print(matriz2)

print()
print("Matriz resultante")
matrizResultante=np.dot(matriz1, matriz2)
print(matrizResultante)

import random
filas = 2
columnas = 3

print("\nEjemplo 1")
matriz_2x3_ejemplo2 = []
for fil in range(filas):
    matriz_2x3_ejemplo2.append([random.randint(1,10)])
    for col in range(columnas):
        matriz_2x3_ejemplo2.append([random.randint(1,10)])
print("Resultado de la matriz:")
print(matriz_2x3_ejemplo2)

print("\n----------------------------")
print("Ejemplo 2")


print("\n----------------------------")
print("Ejemplo 3")
matriz_2x3_ejemplo3 = [[random.randint(1,10)] * columnas for fil in range (filas)]
print("Resultado de la matriz:")
print(matriz_2x3_ejemplo3)


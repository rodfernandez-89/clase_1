#'-Librerias-------------------------------
from metodos import insertar_numeros
import random

#'-Listas----------------------------------
lista_numeros = []

#'-Bloque principal------------------------
for i in range(3):
    numero = int(input("Ingrese un numero: "))
    insertar_numeros(lista_numeros, numero) #Se pasa la posición de memoria
print(f"Lista de numeros : {lista_numeros}") # Salida de mensaje con el resultado de los números almacenados
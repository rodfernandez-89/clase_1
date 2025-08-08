#'-Listas--------------------------------------------------------
lista_numeros = []

#'-Funcion para agregar numeros a la lista------------------------
'''Los números ingresados por el usuario, se agregaran a la lista "lista_numeros" y me devuelve la lista completa'''
def agregarNumero(numero):
    lista_numeros.append(numero)
    return lista_numeros

#'-Función para almacenar mensajes de salida----------------------
'''En esta función se almacenan los mensajes de salida'''
def salidaMensaje(lista_numeros):
    print(f"Numeros ingresados: {lista_numeros}")

#'-Función principal----------------------------------------------
'''Inicia el sistema solicitando al usuario que ingrese un número'''
def main():
    for i in range(3):
        numero = int(input("Ingrese un numero: "))
    agregarNumero(numero)
    salidaMensaje(lista_numeros)
main()
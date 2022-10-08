#Definir una tupla con 10 edades de personas.
#Imprimir la cantidad de personas con edades superiores a 20.
#Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

def edad(lista):
    print("Todas las edades superiores a 20: ")
    for i in lista:
        if (i > 20):
            print(i, end=" ")

    exit()

def main():
    x = 10
    lista = [0]*x
    for i in range(x):
        lista[i] = int(input(f"Escriba la edad de la persona {i+1}: "))
    edad(lista)

main()
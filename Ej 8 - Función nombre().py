#Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
#También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)

def nombre(lista, x):
    print(f"Lista de nombres que comienzan por {x}: ")
    for i in lista:
        for j in x:
            if(i[0] == j):
                print(i, end=" ")
    
    exit()

def main():
    x = [0, 0]
    x[0] = str(input("Escribe un carácter: "))
    x[0] = x[0].lower()
    x[1] = x[0].upper()
    if(len(x[0]) > 1):
        main()
    y = int(input("Escribe el tamaño de la lista: "))
    lista = [0]*y
    for i in range(y):
        lista[i] = str(input(f"Escribe un numbre en el espacio {i+1}: "))
    nombre(lista, x)

main()

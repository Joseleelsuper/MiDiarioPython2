#Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, 
#y devuelva las palabras que tengan mas de n caracteres.

def filtrar_palabras(lista, n):
    lista2 = []
    for i in lista:
        if(len(i) > n):
            lista2.append(i)
    print(f"Las palabras que superan los {n} carácteres son: ",lista2)

    exit()

def main():
    n = int(input("Escribe un número: "))
    x = int(input("Escribe el número de palabras que habrá en la lista: "))
    lista = [0]*x
    for i in range(x):
        lista[i] = str(input(f"Escribe la palabra ubicada en el espacio {i+1}: "))
    
    filtrar_palabras(lista, n)

main()

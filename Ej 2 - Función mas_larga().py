#Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.

def mas_larga(lista):
    y = 0
    for i in lista:
        if((y>0 and len(i) > len(x)) or y == 0):
            x = i
        y+=1
    print("La palabra más larga es: ",x)

    exit()

def main():
    x = int(input("Escribe el número de palabras que habrá en la lista: "))
    lista = [0]*x
    for i in range(x):
        lista[i] = str(input(f"Escribe la palabra en el hueco de la lista {i+1}: "))
    
    mas_larga(lista)

main()
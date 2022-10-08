#La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. 
#Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. 
#Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.

def max_in_list(lista):
    x = 0
    for i in lista:
        if(i > x):
            x = i
        
    print("El número mayor de la lista es: ",x)

    exit()

def main():
    x = int(input("Escribe el número de espacios de la lista: "))
    lista = [0]*x
    for i in range(x):
        lista[i] = int(input(f"Escribe el número {i+1}: "))
    
    max_in_list(lista)

main()

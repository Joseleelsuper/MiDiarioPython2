#Construir un pequeño programa que convierta números binarios en enteros.

def binario_a_enteros(x):
    y = 0
    cont = 0
    for i in x:
        if(i == "1"):
            y += 2**cont
        cont+=1
    print("El número en decimal es: ",y)

    exit()

def main():
    x = str(input("Escribe un número en binario: "))
    binario_a_enteros(x)

main()

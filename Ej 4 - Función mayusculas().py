#Escribir un programa que le diga al usuario que ingrese una cadena. 
#El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.

def mayusculas(cadena):
    mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
             "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    x = 0
    for i in cadena:
       for j in mayus:
            if (j == i):
                x+=1

    print("El número de mayúsculas en la cadena es: ",x)

    exit()

def main():
    cadena = str(input("Escribe una frase: "))
    mayusculas(cadena)

main()
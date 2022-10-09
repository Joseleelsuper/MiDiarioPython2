#Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
#Se puede hacer que el usuario sea quien elija la palabra.

from collections import Counter

def contar_vocales(cadena):
    cadena = cadena.lower()
    #:0 es para que no muestre el valor de la letra, solo la cantidad de veces que aparece
    vocales = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    for i in cadena:
        if(i in vocales):
            vocales[i] += 1
            print(f"La letra {i} aparece {vocales[i]} veces")

    exit()

def main():
    cadena = str(input("Escribe una frase: "))
    contar_vocales(cadena)

main()
#Escribir un pequeño programa donde:
#- Se ingresa el año en curso.
#- Se ingresa el nombre y el año de nacimiento de tres personas.
#- Se calcula cuántos años cumplirán durante el año en curso.
#- Se imprime en pantalla.

def datos(lista, personas, x):
    for i in range(personas):
        print(f"{lista[i]} cumplirá un total de {x - lista[i+personas]} años este curso.")

def main():
    x = int(input("Ingresa el año del curso: "))
    personas = 3
    lista = [0]*(2*personas)
    for i in range(personas):
        lista[i] = str(input(f"Escribe el nombre de la persona {i+1}: "))
        lista[i+personas] = int(input(f"Escribe el año de nacimiento de la persona {i+1}: "))
    datos(lista, personas, x)

main()
        

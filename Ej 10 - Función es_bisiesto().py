#Escriba una función es_bisiesto() que determine si un año determinado es un año
#bisiesto. Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400

def es_bisiesto(año):
    if((año % 4 == 0 or año % 400 == 0) and año % 100 != 0):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
        
    exit()

def main():
    año = int(input("Escribe un año: "))
    es_bisiesto(año)

main()

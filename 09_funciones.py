#Funciones

def saludar_usuario():
    print("Hola como estas?")
    print("Futuro SRE")

#saludar_usuario()

for i in range(5):
    print(f"Turno: {i}")
    saludar_usuario()

def suma(numero1, numero2):
    return numero1+numero2

print(suma(1,100000)*suma(2,2))

#Por medio de input

numero1 = float(input("Selecciona tu primer número: "))

def seleccionar_numero_dos():
    numero2 = float(input("Selecciona tu segundo numero: "))
    if numero2 == 0:
        print("No es posible seleccionar 0 para la división")
        return seleccionar_numero_dos()
    return numero2

numero2= seleccionar_numero_dos()

print("El resultado de tu suma es: ", numero1+numero2)
print("El resultado de tu resta es: ", numero1-numero2)
print("El resultado de tu multiplicacion es: ", numero1*numero2)
print("El resultado de tu divisón es: ", numero1/numero2)
#Args(), Kwargs



#Args
#Agrupa n argumentos, lo almacena en una tupla
#permite recibir múltiples argumentos posicionales.

def ejemplo(arg1, arg2, arg3, arg4):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)

ejemplo("Hola", "dos", "Adios", "tres")

def ejemplo_dos(*args): #funciona como un tipo de comodin para recibir n argumentos
    #print(args) #Lo imprime como tupla
    for i in args:
        print(i, type(i)) #Lo imprime como cada tipo de dato

ejemplo_dos("Mex", "USA", "Brazil", "Canada", 22, True)

def total(*args):
    total = sum(args)
    print(total)

total(22, 100, 200, 44)

#kwargs, keyworkd arguments
#permite recibir múltiples argumentos nombrados (clave=valor)

def empleado(nombre, puesto, lenguaje):
    print(nombre)
    print(puesto)
    print(lenguaje)

empleado("Mauro", "SRE", "Python") #Puede ser (nombre='Mauro', puesto='SRE', lenguaje='Python')

def empleado_dos(**kwargs):
    #for key, value in kwargs.items():
    #    print(f"{key}:{value}")
    print(kwargs)

empleado_dos(nombre='Mauro', puesto='SRE', lenguaje='Python')

#Ejemplo args(valor solo), kwargs(clave=valor)

def calcular_precio_total(*args,**kwargs):
    precio_total = sum(args)
    descuento = kwargs.get('descuento', 0)
    impuesto = kwargs.get('impuesto', 0)

    precio_total = precio_total - (precio_total*descuento) 
    #Mejor forma de representarlo 
    #precio_total -= precio_total * descuento

    precio_total = precio_total + (precio_total * impuesto)
    #Mejor forma de representarlo
    #precio_total += precio_total * impuesto
    return precio_total

precio_final = calcular_precio_total(100, 65, 30, descuento=.2, impuesto=.01)
print(precio_final) #157.6 

##Desempaquetado de iterables otra forma de representarlo
suma_de_precios = [100, 65, 30] #Lista
descuentos_e_impuestos = {'descuento': .2, 'impuesto': .01} #diccionario
precio_final_dos = calcular_precio_total(*suma_de_precios, **descuentos_e_impuestos)
print(precio_final_dos)#157.6

#Primer forma de importar

import aritmeticas.operaciones_avanzadas as op_avanzadas
import aritmeticas.operaciones_basicas as op_basicas

#resultado = aritmeticas.operaciones_avanzadas.multiplicacion(10,2) sin alias
resultado = op_avanzadas.multiplicacion(100,2) #Con el alias definido
print(resultado)

#Segunda forma de importar

from aritmeticas import operaciones_avanzadas as avan
from aritmeticas import operaciones_basicas as bas

result = avan.dividir(10,2)
print(result)
result_dos = bas.restar(10,2)
print(result_dos)
#Importando el modulo
from aritmeticas.operaciones_avanzadas import multiplicacion, dividir


def ingresar_valores():
    n1 = float(input("Ingresa tu primer digito: "))
    n2 = float(input("Ingresa tu segundo digito: "))
    if n2 == 0 or n2 == '':
        return ingresar_valores()
    print(f"El resultado de tu division es: {dividir(n1,n2)}")

ingresar_valores()



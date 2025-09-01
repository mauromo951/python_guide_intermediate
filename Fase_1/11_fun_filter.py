#Funcion de Orden Superior, High Order Superior

#filter() filter(función, iterable)
#Filtra elementos de una colección según una condición booleana.

#Retornar los pares de una lista
def retornar_par(numero):
    return numero%2==0

numeros = [1,2,3,4,5,6,7,8]

pares = list(filter(lambda x:x%2==0, numeros))
pares_dos = list(filter(retornar_par, numeros))
print(pares)
print(pares_dos)

#Aplicar filtro que empiecen con letra A en una lista

paises = ['Mexico', 'Argentina', 'Brasil', 'Alemania','angola']


lista_filtrada = list(filter(lambda x:x[0]=='A' or x[0]=='a',paises))
print(lista_filtrada)
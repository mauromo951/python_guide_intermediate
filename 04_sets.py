#set() y operaciones entre sets, coleccion desordenada de objetos únicos


variable = {'manzana','pera','manzana','platano'}

print(type(variable))
print(variable)

#Tipo 1 de Sets: Set mutable
a=set('adacadabra') #Mutable, se pueden añadir nuevos elementos
print(a)
a.add('g')
print(a)
a.add('a')
print(a)

#Tipo 2 de Sets: Set inmutables (no se pueden añadir elemtnos)
b=frozenset('perro')
print(b)
#no se puede b.add ya que es inmutable

#INTERSECTION, solo imprime los valores en los que coinciden ambos sets
miSet = {1,2,3,4,5,6}.intersection({3,4,5,6,7})
miSet = {1,2,3,4,5,6} & {3,4,5,6,7}
print(miSet)

#UNION, quita los duplicados y crea un set con elementos unicos
miSet_union = {1,2,3,4,5,6}.union({3,4,5,6,7})
miSet_union = {1,2,3,4,5,6} | ({3,4,5,6,7})
print(miSet_union)

#Difference, del primer set identifica los elementos que no tienen el segundo set

miset_dif = {1,2,3,4}.difference({2,3,5}) #como en el primero no hay 5 no hace ningun efecto en la salida
miset_dif = {1,2,3,4} - {2,3,6} 
print(miset_dif)

#Diferencia simétrica
#Ahora si contempla los valores únicos de cada set y los junta en un set único
miset_sim_dif = {1,2,3,4}.symmetric_difference({2,3,5})
print(miset_sim_dif)

#Superset, arroja true o false
#Valida si el segundo set existe o no dentro del primer set

super_set= {1,2,3,4}.issuperset({4,5}) #False porque 4 y 5 no están dentro del primer set
super_set2= {1,2,3,4,5,6,7,8}.issuperset({4,5,7}) #True porque el segundo set si esta dentro del primer set
print(super_set2)

#subset
#Valida si el elemento A esta por completo en el elemnto B
sub_set= {1,2,3,4}.issubset({1,2,3,4,5,6}) #True todo A existe en B
print(sub_set)
import sys
#Tipos numéricos
print('Tipos numéricos: ')
print(sys.getsizeof(5))
print(sys.getsizeof(5.3))
#Tipo String
print('Tipo String: ')
print(sys.getsizeof(''))
print(sys.getsizeof('1'))
print(sys.getsizeof('1234'))
#Tipo Booleano
print('Tipo Booleano: ')
print(sys.getsizeof(True))
print(sys.getsizeof(False))
#Lista
print('Tipo Lista: ')
print(sys.getsizeof([]))
print(sys.getsizeof([1]))
print(sys.getsizeof([1, 2, 3, 4]))
#Tuplas
print('Tipo Tuplas:')
print(sys.getsizeof(()))
print(sys.getsizeof((1,)))
print(sys.getsizeof((1, 2, 3, 4)))
#Conjuntos 
print('Tipo Set:')
print(sys.getsizeof(set()))
print(sys.getsizeof(set([1])))
print(sys.getsizeof(set([1, 2, 3, 4])))
#Diccionario
print('Tipo Diccionario:')
mi_diccionario = {"clave1": "valor1", "clave2": 42, "clave3": [1, 2, 3]}
print(mi_diccionario)
print(mi_diccionario["clave1"])  # Imprime "valor1"
print(mi_diccionario["clave2"])  # Imprime 42
print(sys.getsizeof(mi_diccionario)) # Imprime 184 bytes

'''
# Tupla vacía
coordenada = ()

# Tupla con elementos
coordenada = (33.9425, -118.4081)  # LAX (Aeropuerto de Los Ángeles)

# Tupla con un solo elemento (requiere coma al final)
rumbo = (270,)  # Sin la coma sería tratado como un entero entre paréntesis

# Tupla sin paréntesis (empaquetado implícito)
avion_info = "Boeing 787", "Dreamliner", 2009, 242

# Indexación (similar a las listas)
print(coordenada[0])  # 33.9425
print(avion_info[-1])  # 242 (pasajeros)

# Slicing
print(avion_info[0:2])  # ("Boeing 787", "Dreamliner")

# Desempaquetado de tuplas
fabricante, modelo, año, capacidad = avion_info
print(f"El {fabricante} {modelo} se lanzó en {año}")

# Desempaquetado con *
lat, lon = coordenada
print(f"Latitud: {lat}, Longitud: {lon}")
'''
lista = [1,3,4,9]
lista[0] = 5

lista_de_tuplas = [(0,0), (4,5), (5,0)]
lista_de_tuplas.append((9,4))
print(lista_de_tuplas)
lista_de_tuplas[0] = (1,1)
print(lista_de_tuplas)

tupla_de_listas = ([1,4,6], [9,7,0])
print(tupla_de_listas)
tupla_de_listas[0][0] = 10
print(tupla_de_listas)
#tupla_de_listas[0] = [4,3,1]   Error de asignación
numeros = (3, 12, 90, 45, 32)

for n in numeros:
    print(n)

#Condicionales con listas y tuplas
if 12 in numeros:
    print("El 12 es parte de la tupla")
else:
    print("No se encuentra el 12")
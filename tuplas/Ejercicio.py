#EJERCICIOS TUPLAS


 #EJERCICIO 1:# Determina en que posicion se encuentra determinado objeto.
print("---------Ejercicio 1---------")
tupla = ("Casa" , "2", "345", "Perro",99)
print("Elementos de tupla:",tupla)
print("Elemento de la posicion 0: ",tupla[0])
print("Elemento de la posicion 1: ",tupla[1])
print("Elemento de la posicion 2: ",tupla[2])
print("Elemento de la posicion 3: ",tupla[3])
print("Elemento de la posicion 4: ",tupla[4])

#EJERCICIO 2: # Ubica cuantos elementos hay en una variable, solo funciona si hay dos terminos identicos, tambien ubica en que posicion esta determinado objeto.
print("---------Ejercicio 2---------")
tupla = ("Casa" , "2",99,"345", "Perro",99)
print("Elementos de tupla:",tupla)
print("Numero de elementos 99:",tupla.count(99))
print("Posicion  ocupa el elemento perro:",tupla.index("Perro"))

#EJERCICIO 3: # Extrae una tupla, y luego la empieza en el indice n y esta terminara en el indice m-1.
print("---------Ejercicio 3---------")
tupla = (1,2,3,4,5,6,7,8,9)
print(tupla)
print(tupla[4:9])
print(tupla[:3])
print(tupla[2:])

#EJERCICIO 4: # Nos permite saber la cantidad de elementos que tiene una tupla gracias a la funcion len.
print("........Ejercicio 5....")
tupla1 = (29, "Televisión", 8763)
tupla2 = (1,2,3, "Videojuego")
print("Número elementos de tupla1: ", len(tupla1))
print("Tupla1: ", tupla1)
print("Número elementos de tupla2: ",len(tupla2))
print("Tupla2: ", tupla2)
tuplaconcatenada = tupla1 + tupla2
print("Número elementos de tuplaconcatenada: ", len(tuplaconcatenada))
print("tuplaconcatenada: ", tuplaconcatenada)

# Ejercicio 5: #  Nos permite multiplicar los valores que contiene la tupla dependiendo de cuantas veces queramos que se multipliquen en este caso 4.
print("........Ejercicio 5....")
tupla = (1,2,3,4,5,6,7,8,9,0)
print(tupla)
tuplaresultante = tupla * 4
print(tuplaresultante)
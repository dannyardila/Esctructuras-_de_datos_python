# Ejercios
"Los ejercicios con diccionarios los hemos dividio en dos grupos diferentes. El primer grupo de ejercicios consiste en la manipulacion de los diccionarios y el segundo grupo consiste en el aprendizaje de los metodos propios de los tipos de datos diccionario."

# Manipulacion 
 
 # EJercicio 1: Muestra algunos elementos del mismo diccionarios. Para acceder a los elementos del diccionario deberas de utilizar la clave del elemento.

print("--------Ejercicio 1--------")

diasemanaingles = {"Lunes" : "Monday", "Martes" : "Tuesday", "Miercoles" : "Wednesday", "Jueves" : "Thursday", "Viernes" : "Friday"}
print(diasemanaingles["Lunes"])
print(diasemanaingles["Miercoles"])
print(diasemanaingles["Viernes"])

# Ejercicio 2:Modifica el valor de algún elemento y borrando algún elemento. En el ejercicio utilizaremos el diccionario del ejercicio anterior añadiendo los días sábado y domingo, modificando el valor de algún elemento y borrando algún elemento.

print("--------Ejercicio 2--------")

diassemanaingles = {"Lunes":"Monday","Martes":"Tuesday","Miercoles": "Wednesday","Jueves": "Thursday","Viernes": "Friday"}

print(diassemanaingles)
diassemanaingles["Sabado"] = "Saturday"
print(diassemanaingles)
diassemanaingles["Domingo"] = "Sunday"
print(diassemanaingles)
diassemanaingles["Lunes"] = "MondayBORRAR"
print(diassemanaingles)

#Ejercicio 3:Funciones max y min con los diccionarios. La primera devolverá el número de elementos que contiene el diccionario; la segunda, el elemento con el valor mayor y la tercera, el elemento con el valor menor. El valor mayor y el valor menor serán devueltos siempre que pueda calcularse dependiendo de los elementos que componen el diccionario. 

print("--------Ejercicio 3--------")

diassemanaingles = {"Lunes" : "Monday","Martes" : "Tuesday","Jueves":"Thursday","Miercoles": "Wednesday", "Viernes" : "Friday"}
print("Número de elementos del diccionario: ",len(diassemanaingles)) 
print("Elemento mayor del diccionario: ",max(diassemanaingles)) 
print("Elemento menor del diccionario: ",min(diassemanaingles))


#Ejercicio 4: Un ejercicio que nos permite aprender todas  la funciones

print("--------Ejercicio 4-----------")

diassemanaingles= {"Lunes": "Monday", "Martes" : "Tuesday",

"Miercoles": "Wednesday",

"Jueves": "Thursday",

"Viernes": "Friday"}

print("Diccionario original: ", diassemanaingles)

diccionariocopia =diassemanaingles.copy()

print("Diccionario copy: ",diccionariocopia)

print("Valor del Lunes (pop): ", diassemanaingles.pop("Lunes"))

print("Diccionario después del pop: ",diassemanaingles)

print("Elemento al azar con popitem: ", diassemanaingles.popitem())

print("Diccionario después del popitem: ", diassemanaingles)

print("Valor del Martes (get): ",diassemanaingles.get("Martes"))

print("Valor del Lunes (get) (no existe): ",diassemanaingles.get("Lunes"))
print("Valor del Lunes (get) (no existe): ",diassemanaingles.get("Lunes","No existe")) 

diassemanaingles.update({"Lunes":"MondayNUEVO", "Martes":"TuesdayNUEVO"})

print("Diccionario después del update: ",diassemanaingles)

print("setdefault del Sábado: ",diassemanaingles.setdefault("Sabado", "Saturday"))

print("Diccionario después del setdefault (nuevo elemento): ",diassemanaingles) 
print("setdefault del Lunes: ",diassemanaingles.setdefault("Lunes", "Lunes"))

print("Diccionario después del setdefault (elemento existente): ",diassemanaingles)

print("Elemento iterable (items): ",diassemanaingles.items())

print("Elemento iterable (claves): ",diassemanaingles.keys()) 
print("Elemento iterable (valores): ",diassemanaingles.values())

print("Diccionario después del clear: ",diassemanaingles.clear())




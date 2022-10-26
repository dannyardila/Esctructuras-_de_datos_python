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
diassemanaingles = {"Lunes":"Monday","Martes":"Tuesday","Miercoles": "Wednesday","Jueves": "Thursday","Viernes": "Friday"}

print(diassemanaingles)
diassemanaingles["Sabado"] = "Saturday"
print(diassemanaingles)
diassemanaingles["Domingo"] = "Sunday"
print(diassemanaingles)
diassemanaingles["Lunes"] = "MondayBORRAR"
print(diassemanaingles)

#E
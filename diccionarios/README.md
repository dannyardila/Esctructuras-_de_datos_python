# DICCIONARIOS

* El diccionario de ejemplo esta compuesto por tres elementos, en la siguiente tabla te mostramos  la relacion entre la clave y el valor asociado:

|Clave|Valor|
|---------|--------|
|"Clave1"   |"Valor1"   |
|"Clave2"      |"Valor2"      |
| "Clave3"  |   "Valor3"   |  

    Las claves de los diccionarios de los diccionariospueden ser diferentes tipos de datos, aunque siempre deberan de ser datos inmutables.Los tipos de datos  soportados en Python para ser claves de los diccionarios son:
         ❥ Cadenas de texto (str).
         ❥ Numeros (enteros,reales y complejos).
         ❥ Booleanos.
         ❥ Bytes
         ❥ Tupla

         Aunque puedes utilizar todos ellos como clave, lo mas comunes son cadenas de texto y enteros.

 El siguiente ejercicio consiste en añadir elementos al diccionario, eliminar elementos del diccionario y en modificar el valor de los elementos del diccionario.

La forma de añadir un elemento al diccionario es la siguiente:

Diccionario/Nueva Clave] = Nuevo Valor

La forma de modificar el valor de un elemento del diccionario es la siguiente:

Diccionario/ClaveQue Se VaAModificar] = Nuevo Valor

La forma de eliminar un elemento del diccionario es la siguiente:

del Diccionario[Clave Elemento A Borrar]

En el ejercicio utilizaremos el diccionario del ejercicio anterior añadiendo los días sábado y domingo, modificando el valor de algún elemento y borrando algún elemento. El código fuente es el siguiente:

# MÉTODOS PROPIOS    
El tipo de dato diccionario en Python posee una serie de funciones que nos permiten manipular los diccionarios realizando operaciones complejas de forma sencilla y con una simple instrucción. El formato de uso de la gran mayoría de las funciones es el siguiente:

Veamos en detalle cada una de las partes:

Diccionario: diccionario que ejecuta la función.

NombreFuncion: nombre de la función que se quiere ejecutar.

Parámetros: no todas las funciones tienen parámetros para ejecutarse, esta parte es dependiente de la función que se quiere ejecutar.

La funciones de listas que pone a nuestra disposición Python son las

siguientes:

✤copy: realiza una copia exacta del diccionario en uno nuevo.

⚫ Valor devuelto: diccionario copiado..

• Parámetros: no tiene.

✤pop: obtiene el valor de la clave pasada como parámetro y además elimina el elemento del diccionario.

• Valor devuelto: valor del elemento o error en caso de no encontrar la clave en el diccionario.

• Parámetros: clave a buscar en el diccionario.

✤popitem: obtiene un elemento aleatorio del diccionario y lo elimina del

mismo.

⚫ Valor devuelto: elemento del diccionario y en caso de que no tenga elementos el diccionario da un error.

⚫ Parámetros: no tiene.

✤get: obtiene el valor de la clave pasada como parámetro.

• Valor devuelto: devolverá el valor del elemento en caso de existir dicha clave y en caso de no existir devolverá "None". Existe la posibilidad de especificar mediante un segundo parámetro un valor diferente a "None" como retorno en caso de no existir la clave.

⚫ Parámetros: tiene dos parámetros, el primero es clave del elemento a buscar y el segundo es opcional y es el valor que se quiere retornar en caso de no existir dicha clave en el diccionario. obligatorio y es la

✤update: realiza una actualización del diccionario utilizando otro diccionario, Aquellos elementos del diccionario que se utilizan para actualizar el principal sustituirán los existentes en el mismo y aquellos elementos que no existan serán añadidos al diccionario como nuevos elementos.

Valor devuelto: nuevo diccionario.

• Parámetros: diccionario.

✤setdefault: intenta insertar un elemento (clave y valor) en el diccionario. En caso de no existir dicho elemento, la función inserta y devuelve el valor del elemento y en caso de existir, lo único que hace es devolver el valor actual.

• Valor devuelto: diccionario resultante.

⚫ Parámetros: dos parámetros que son la clave y valor. Es posible no especificar el valor y por defecto se insertará el valor None como valor del elemento.

✤clear: elimina todos los elementos del diccionario.

• Valor devuelto: diccionario vacío.

• Parámetros: no tiene.

✤items: devuelve un objeto iterable (que puede utilizarse en bucles. Lo veremos en próximos capítulos) compuesto por todos los elementos del diccionario.

⚫ Valor devuelto: objeto iterable compuesto por los elementos del diccionario.

Parámetros: no tiene.

✤keys: devuelve un objeto iterable (que puede utilizarse en bucles. Lo veremos en próximos capítulos) compuesto por todas las claves del diccionario.

⚫ Valor devuelto: objeto iterable compuesto por las claves del diccionario.

Parámetros: no tiene.

✤values: devuelve un objeto iterable (que puede utilizarse en bucles. Lo veremos en próximos capítulos) compuesto por todos los valores del diccionario.

• Valor devuelto: objeto iterable compuesto por los valores del diccionario.

• Parámetros: no tiene.


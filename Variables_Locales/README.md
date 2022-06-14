# Funciones 

## Variables Locales y Globales

### Variables Locales    

- Variables que se definen dentro de una funcion. Son validas unicamente dentro de la funcion.

- Las variables correspondientes a la funcion, solamente son accesibles por la funcion, es decir, se pueden usar solamente por ella. Al usuarlas fuera de la funcion marcara error.

- Una variable del algoritmo principal que se pasa a una funcion donde se modificia y es variable local, cambia su valor en la funcion pero NO en el algoritmo principal.

### Variables Globales 
- Son aquelas que no importa donde se usen o modifiquen siemnpre conservan los valores asignados, ya sea en el algortimo principal o en las funciones.
- Para hacer que una variable sea global hay que definirla como tal por medio de la instruccion `Global nombre_variable`

## Llamado por valor y llmadado por referencia 


### Paso por valor:
- Cuando se pasa una variable a una funcion creando una nueva localidad de memoria, donde se copian los valores de los parametros de la funcion.
- La memoria ocupada aumenta de tamaño.
Aunque en python no se aumenta la memoria, el paso de la variable es equivalente a paso por valor

### Paso por referencia 
- La variable se puede modificar en la funcion y el cambio siempre se realiza usando la referencia a la localidad de memoria donde se almacena la variable. Ej. Vriables tipo lista.

### Funciones lambda
- declaracion de una funcion en un solo renglon.
`f= lamda parámetros: expresión de la función f`

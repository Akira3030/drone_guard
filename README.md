<div>
    <h1 align="center">:snake: Python :snake:</h1>
    <h1 align="center">
        Drone Guard: Clean Code & Refactoring & Clean Architecture & Code Smell
    </h1>
<div>

## Table of contents
* [Uso de la aplicación](#uso-de-la-aplicación)
* [Github](#github)
* [Clean code](#clean-code)
* [Clean architecture](#clean-architecture)
* [Code smell](#code-smell)


## uso de la aplicación

### Ejecutar la aplicacion
entrypoint.py
```sh
/usr/bin/python3 /home/miguelgranadino/Escritorio/drone_guard/entrypoint.py
```

### Ejecutar los tests
```sh
python -m unittest -v
```

### Covertura de los tests
```sh
coverage run -m unittest && coverage report
```

### Dependencias
```sh
sudo pip install coverage
sudo pip install html-testRunner
sudo pip install pyyaml
sudo pip install flask_api
sudo pip install flask_script
sudo pip install flask_testing
```


## github
```sh
git status
git add .
git status
git commit -m "comentario"
git push -u origin master
   Username:
   Password:
```
## clean code

### 1) Evitar magic numbers
```python
# Bad:What the heck is 86400 for? --> No hardcode
time.sleep(86400);

# Good:Extract magic number as a variable
SECONDS_IN_A_DAY = 86400
time.sleep(SECONDS_IN_A_DAY)
```

### 2) Los nombres de variables deben revelar intención

```python
# Bad:
df = pd.read_csv('comercios.csv')
# Good:
comercios = pd.read_csv('comercios.csv')

# Bad:
addCmt
# Good:
addComment

# Bad:
user.createUser() --> User es redundante
# Good:
user.create();
```

### 3) La regla del Boy Scout

- Deja el campo más limpio de como te lo encontrastes

### 4) Funciones
- 20 lineas de largo
- Hacer una única cosa
- Command Query Separation --> Las funciones deben hacer algo o devolver algo pero no ambas cosas.
- No más de dos argumentos
- Mejor devolver excepciones que códigos de error siempre.
- No usar Switch --> Los switchs hacen n cosas
- Encapsular condicionales, evitar poner en los if cadenas de booleanos, mejor una subfunción con un nombre explícito
- Evitar condicionales negativas

### 4) Try - except

- Si hay un bloque try/catch mejor simplificarlos extrayendo funciones para cada uno de los bloques.
- Si hay try/catch en una función no debería haber nada más, si no seguro se está haciendo más de una cosa.
```python
try:
    hagoAlgoQuePuedeFallar()
except Exception as error:
    logError(error)
    
def logError(Exception e):
    logfile.exception(error)
```
### 5) Comentarios
- Los comentarios solo están justificados cuando no somos capaces de expresarnos con el código.

### 6) Clases
- Nombres de clases: evitar palabras como Manager, Services, Processor, etc
- El tamaño de los ficheros no debería superar las 200 líneas de media, con un límite máximo en 500.
- La anchura de las líneas de código, entre 80 y 120 caracteres, no deberíamos hacer scroll horizontal para leer código.
- El equipo debería tener unas reglas convenientemente consensuadas.

### 7) Errores
- Crear clases para los casos especiales en lugar de dejar al código cliente procesar el caso excepcional (patrón caso especial, Fowler).
- En general no es recomendable devolver null, en su lugar es mejor devolver una excepción o un objeto de caso especial.
- No usar códigos de error ya que confunden el flujo de ejecución y obligan al invocador a procesarlos inmediatamente.


### 8) Pricipio de inversión de dependencias(SOLID)
Principio de diseño de clases
- Nuestras clases deben depender de abstracciones, nunca de detalles concretos. 
De esta forma podremos tener nuestras entidades desacopladas facilitando su mantenimiento.
- Inyección de dependencias –> Un objeto no es responsable de instanciar sus dependencias, lo delega

```python
#Injeccion de dependencias
command = FindAllDocumentsQuery()
use_case = FindAlldocumentsUseCase(command)
routes = use_case.execute()
```

### 9) Tests
- Un assert por test
- se debe probar todo lo que pueda fallar
- Usar herramientas de cobertura
- No ignorar pruebas triviales, sobre todo por su labor de documentación
- Las pruebas deben ser rápidas (no más de 30 segundos todas)

## clean architecture

### 1) Identificadores UUIDs

- Este tipo de identificadores son útiles para evitar delegar la responsabilidad de generación de IDs a nuestra infraestructura. 
- Dado que los UUIDs son generados de forma aleatoria, y con una probabilidad despreciable de colisión, podemos hacer que nuestras entidades tengan el identificador como uno de los parámetros necesarios para ser construidos.
- Con esto hacemos que no sea necesario pasar por el repositorio de base de datos para saber qué identificador tendrá la entidad, con lo que lo podemos esperar incluso desde fuera.

```python
import uuid 

id_user = uuid.uuid1())
```

### 2) Desacoplar del framework
- No estamos obligados a usar la estructura de directorios del framework.
- Desacoplarnos de la estructura de directorios marcada por los frameworks, y cómo podemos llegar a hacerlo.
- ¿Qué beneficios tiene saltarte esto? si sale una nueva versión del framework.
Separar el dominio de la aplicación.
 
 ### 3) Tell don't ask
 <b>No usar getters y setters</b>
 - Añadir un constructor para rellenar los atributos de clase
 - Usar atributos de clase privados y sin setters
 - Evitar exponer la escritura de sus atributos (hacerlos privados, y no tener setters/getters).
 - Si no lo hacemos asi podrian darse estados incosistentes de nuestro monedo de dominio: por ejemplo crear un usuario sin email.
 - Hacer los atributos privados, no accesibles desde fuera.
 - Meter las validaciones de los atributos dentro de las clases. Como metodos privados.
 - El modelo de domino ya no es anemico.
 
 <b>Esconder los detalles de implentación de las clases</b>
 - Si modificamos algun metodo privado de nuestra clase ese cambio no afectara a otras clases.
 - Si hay muchas otras clases que usen metodos de nuestras clases cuando cambiemos esos metodos tambien tendremos que cambiar el resto de clases que la usan (por eso hay que evitar el acoplamiento entre clases).
 
 [TellDontAsk](https://martinfowler.com/bliki/TellDontAsk.html)
 
 
 
 ### 4) Modelo de domios anemicos
 - Solo tienen atributos sin comportamiento
 - Por lo tanto son DTOs (Data Transfer Objectos)
 
 
 ### 4) Testing
 - Diseñar la clase sabiendo que debera ser testeada
 
 ### 5) Excepciones del dominio
 
 
 ### 6) Clausulas de guarda
 ```python
 # Código farragoso de leer con multiples niveles de if-else
 if self.user_is_ready(user_id):
     if self.is_the_right_moment_to_notify_this_user():
         if.self ...
             return ...
         else:
             return ...
       else:
          ...
 else:
    ...
    
 # Refactoring con clausulas de guarda --> mucho más facil de leer
 if not self.user_is_ready(user_id):
     raise UserIsNotReady()
     
 if not is_the_right_moment_to_notify_this_user():
     raise ...
     
 if ...
     return ...
 
 ```
 
 ## code smell
 
 


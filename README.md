<div>
    <h1 align="center">:snake: Python</h1>
    <h1 align="center">
        Drone Guard: ejemplo de Clean Code & Refactoring & Clean Architecture en
    </h1>
<div>

## Table of contents
* [Ejecutar la aplicación](#ejecutar-la-aplicacion)
* [Ejecutar los tests](#ejecutar-los-tests)
* [Tests Coverage](#tests-coverage)
* [Dependencias](#dependencias)
* [Github](#github)
* [Ejemplos Clean Code](#ejemplos-clean-code)


## :monkey_face: Uso de la aplicación

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


## :monkey_face: GITHUB
```sh
git status
git add .
git status
git commit -m "comentario"
git push -u origin master
   Username:
   Password:
```
## :monkey_face: CLEAN CODE

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

Deja el campo más limpio de como te lo encontrastes
(Si no hay Tests tendremos miedo de tocar, no sea que rompamos algo)

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
    hagoAlgoQuePuedeFallar(); 
except Exception as error:
    logfile.exception(error)
```
### 5) Comentarios
Los comentarios solo están justificados cuando no somos capaces de expresarnos con el código.

### 6) Clases
- El tamaño de los ficheros no debería superar las 200 líneas de media, con un límite máximo en 500.
- La anchura de las líneas de código, entre 80 y 120 caracteres, no deberíamos hacer scroll horizontal para leer código.
- Cualquier equipo debería tener unas reglas convenientemente consensuadas.

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
- Pruebas suficientes, se debe probar todo lo que pueda fallar
- Usar herramientas de cobertura
- No ignorar pruebas triviales, sobre todo por su labor de documentación
-Las pruebas deben ser rápidas (no más de 30 segundos todas)

## :monkey_face: CLEAN ARCHITECTURE, DDD Y CQRS

### Identificadores UUIDs

Este tipo de identificadores son útiles para evitar delegar la responsabilidad de generación de IDs a nuestra infraestructura. Dado que los UUIDs son generados de forma aleatoria, y con una probabilidad despreciable de colisión, podemos hacer que nuestras entidades tengan el identificador como uno de los parámetros necesarios para ser construidos. Con esto hacemos que no sea necesario pasar por el repositorio de base de datos para saber qué identificador tendrá la entidad, con lo que lo podemos esperar incluso desde fuera.

### Desacoplar del framework
No estamos obligados a usar la estructura de directorios del framework.
Desacoplarnos de la estructura de directorios marcada por los frameworks, y cómo podemos llegar a hacerlo.
¿Qué beneficios tiene saltarte esto? si sale una nueva versión del framework.
Separar el dominio de la aplicación.
 
 ### Usar atributos de clase privados y sin getters
 
 Evitar exponer la escritura de sus atributos (hacerlos privados, y no tener setters si no sólo getters).
 





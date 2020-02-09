<h1 align="center">
  🐘🎯 Drone Guard: ejemplo de Clean Code & Refactoring & Clean Architecture en Python
</h1>

## Table of contents
* [Ejecutar la aplicación](#ejecutar-la-aplicacion)
* [Ejecutar los tests](#ejecutar-los-tests)
* [Tests Coverage](#tests-coverage)
* [Dependencias](#dependencias)
* [Github](#github)
* [Ejemplos Clean Code](#ejemplos-clean-code)


## :large_blue_circle: Uso de la aplicación

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


## :large_blue_circle: Uso de Github
```sh
git status
git add .
git status
git commit -m "comentario"
git push -u origin master
   Username:
   Password:
```
## :large_blue_circle: Ejemplos Clean Code

### 1) Evitar magic numbers
--------------------------------------
```python
# Bad:What the heck is 86400 for? --> No hardcode
time.sleep(86400);

# Good:Extract magic number as a variable
SECONDS_IN_A_DAY = 86400
time.sleep(SECONDS_IN_A_DAY)
```

### 2) Los nombres de variables deben revelar intención
---------------------------------------

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
- No más de dos argumentos

### 5) Command Query Separation
Las funciones deben hacer algo o devolver algo pero no ambas cosas.

### 6) Mejor Exceptions a devolver Error Codes

### 7) No usar Switch
Los switchs hacen n cosas

### 8) Pricipio de inversión de dependencias(SOLID)
Principio de diseño de clases
"Nuestras clases deben depender de abstracciones, nunca de detalles concretos. 
De esta forma podremos tener nuestras entidades desacopladas facilitando su mantenimiento."

```python
#Injeccion de dependencias
command = FindAllDocumentsQuery()
use_case = FindAlldocumentsUseCase(command)
routes = use_case.execute()
```


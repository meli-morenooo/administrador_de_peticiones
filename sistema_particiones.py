import random

# -------- DATOS DE UTILIDAD -----------------
# Tamaño de la dirección almacenada (procesos o peticiones)
size = 10

# Establezco una posición aleatoria en el disco.
posicion_actual = random.randint(0, 999)

# Creo una lista vacía donde se van a almacenar los numeros de pista. Ejecuto el código que va a crear el orden de pista aleatoria y va a almacenarlo en la lista vacía.
peticiones = []

for i in range(size):
    i = random.randint(0, 999)
    peticiones.append(i)

print(peticiones)
# ---------------------------------------------

# --------------- FUNCIONES -------------------
def fcfs(peticiones):
    for i in peticiones:
        print(i)

# EJECUCION:
# fcfs(peticiones)

def sstf(peticiones, posicion_actual):
    print(f"Posicion Actual: {posicion_actual}")
    # Inicializo en cero el numero mas cercano de la posicion del disco
    numero_cercano = 0
    size_partition = 1000
    # Inicio el recorrido del disco
    for x in range(size_partition):
        # Inicio la lectura de peticiones dentro del disco
        for i in peticiones:
            # Busco el número más cercano de la posición actual
            numero_cercano = min(peticiones, key=lambda x:abs(x-posicion_actual))
            # Muestro el número más cercano de la posición actual
            print(numero_cercano)
            # Actualizo la posición actual
            posicion_actual = numero_cercano
            # Elimino el número cernano de la lista peticiones para evitar repeticiones en los mivimientos
            peticiones.remove(numero_cercano)

# EJECUCION
# sstf(peticiones, posicion_actual)

def scan(peticiones, posicion_actual):
    size = 10
    print(f"Posicion Actual: {posicion_actual}")
    # Tamaño del disco - recorrido 
    size_disco = 999
    # Armo una lista con las direcciones para luego poder elegir de forma aleatoria con la función random
    direc = ["left", "right"]
    direction = random.choice(direc)
    print(f"Direccion: {direction}")
    
    left = []
    right = []
    for i in range(size):
        if (peticiones[i] < posicion_actual):
            left.append(peticiones[i])
        if (peticiones[i] > posicion_actual):
            right.append(peticiones[i])
    
    left.sort()
    right.sort()
    left = list(reversed(left))
    
    arranque = 2
    while arranque != 0:
        if direction == 'left':
            for i in left:
                print(i)
                                 
            # Cambio el valor de direction para poder realizar el recorrido de derecha
            direction = "right"
        
        elif direction == "right":
            for i in right:
                print(i)
                
            direction = "left"

        arranque -= 1
        
# EJECUCION
# scan(peticiones, posicion_actual)

def c_scan(peticiones, posicion_actual):
    size = 10
    print(f"Posicion Actual: {posicion_actual}")
    # Tamaño del disco - recorrido 
    size_disco = 999
    # Armo una lista con las direcciones para luego poder elegir de forma aleatoria con la función random
    direc = ["left", "right"]
    direction = random.choice(direc)
    print(f"Direccion: {direction}")
    
    left = []
    right = []
    for i in range(size):
        if (peticiones[i] < posicion_actual):
            left.append(peticiones[i])
        if (peticiones[i] > posicion_actual):
            right.append(peticiones[i])
    
    left.sort()
    right.sort()
    left = list(reversed(left))
    
    arranque = 2
    while arranque != 0:
        if direction == 'left':
            for i in left:
                print(i)
            
            right = list(reversed(right))
            # Cambio el valor de direction para poder realizar el recorrido de derecha
            direction = "right"
        
        elif direction == "right":
            for i in right:
                print(i)
            
            left = list(reversed(left))
            direction = "left"

        arranque -= 1
        
# EJECUCION
# c_scan(peticiones, posicion_actual)
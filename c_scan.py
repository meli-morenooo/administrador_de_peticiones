# C-SCAN. Este algoritmo es otra variante más del algoritmo SCAN. C-SCAN mueve el brazo
# de un extremo a otro igual que SCAN, sirviendo las peticiones que encuentra en su
# trayectoria. Al llegar al extremo opuesto, el brazo regresa rápidamente al extremo
# del que partió, sin servir ninguna petición en su regreso.

import random
print('+-----------------------------------------+')
print("| ##   ##   ##    ###   ###  ##   #   ##  |")
print("| # # # #  #  #  #   #  #    # #  #  #  # |")
print("| #  #  #  #  #  #   #  #    #  # #  #  # |")
print("| #     #  #  #   ###   ###  #   ##  #  # |")
print("| #     #  #  #  # #    #    #    #  #  # |")
print("| #     #  #  #  #  #   #    #    #  #  # |")
print("| #     #   ##   #   #  ###  #    #   ##  |")
print('+-----------------------------------------+')

# Creo una función para ejecutar el proceso de C-SCAN
def algoritmo_c_scan(peticiones, posicion_actual, direction):
    # Tamaño del disco - recorrido 
    size_disco = 1000
    # Tiempo de espera del movimiento
    tiempo_de_espera = 0
    # Movimientos realizados en el desplazamiento
    desplazamiento = 0
    # Listas vacías para establecer el orden de busqueda de izquierda a derecha
    left = []
    right = []
    # Listas vacías para almacenar los datos a visibilizar
    tiempoEspera = []
    desplaZam = []
    secuencia = []
    movimiento_realizado = []
    
    # Valor de los extremos según la dirección que tome al iniciar el algoritmo.
    if (direction == "left"):
        left.append(0)
    elif (direction == "right"):
        right.append(size_disco - 1)
    # Agrego los valores de las peticiones de acuerdo al recorrido según la dirección que tome y les corresponda
    for i in range(size):
        if (peticiones[i] < posicion_actual):
            left.append(peticiones[i])
        if (peticiones[i] > posicion_actual):
            right.append(peticiones[i])
    
    # Ordeno las listas y reverso para poder realizar los calculos sin errores y en el orden que corresponde
    left.sort()
    right.sort()
    left = list(reversed(left))
    print("_______________________________________________________________________")
    print("Según la dirección elegida, la secuencia inicial se encuentra ordenada\nde la siguiente manera:\n")
    print(f"Secuencia de Left: {left}")
    print(f"Secuencia de Right: {right}")
    print("_______________________________________________________________________\n")

    
    # Algoritmo que pone en marcha el proceso
    # La variable arranque solo sirve para poner en marcha el bucle
    # Necesito que haga 2 vueltas para recorer el lado izquierdo y luego volver para el lado recho o viceversa
    arranque = 2
    while arranque != 0:
        if direction == "left":
            for i in left:
                # El tiempo de espera inicial es de cero y se suma el desplazamiento realizado para actualizar 
                # el tiempo de espera del siguiente movimiento.
                tiempo_de_espera += desplazamiento
                # Almaceno este dato para su posterior suma al final del algoritmo
                tiempoEspera.append(tiempo_de_espera)
                                                
                # Para evitar errores en los calculos de los mivimientos y obtener un resultado correcto, 
                # establezco condiciones y voy resolviendo en base a cada condicion
                if i > posicion_actual:
                    # Realizo el calculo del movimiento
                    desplazamiento = i - posicion_actual
                    # Almaceno el desplazamiento realizado para su posterior suma total
                    desplaZam.append(desplazamiento)
                    # Armo un string para visibilizar el calculo del movimiento realizado
                    operation = "(" + str(i) + "-" + str(posicion_actual) + ")"
                    # Almaceno el string armado
                    movimiento_realizado.append(operation)
                    
                elif i < posicion_actual:
                    desplazamiento = posicion_actual - i
                    desplaZam.append(desplazamiento)
                    operation = "(" + str(posicion_actual) + "-" + str(i) + ")"
                    movimiento_realizado.append(operation)
                    
                # Actualizo la posicion actual
                posicion_actual = i
                # Almaceno los datos de acuerdo a la marcha del cilindro
                secuencia.append(posicion_actual)
            
            # Como en C-SCAN de un extremo se salta directo al otro extremo, necesito agregarlo para un correcto calculo    
            if posicion_actual == 0:
                if (size_disco-1) not in right:
                    right.append(size_disco-1)
                    right = list(reversed(right))
                else:
                    left = list(reversed(left))
            # Cambio el valor de direction para poder realizar el recorrido de derecha
            direction = "right"

        # Repito el mismo proceso que en left
        elif (direction == "right"):
            for i in right:
                tiempo_de_espera += desplazamiento
                tiempoEspera.append(tiempo_de_espera)
                if i > posicion_actual:
                    desplazamiento = i - posicion_actual
                    desplaZam.append(desplazamiento)
                    operation = "(" + str(i) + "-" + str(posicion_actual) + ")"
                    movimiento_realizado.append(operation)                    
                
                elif i < posicion_actual:
                    desplazamiento = posicion_actual - i
                    desplaZam.append(desplazamiento)
                    operation = "(" + str(posicion_actual) + "-" + str(i) + ")"
                    movimiento_realizado.append(operation)
                
                posicion_actual = i            
                secuencia.append(posicion_actual)
            
            if posicion_actual == 999:
                if 0 not in left:
                    left.append(0)
                    left = list(reversed(left))
                else:
                    left = list(reversed(left))
                    
            direction = "left"
         
        arranque -= 1
       
    # Realizo la suma del tiempo de espera 
    time = 0
    for t in tiempoEspera:
        time += t
    # Realizo la suma de los desplazamientos
    mov = 0
    for m in desplaZam:
        mov += m

    print("_______________________________________________________________________")
    print("Luego de llegar a un extremo se realiza el salto al otro extremo.\nLa secuencia inicial se ordena de nuevo de la siguiente manera:\n")
    print(f"Secuencia de Left: {left}")
    print(f"Secuencia de Right: {right}")
    print("_______________________________________________________________________\n")
    print("--------------------------------------------------------------------------------------------------------") 
    print(f"La distancia total que mueve la cabeza se calculo de la siguiente manera:\n{movimiento_realizado}")
    print(f"El tiempo promedio de espera se calculo de la siguiente manera: ({time} / 10)")
    print("--------------------------------------------------------------------------------------------------------\n")
    print("--------------------------------------------------------------------------------------------------------") 
    print(f"Número total de movimientos realizados durante el desplazamiento de la búsqueda: {mov}")
    print(f"Tiempo promedio de espera durante el reccorrido: {time / 10}")
    print(f"Secuencia de búsqueda realizada: {secuencia}")
    print("--------------------------------------------------------------------------------------------------------\n")


# Tamaño de la dirección almacenada (procesos o peticiones)
size = 10

# Establezco una posición aleatoria en el disco.
posicion_actual = random.randint(0, 999)  # Cilindro actual

# Ejecuto el código que va a crear el orden de pista aleatoria y va a almacenarlo en la lista vacía.
peticiones = []
for p in range(size):
    part = random.randint(0, 999)
    peticiones.append(part)
    
# Armo una lista con las direcciones para luego poder elegir de forma aleatoria con la función random
direc = ["left", "right"]
direction = random.choice(direc)

print("\n--------------------------------------------------------------------------------------------------------")
print(f"La secuencia de servicio del algoritmo C-SCAN es: {peticiones}")
print(f"El encabezado actual está en el N° {posicion_actual}")
print(f"Dirección del cilindro: '{direction}'")
print("--------------------------------------------------------------------------------------------------------") 

# Pongo en marcha la función del elevador
algoritmo_c_scan(peticiones, posicion_actual, direction)
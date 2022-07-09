# SCAN = las cabezas se mueven de un extremo a otro del disco, atendiendo las solicitudes
# que se van encontrando

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

# Creo una función para ejecutar el proceso del elevador 
def algoritmo_scan(peticiones, posicion_actual, direction):
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
    
    # Como el sistema es tipo elevador y va de un extremo a otro, le vamos a agregar el último
    # valor de los extremos según la dirección que tome al iniciar el algoritmo.
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
    
    # Ordeno las listas y reverso left para poder realizar los calculos sin errores y en el orden que corresponde
    left.sort()
    right.sort()
    left = list(reversed(left))
    print("_______________________________________________________________________")
    print(f"Secuencia de Left: {left}")
    print(f"Secuencia de Right: {right}")
    print("_______________________________________________________________________\n")
    
    # Algoritmo que pone en marcha el elevador
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
            # Cambio el valor de direction para poder realizar el recorrido de derecha
            direction = "right"

        # Repito el mismo proceso que en left
        elif (direction == "right"):
            for i in right:
                tiempo_de_espera += desplazamiento
                tiempoEspera.append(tiempo_de_espera)
                if i > posicion_actual:
                    desplazamiento = i - posicion_actual
                    operation = "(" + str(i) + "-" + str(posicion_actual) + ")"
                    movimiento_realizado.append(operation)
                    
                
                elif i < posicion_actual:
                    desplazamiento = posicion_actual - i
                    operation = "(" + str(posicion_actual) + "-" + str(i) + ")"
                    movimiento_realizado.append(operation)
                
                posicion_actual = i            
                secuencia.append(posicion_actual)
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
print(f"La secuencia de servicio del algoritmo SCAN es: {peticiones}")
print(f"El encabezado actual está en el N° {posicion_actual}")
print(f"Dirección del cilindro: '{direction}'")
print("--------------------------------------------------------------------------------------------------------") 
# Pongo en marcha la función del elevador
algoritmo_scan(peticiones, posicion_actual, direction)
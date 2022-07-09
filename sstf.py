# SSTF es otro tipo de algoritmo de programación. En este tipo de programación de disco, el
# trabajo que tiene menos tiempo de búsqueda se ejecutará primero. Entonces, en la
# programación SSTF (tiempo de búsqueda más corto primero), primero tenemos que calcular
# el tiempo de búsqueda. Y después de calcular el tiempo de búsqueda, cada solicitud se
# atenderá en función del tiempo de búsqueda. La solicitud que está cerca del brazo del
# disco se ejecutará primero.


# En este algoritmo voy a establecer un tamaño de 10 procesos/peticiones
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

# Tamaño de la dirección almacenada (procesos o peticiones)
size = 10

# Establezco una posición aleatoria en el disco.
posicion_actual = random.randint(0, 999)

# Ejecuto el código que va a crear el orden de pista aleatoria y va a almacenarlo en la lista vacía.
peticiones = []
for p in range(size):
    part = random.randint(0, 999)
    peticiones.append(part)
    
print("\n--------------------------------------------------------------------------------------------------------")
print(f"La secuencia de servicio del algoritmo SSTF es: {peticiones}")
print(f"El encabezado actual está en el N° {posicion_actual}")
print("--------------------------------------------------------------------------------------------------------\n") 

# Creo una lista vacia para almacenar los movimientos realizados en la busqueda de cada peticion
cantidad_movimientos = []
# Creo una lista vacia para almacenar los procesos en el orden que se dieron al más cercano de la posicion del disco
procesos = []
# Creo una lista vacía donde almaceno las operaciones realizadas de los movimientos de las peticiones
movimiento_realizado = []
# Inicializo en cero el numero mas cercano de la posicion del disco
numero_cercano = 0

# maximo = max(peticiones, key=lambda x:abs(x-peticiones[0]))
# minimo = min(peticiones, key=lambda x:abs(x-peticiones[0]))

# Para calcular la cantidad de movimientos establesco el tamaño del disco en 1000
size_partition = 1000
# Inicio el recorrido del disco
for x in range(size_partition):
    # Inicio la lectura de peticiones dentro del disco
    for i in peticiones:
        # Busco el número más cercano de la posición actual
        numero_cercano = min(peticiones, key=lambda x:abs(x-posicion_actual))
        # Para evitar errores en los calculos de los mivimientos y obtener un resultado correcto, 
        # establezco condiciones y voy resolviendo en base a cada condicion
        if numero_cercano > posicion_actual:
            # Realizo el calculo del movimiento
            movimiento = numero_cercano - posicion_actual
            # Almaceno ese calculo del movimiento
            cantidad_movimientos.append(movimiento)
            # Armo un string para visibilizar el calculo del movimiento realizado
            operation = "(" + str(numero_cercano) + "-" + str(posicion_actual) + ")"
            # Almaceno el string armado
            movimiento_realizado.append(operation)
        elif numero_cercano < posicion_actual:
            movimiento = posicion_actual - numero_cercano
            cantidad_movimientos.append(movimiento)
            operation = "(" + str(posicion_actual) + "-" + str(numero_cercano) + ")"
            movimiento_realizado.append(operation)
        
        # Almaceno el numero cercano encontrado para luego visibilizar de forma 
        # resumida los movimientos realizados de las peticiones
        procesos.append(numero_cercano)
        # Actualizo la posición actual
        posicion_actual = numero_cercano
        # Elimino el número cernano de la lista peticiones para evitar repeticiones en los mivimientos
        # y errores de calculos
        peticiones.remove(numero_cercano)
        
# Realizo un algoritmo para sumar los movimientos realizados
mov = 0
for m in cantidad_movimientos:
    mov += m

print("--------------------------------------------------------------------------------------------------------") 
print(f"La distancia total que mueve la cabeza se calculo de la siguiente manera:\n{movimiento_realizado}")
print("--------------------------------------------------------------------------------------------------------\n")
print("--------------------------------------------------------------------------------------------------------") 
print(f"Cantidad de movimientos: {mov}")
print(f"Peticiones: {procesos}")
print("--------------------------------------------------------------------------------------------------------\n")
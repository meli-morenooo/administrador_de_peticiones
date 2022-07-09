# Las siglas FCFS significan en inglés First Come First Served (Primero en llegar, Primero en ser Servido),
# dentro de los algoritmos de Planificación de la CPU, este es el más sencillo.
# La carga de trabajo se procesa simplemente en un orden de llegada. Por no tener
# en consideración el estado del sistema ni las necesidades de recursos de los procesos
# individuales, la planificación FCFS puede dar lugar a pobres rendimientos.
# Este algoritmo posee un alto tiempo de respuesta de la CPU pues el proceso no abandona
# la CPU hasta no haber concluido pues es un algoritmo Sin Desalojo (No Apropiativo). La planificación
# FCFS elimina la noción e importancia de las prioridades de los procesos.


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

# Creo una lista vacía donde se van a almacenar los numeros de pista.
peticiones = []

# Ejecuto el código que va a crear el orden de pista aleatoria y va a almacenarlo en la lista vacía.
for i in range(size):
    i = random.randint(0, 1000)
    peticiones.append(i)

print("\n--------------------------------------------------------------------------------------------------------")
print(f"La secuencia de servicio del algoritmo FCFS/FIFO es: {peticiones}")
print("--------------------------------------------------------------------------------------------------------\n")

# Creo una segunda lista vacia para almacenar los procesos y simular la entrega de la direccion
peticiones2 = []
# A cada proceso o petición lo identifico con la variable "p" y le agrego el n° de orden, ej: Proceso N° 01, Proceso N° 03..Proceso N° 10)
p = "Proceso N° "
# Creo la variable contador para agregar a la variable p
contador1 = 0
contador2 = 10

print("_________________________|_________________________")
print("________PILA_____________|_____________PILA________")
print("_______ENTRADA___________|____________SALIDA_______")

for i in peticiones:
    contador1 += 1
    # Para lograr la visibilidad simulada de una pila con su orden de entrada de las peticiones
    # indico condiciones para lograr el orden deseado en pila de entrada y en pila de salida
    if contador1 > 0 and contador1 < 10:
        if contador2 > 0 and contador2 < 10:
            print(f"{p}0{contador2}: {peticiones[contador2-1]}       |     {p}0{contador1}: {i}")
            print("_________________________|_________________________")           

        else:
            print(f"{p}{contador2}: {peticiones[contador2-1]}     |     {p}0{contador1}: {i}")
            print("_________________________|_________________________")           
    else:
        if contador2 > 0 and contador2 < 10:
            print(f"{p}0{contador2}: {peticiones[contador2-1]}      |     {p}{contador1}: {i}")
            print("_________________________|_________________________")           
        else:
            print(f"{p}{contador2}: {peticiones[contador2-1]}     |     {p}{contador1}: {i}")
            print("_________________________|_________________________")           
    
    contador2 -= 1
    peticiones2.append(i)

print("\n--------------------------------------------------------------------------------------------------------")
print(f"Lista de peticiones: {peticiones2}")
print("--------------------------------------------------------------------------------------------------------\n")
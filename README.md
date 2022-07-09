# Administrador de peticiones
Construir un Algoritmo (Python preferiblemente) que SIMULE la Administración de Peticiones para recuperar los bloques (sectores)  de un archivo de la unidad de almacenamiento secundaria.


### A) Recibe como parámetro una lista de sectores  y el método de administración según este esquema (o similar)

- FCFS: (FIRST COME, FIRTS SERVED) Servicio por orden de llegada  similar a FIFO  (First In, First Out) Primero en Entrar, Primero en Salir

![Prueba de FCFS](https://user-images.githubusercontent.com/87624300/178117858-320d95ad-7a7d-43a5-b24d-e8c798fb744f.jpg)

- SSTF: (SHORTEST SEEK TIME FIRST) El MAS CERCANO A LA POSICION ACTUAL (de la cabeza lectora)  o algoritmo de tiempo de búsqueda más corto primero.

![Prueba de SSTF](https://user-images.githubusercontent.com/87624300/178117939-9b290f34-c824-45e7-aeb2-1774800cfc09.jpg)

- SCAN: (SCAN) también se conoce como algoritmo de elevador o de EXPLORACION.

![Prueba de Scan](https://user-images.githubusercontent.com/87624300/178117948-2fcdf9da-ac83-4f4b-a3e1-c7a75565880e.jpg)

- C-SCAN: (CIRCULAR SCAN), variante de SCAN llamada EXPLORACION CIRCULAR

![Prueba de C-Scan](https://user-images.githubusercontent.com/87624300/178117996-2a786a98-f75b-47a2-b21e-55be324eb6f9.jpg)

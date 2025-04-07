# Tarea-6

Implementar en los grupos de trabajo un programa que resuelva el problema de cubrimiento de vértices implementando los siguientes 4 algoritmos:

Escoger arbitrariamente un eje, incluir los dos vértices conectados, descartar todos los demás ejes conectados por los vertices escogidos y repetir hasta que no queden ejes.
Escoger el vértice de mayor grado, descartar los ejes que llegan al vertice escogido y repetir hasta que no queden ejes.
Escoger arbitrariamente un eje, incluir el vértice de mayor grado de los dos vértices conectados por el eje, descartar todos los demás ejes conectados por el vértice escogido y repetir hasta que no queden ejes.
Escoger aleatoriamente un eje, incluir aleatoriamente uno de los dos vértices conectados, descartar todos los demás ejes conectados por el vértice escogido y repetir hasta que no queden ejes.

El programa debe recibir un archivo de texto con los ejes del grafo y un número que indique el algoritmo a ejecutar. Cada linea del archivo debe contener una pareja de números que representan los dos vértices conectados, separados por tab. El programa no pueden hacer ninguna suposición acerca del sistema operativo o del sistema de archivos del usuario.

El programa debe imprimir los vertices del cubrimiento encontrado y el tamaño del conjunto de vértices.

Realizar pruebas con diferentes tipos de grafos de 100, 1000 y 10000 vértices. Calcular una tabla con los tamaños de las soluciones encontradas y los tiempos de ejecución de todos los experimentos.

Para los algoritmos 2 y 3 encontrar ejemplos en los que la solución que encuentra el algoritmo sea peor que 2 veces el número de vértices óptimo.

Entregar un archivo zip con el código fuente del programa, un README que explique la forma en que se debe usar y un archivo de excel con los resultados de los experimentos.

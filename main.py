import time
from algorithms.vertex_cover_1 import vertex_cover_1
from algorithms.vertex_cover_2 import vertex_cover_2
from algorithms.vertex_cover_3 import vertex_cover_3
from algorithms.vertex_cover_4 import vertex_cover_4


# Lee el archivo input.txt, que contiene el grafo y el algoritmo a usar
def import_graph():

    vertexList = []
    algorithm = 0

    with open("input.txt", "r") as f:

        for line in f:
            line = line.strip()
            if not line:
                break

            # Separa la linea
            nodes = line.split("\t")

            # Separa los nodos
            node1 = nodes[0]
            node2 = nodes[1]

            # guarda el nodo como un par de nodos
            vertexList.append((node1, node2))

        # Lee el algoritmo
        algorithm = int(f.readline()[-1].strip())

    return vertexList, algorithm


# Dependiedo del algoritmo, llama a la funcion correspondiente del archivo algorithms.py
def solve_vertex_cover(vertexList, algorithm):

    if algorithm == 1:
        return vertex_cover_1(vertexList)
    elif algorithm == 2:
        return vertex_cover_2(vertexList)
    elif algorithm == 3:
        return vertex_cover_3(vertexList)
    elif algorithm == 4:
        return vertex_cover_4(vertexList)
    else:
        raise ValueError("Algoritmo invalido. Debe ser un numero entre 1 y 4.")


def main():

    # Importa el grafo
    graph, algorithm = import_graph()

    # Comienza a contar el tiempo
    start_time = time.time()

    # Resuelve el problema de vertex cover
    vertex_cover = solve_vertex_cover(graph, algorithm)

    # Termina de contar el tiempo
    end_time = time.time()

    # Imprime el resultado
    print("Resultados del algoritmo ", str(algorithm) + ":\n")

    # Calcula el tiempo de ejecucion
    ms_time = (end_time - start_time) * 1000
    print("Tiempo de ejecucion: ", round(ms_time, 5), "ms")
    print("Numero de nodos en el vertex cover: ", len(vertex_cover))

    # Imprime el vertex cover
    print("Nodos en el vertex cover: ", vertex_cover)


if __name__ == "__main__":
    main()

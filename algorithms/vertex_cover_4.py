import random


def vertex_cover_4(edges):
    """
    Escoger aleatoriamente un eje, incluir aleatoriamente uno de los dos
    vértices conectados, descartar todos los demás ejes conectados por el
    vértice escogido y repetir hasta que no queden ejes.

    Esto es básicamente el algoritmo 3 pero randomizado.
    """

    # Inicializa el conjunto de cobertura y los ejes no cubiertos
    vertex_cover = set()
    uncovered_edges = set(edges)

    # Construye el grafo como una lista de adyacencia
    graph = {}
    for node1, node2 in edges:
        if node1 not in graph:
            graph[node1] = set()
        if node2 not in graph:
            graph[node2] = set()
        graph[node1].add(node2)
        graph[node2].add(node1)

    # Mientras haya ejes no cubiertos
    while uncovered_edges:
        # Escoge un eje aleatorio
        edge = random.choice(list(uncovered_edges))
        node1, node2 = edge

        # Escoge aleatoriamente uno de los dos extremos
        if random.random() < 0.5:
            chosen_node = node1
        else:
            chosen_node = node2

        # Verifica si el nodo aún está en el grafo
        if chosen_node not in graph:
            uncovered_edges.discard(edge)
            continue

        # Agrega el nodo al conjunto de cobertura
        vertex_cover.add(chosen_node)

        # Elimina los ejes que contengan el nodo
        for neighbor in list(graph[chosen_node]):
            uncovered_edges.discard((chosen_node, neighbor))
            uncovered_edges.discard((neighbor, chosen_node))
            graph[neighbor].remove(chosen_node)

        # Elimina el nodo del grafo
        graph.pop(chosen_node)

    return vertex_cover

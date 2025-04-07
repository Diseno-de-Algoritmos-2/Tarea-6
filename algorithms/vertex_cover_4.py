import random


def vertex_cover_4(vertexList):
    """
    Escoger aleatoriamente un eje, incluir aleatoriamente uno de los dos
    vértices conectados, descartar todos los demás ejes conectados por el
    vértice escogido y repetir hasta que no queden ejes.

        Esto es basicamente el algoritmo 3 pero randomizado.
    """

    # Inicializa el conjunto de cobertura
    uncovered_edges, vertex_cover = vertexList, []

    # Organiza el grafo en un diccionario como una lista de adyacencia
    graph = {}
    for edge in vertexList:
        node1, node2 = edge
        if node1 not in graph: graph[node1] = []
        if node2 not in graph: graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1)

    # Mientras haya ejes no cubiertos
    while uncovered_edges:

        # Escoge un eje aletorio
        edge = random.choice(uncovered_edges)

        # escoge aleatoriamente uno de los dos extremos
        max_node = random.choice(edge)

        # Agrega el nodo al conjunto de cobertura
        if max_node not in vertex_cover: vertex_cover.append(max_node)

        # Elimina los ejes que contengan el nodo
        for neighbor in graph[max_node]:
            edge = (max_node, neighbor)
            edgev = (neighbor, max_node)
            if edge in uncovered_edges: uncovered_edges.remove(edge)
            if edgev in uncovered_edges: uncovered_edges.remove(edgev)

        # Elimina el nodo del grafo
        graph.pop(max_node)
        for neighbor in graph:
            if max_node in graph[neighbor]: graph[neighbor].remove(max_node)

    return vertex_cover

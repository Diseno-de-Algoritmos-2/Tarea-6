def vertex_cover_3(edges):
    """
    Escoger arbitrariamente un eje, incluir el vértice de mayor grado
    de los dos vértices conectados por el eje, descartar todos los demás
    ejes conectados por el vértice escogido y repetir hasta que no queden ejes.

    Esto es básicamente el algoritmo 1 y 2 combinados.
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
        # Escoge un eje arbitrario
        edge = next(iter(uncovered_edges))
        node1, node2 = edge

        # Verifica si ambos nodos aún están en el grafo
        if node1 not in graph or node2 not in graph:
            uncovered_edges.discard(edge)
            continue

        # Compara cuál extremo tiene mayor grado
        node1_degree = len(graph[node1])
        node2_degree = len(graph[node2])

        if node1_degree >= node2_degree:
            max_node = node1
        else:
            max_node = node2

        # Agrega el nodo al conjunto de cobertura
        vertex_cover.add(max_node)

        # Elimina los ejes que contengan el nodo
        for neighbor in list(graph[max_node]):
            uncovered_edges.discard((max_node, neighbor))
            uncovered_edges.discard((neighbor, max_node))
            graph[neighbor].remove(max_node)

        # Elimina el nodo del grafo
        graph.pop(max_node)

    return vertex_cover

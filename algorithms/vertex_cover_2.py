def vertex_cover_2(edges):
    """
    Escoger el vértice de mayor grado, descartar los ejes que llegan al
    vértice escogido y repetir hasta que no queden ejes.
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

        # Escoge el nodo de mayor grado usando un bucle explícito
        max_node = None
        max_degree = -1
        for node, neighbors in graph.items():
            degree = len(neighbors)
            if degree > max_degree:
                max_degree = degree
                max_node = node

        # Verifica si se encontró un nodo válido
        if max_node is None:
            break

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

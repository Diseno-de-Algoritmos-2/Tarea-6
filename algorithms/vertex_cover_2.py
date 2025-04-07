def vertex_cover_2(vertexList):
    """
    Escoger el vértice de mayor grado, descartar los ejes que llegan al
    vertice escogido y repetir hasta que no queden ejes.
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

        # Escoge el nodo de mayor grado
        max_node = None
        max_degree = -1

        for node, neighbors in graph.items():
            if len(neighbors) > max_degree:
                max_degree = len(neighbors)
                max_node = node

        if max_node is None:
            break

        # Agrega el nodo al conjunto de cobertura
        if max_node not in vertex_cover: vertex_cover.append(max_node)

        # Elimina los ejes que contengan el nodo
        for neighbor in graph[max_node]:
            edge = (max_node, neighbor)
            edgev = (neighbor, max_node)
            if edge in uncovered_edges: uncovered_edges.remove(edge)
            if edgev in uncovered_edges:uncovered_edges.remove(edgev)

        # Elimina el nodo del grafo
        graph.pop(max_node)
        for neighbor in graph:
            if max_node in graph[neighbor]: graph[neighbor].remove(max_node)

    return vertex_cover

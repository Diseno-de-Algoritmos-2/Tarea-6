def vertex_cover_1(vertexList):
    """
    Algoritmo 1: Escoger arbitrariamente un eje e incluir sus extremos en el conjunto de cobertura,
    eliminar los ejes conectados a esos nodos y repetir el proceso hasta que no queden ejes.
    """
    
    # Inicializa el conjunto de cobertura
    uncovered_edges = vertexList
    vertex_cover = []
    
    # Mientras haya ejes no cubiertos
    while uncovered_edges:
        
        # Escoge un eje arbitrario
        edge = uncovered_edges[0]
        
        # Elimina los ejes que contengan ALGUNO de los nodos de ese eje
        for node in edge:
            for uncovered_edge in uncovered_edges:
                if node in uncovered_edge:
                    uncovered_edges.remove(uncovered_edge)
                    
        # Agrega los nodos del eje al conjunto de cobertura
        for node in edge:
            if node not in vertex_cover:
                vertex_cover.append(node)
                
    return vertex_cover
        
        
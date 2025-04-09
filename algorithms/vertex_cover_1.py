def vertex_cover_1(edges):
    """
    Escoger arbitrariamente un eje e incluir sus extremos en el conjunto de cobertura,
    eliminar los ejes conectados a esos nodos y repetir el proceso hasta que no queden ejes.
    """

    # Inicializa el conjunto de cobertura
    vertex_cover = set()

    # Mientras haya ejes no cubiertos
    while edges:
        # Escoge un eje arbitrario
        edge = next(iter(edges))

        # Agrega los nodos del eje al conjunto de cobertura
        vertex_cover.update(edge)

        # Elimina los ejes que contengan ALGUNO de los nodos de ese eje
        edges = {e for e in edges if not (e[0] in edge or e[1] in edge)}

    return vertex_cover

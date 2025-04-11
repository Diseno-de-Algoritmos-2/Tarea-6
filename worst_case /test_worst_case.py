from time import time

# --------------------- Algoritmo 2 ---------------------
def vertex_cover_2(edges):
    vertex_cover = set()
    uncovered_edges = set(edges)
    graph = {}
    for node1, node2 in edges:
        graph.setdefault(node1, set()).add(node2)
        graph.setdefault(node2, set()).add(node1)
    while uncovered_edges:
        max_node = max(graph, key=lambda x: len(graph[x]), default=None)
        if max_node is None:
            break
        vertex_cover.add(max_node)
        for neighbor in list(graph[max_node]):
            uncovered_edges.discard((max_node, neighbor))
            uncovered_edges.discard((neighbor, max_node))
            graph[neighbor].discard(max_node)
        del graph[max_node]
    return vertex_cover

# --------------------- Algoritmo 3 ---------------------
def vertex_cover_3(edges):
    vertex_cover = set()
    uncovered_edges = set(edges)
    graph = {}
    for node1, node2 in edges:
        graph.setdefault(node1, set()).add(node2)
        graph.setdefault(node2, set()).add(node1)
    while uncovered_edges:
        edge = next(iter(uncovered_edges))
        node1, node2 = edge
        if node1 not in graph or node2 not in graph:
            uncovered_edges.discard(edge)
            continue
        max_node = node1 if len(graph[node1]) >= len(graph[node2]) else node2
        vertex_cover.add(max_node)
        for neighbor in list(graph[max_node]):
            uncovered_edges.discard((max_node, neighbor))
            uncovered_edges.discard((neighbor, max_node))
            graph[neighbor].discard(max_node)
        del graph[max_node]
    return vertex_cover

# --------------------- Leer grafo desde archivo ---------------------
def leer_grafo_desde_txt(ruta):
    edges = set()
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            if linea.strip():
                a, b = map(int, linea.strip().split('\t'))
                edges.add((a, b))
    return edges

# --------------------- Ejecutar y mostrar resultados ---------------------
def probar_algoritmo(nombre, edges, algoritmo, optimo):
    inicio = time()
    if algoritmo == 2:
        resultado = vertex_cover_2(edges)
    elif algoritmo == 3:
        resultado = vertex_cover_3(edges)
    else:
        print("Algoritmo no válido")
        return
    fin = time()
    
    tamaño = len(resultado)
    razon = tamaño / optimo
    tiempo = fin - inicio

    print(f"\n--- {nombre} (Algoritmo {algoritmo}) ---")
    print(f"  Solución encontrada: {resultado}")
    print(f"  Tamaño de la solución: {tamaño}")
    print(f"  Tamaño óptimo: {optimo}")
    print(f"  Razón: {razon:.2f}")
    print(f"  Tiempo de ejecución: {tiempo:.6f} s")

    if razon >= 2.0:
        print("  [!] El algoritmo generó una solución peor que el doble del óptimo.")
    else:
        print("  [OK] La solución está dentro del rango esperado.")

# --------------------- Ejecutar desde archivo ---------------------
if __name__ == "__main__":
    archivo = "grafo_peor_caso.txt" 
    optimo = 10  

    try:
        edges = leer_grafo_desde_txt(archivo)
        probar_algoritmo("Grafo cargado desde archivo", edges, algoritmo=2, optimo=optimo)
        probar_algoritmo("Grafo cargado desde archivo", edges, algoritmo=3, optimo=optimo)
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo: {archivo}")
    except Exception as e:
        print(f"[ERROR] Falló la ejecución: {e}")

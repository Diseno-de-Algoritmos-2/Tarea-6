import matplotlib.pyplot as plt
import random
import time
import sys
import os

# Agrega el directorio raíz al path para poder importar los módulos correctamente
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importaciones correctas
from algorithms.vertex_cover_1 import vertex_cover_1
from algorithms.vertex_cover_2 import vertex_cover_2
from algorithms.vertex_cover_3 import vertex_cover_3
from algorithms.vertex_cover_4 import vertex_cover_4

from graph_generator import generate_graph


# Lee el archivo input.txt, que contiene el grafo y el algoritmo a usar
def import_graph(file_path="input.txt"):

    vertexList = []
    with open(file_path, "r") as f:

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

    return vertexList

def monte_carlo(N_Simulations):

    # --- Simulación de montecarlo para cada algoritmo

    # Estructuras de datos para guardar los resultados
    results = {
        "vertex_cover_1": [],
        "vertex_cover_2": [],
        "vertex_cover_3": [],
        "vertex_cover_4": []
    }

    # 0. Simulación de montecarlo
    for i in range(N_Simulations):

        # 1. Creamos un grafo aleatorio que se guardará en el archivo input.txt
        N_Graphs = [100, 250, 500]
        num_nodes = random.choice(N_Graphs)
        generate_graph(num_nodes, edge_probability=0.33)

        # 2. Importa el grafo
        graph = import_graph("simulations/input.txt")

        # ALGORITMOS 
        # _____________

        start_time = time.perf_counter()
        vertex_cover = vertex_cover_1(graph.copy())
        end_time = time.perf_counter()
        ms_time = round((end_time - start_time) * 1000, 7)
        results["vertex_cover_1"].append((num_nodes, len(vertex_cover), ms_time))

        start_time = time.perf_counter()
        vertex_cover = vertex_cover_2(graph.copy())
        end_time = time.perf_counter()
        ms_time = round((end_time - start_time) * 1000, 7)
        results["vertex_cover_2"].append((num_nodes, len(vertex_cover), ms_time))

        start_time = time.perf_counter()
        vertex_cover = vertex_cover_3(graph.copy())
        end_time = time.perf_counter()
        ms_time = round((end_time - start_time) * 1000, 7)
        results["vertex_cover_3"].append((num_nodes, len(vertex_cover), ms_time))

        start_time = time.perf_counter()
        vertex_cover = vertex_cover_4(graph.copy())
        end_time = time.perf_counter()
        ms_time = round((end_time - start_time) * 1000, 7)
        results["vertex_cover_4"].append((num_nodes, len(vertex_cover), ms_time))

    return results

def plot_results(results):
    
    sizes = [100, 250, 500]
    
    print("\n        RESUMEN        \n")
    
    print("\nAverage Execution Time (ms):")
    headers = ["Graph Size"] + list(results.keys())
    print(" | ".join(headers))
    print("-" * (sum(len(h) for h in headers) + len(headers) - 1))
    
    for size in sizes:
        row = [str(size)]
        for algo, data in results.items():
            size_data = [entry for entry in data if entry[0] == size]
            if size_data:
                avg_time = sum(entry[2] for entry in size_data) / len(size_data)
                row.append(f"{avg_time:.4f}")
            else:
                row.append("N/A")
        print(" | ".join(row))
        
    print("\nAverage Vertex Cover Size:")
    print(" | ".join(headers))
    print("-" * (sum(len(h) for h in headers) + len(headers) - 1))
    
    for size in sizes:
        row = [str(size)]
        for algo, data in results.items():
            size_data = [entry for entry in data if entry[0] == size]
            if size_data:
                avg_vertices = sum(entry[1] for entry in size_data) / len(size_data)
                row.append(f"{avg_vertices:.2f}")
            else:
                row.append("N/A")
        print(" | ".join(row))

    # ----------------------------------------------------------
    
    for size in sizes:

        times_by_size = {}
        vertices_by_size = {}
        
        for algo, data in results.items():
            size_data = [entry for entry in data if entry[0] == size]
            
            if size_data:
                times_by_size[algo] = [entry[2] for entry in size_data]
                vertices_by_size[algo] = [entry[1] for entry in size_data]
        
        if not times_by_size:
            continue
            
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        fig.suptitle(f'Graph Size: {size} nodes', fontsize=16)
        
        ax1.boxplot(list(times_by_size.values()), tick_labels=list(times_by_size.keys()))
        ax1.set_title('Execution Time Comparison')
        ax1.set_ylabel('Time (ms)')
        ax1.set_xticklabels(list(times_by_size.keys()), rotation=45)
        
        ax2.boxplot(list(vertices_by_size.values()), tick_labels=list(vertices_by_size.keys()))
        ax2.set_title('Vertex Cover Size Comparison')
        ax2.set_ylabel('Number of Vertices')
        ax2.set_xticklabels(list(vertices_by_size.keys()), rotation=45)
        
        plt.tight_layout()
        plt.savefig(f'simulations/algorithm_comparison_size_{size}.png')
        
    plt.show()


def main():
    N_Simulations = 25
    results = monte_carlo(N_Simulations)
    plot_results(results)

if __name__ == "__main__":
    main()

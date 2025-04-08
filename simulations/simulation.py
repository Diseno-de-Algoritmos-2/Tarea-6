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


def monte_carlo(N_Simulations):
    """
    Realiza simulaciones de Monte Carlo para comparar los algoritmos de vertex cover.
    """

    # Estructuras de datos para guardar los resultados
    results = {
        "vertex_cover_1": [],
        "vertex_cover_2": [],
        "vertex_cover_3": [],
        "vertex_cover_4": [],
    }

    # Tamaños de grafo y probabilidad de arcos
    graph_sizes = [100, 1000, 10000]
    edge_probability = 0.1

    for size in graph_sizes:
        for _ in range(N_Simulations):
            # Genera un grafo aleatorio
            graph = generate_random_graph(size, edge_probability)

            # ALGORITMO 1
            start_time = time.perf_counter()
            vertex_cover = vertex_cover_1(graph.copy())
            end_time = time.perf_counter()
            ms_time = round((end_time - start_time) * 1000, 7)
            results["vertex_cover_1"].append((size, len(vertex_cover), ms_time))

            # ALGORITMO 2
            start_time = time.perf_counter()
            vertex_cover = vertex_cover_2(graph.copy())
            end_time = time.perf_counter()
            ms_time = round((end_time - start_time) * 1000, 7)
            results["vertex_cover_2"].append((size, len(vertex_cover), ms_time))

            # ALGORITMO 3
            start_time = time.perf_counter()
            vertex_cover = vertex_cover_3(graph.copy())
            end_time = time.perf_counter()
            ms_time = round((end_time - start_time) * 1000, 7)
            results["vertex_cover_3"].append((size, len(vertex_cover), ms_time))

            # ALGORITMO 4
            start_time = time.perf_counter()
            vertex_cover = vertex_cover_4(graph.copy())
            end_time = time.perf_counter()
            ms_time = round((end_time - start_time) * 1000, 7)
            results["vertex_cover_4"].append((size, len(vertex_cover), ms_time))

        print(f"Simulaciones para el tamaño {size} completadas.")

    return results


def generate_random_graph(num_nodes, edge_probability):
    """
    Genera un grafo aleatorio no dirigido.

    :param num_nodes: Número de nodos en el grafo.
    :param edge_probability: Probabilidad de que exista un arco entre dos nodos.
    :return: Un conjunto de arcos (edges), donde cada arco es un frozenset de dos nodos.
    """
    edges = set()

    for node1 in range(num_nodes):
        for node2 in range(node1 + 1, num_nodes):
            if random.random() < edge_probability:
                edges.add((node1, node2))

    return edges


def plot_results(results):

    sizes = [100, 1000, 10000]

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
        fig.suptitle(f"Graph Size: {size} nodes", fontsize=16)

        ax1.boxplot(
            list(times_by_size.values()), tick_labels=list(times_by_size.keys())
        )
        ax1.set_title("Execution Time Comparison")
        ax1.set_ylabel("Time (ms)")
        ax1.set_xticklabels(list(times_by_size.keys()), rotation=45)

        ax2.boxplot(
            list(vertices_by_size.values()), tick_labels=list(vertices_by_size.keys())
        )
        ax2.set_title("Vertex Cover Size Comparison")
        ax2.set_ylabel("Number of Vertices")
        ax2.set_xticklabels(list(vertices_by_size.keys()), rotation=45)

        plt.tight_layout()
        plt.savefig(f"simulations/algorithm_comparison_size_{size}.png")


def main():
    N_Simulations = 25
    results = monte_carlo(N_Simulations)
    plot_results(results)


if __name__ == "__main__":
    main()

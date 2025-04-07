import networkx as nx

def generate_graph_networkx(num_nodes, edge_probability):
    
    return nx.gnp_random_graph(num_nodes, edge_probability)


def save_graph_to_file(edges, filename="simulations/input.txt"):

    with open(filename, "w") as f:
        for edge in edges:
            f.write(f"{edge[0]}\t{edge[1]}\n")
    
    print(f"Graph saved to {filename} with {len(edges)} edges")

def generate_graph(num_nodes, edge_probability=0.4):

    G = generate_graph_networkx(num_nodes, edge_probability)
    edges = G.edges()
    save_graph_to_file(edges, "simulations/input.txt")
import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
import csv

def initialize_ba_network(n=500, m=3):
    """Initialize a Barabási–Albert network."""
    return nx.barabasi_albert_graph(n, m)

def add_community_structure(graph, num_communities=3):
    """Assign nodes to communities representing work, family, and school."""
    community_labels = {}
    nodes = list(graph.nodes())

    # Shuffle nodes for random assignment
    random.shuffle(nodes)

    for i, node in enumerate(nodes):
        community_labels[node] = i % num_communities  # Assign community
    
    return community_labels

def visualize_network(graph, community_labels):
    """Plot the network with different colors for communities."""
    plt.figure(figsize=(10, 7))
    
    pos = nx.spring_layout(graph)  # Compute layout positions
    communities = set(community_labels.values())
    colors = plt.cm.viridis(np.linspace(0, 1, len(communities)))  # Assign colors to communities

    for community, color in zip(communities, colors):
        nodes = [node for node in graph.nodes if community_labels[node] == community]
        nx.draw_networkx_nodes(graph, pos, nodelist=nodes, node_color=[color], label=f"Community {community}", node_size=50)

    nx.draw_networkx_edges(graph, pos, alpha=0.5)
    plt.legend()
    plt.show()

def save_network_to_txt(graph, community_labels, filename="ba_network_output.txt"):
    """Save network details to a TXT file."""
    with open(filename, "w") as f:
        for node in graph.nodes():
            f.write(f"Node {node} (Community {community_labels[node]}): {list(graph.neighbors(node))}\n")
    print(f"Network details saved to {filename}")

def save_network_to_csv(graph, community_labels, filename="ba_network_output.csv"):
    """Save network details to a CSV file."""
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Node", "Community", "Connections"])
        for node in graph.nodes():
            writer.writerow([node, community_labels[node], ", ".join(map(str, graph.neighbors(node)))])
    print(f"Network details saved to {filename}")

# Create and visualize the BA network with community structure
ba_network = initialize_ba_network(n=100, m=3)
community_labels = add_community_structure(ba_network)
visualize_network(ba_network, community_labels)

# Save output to files
save_network_to_txt(ba_network, community_labels, "ba_network_output.txt")
save_network_to_csv(ba_network, community_labels, "ba_network_output.csv")

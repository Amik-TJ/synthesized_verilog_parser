import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import random
matplotlib.use('Qt5Agg')


def generate_random_features(G):
    for node in G.nodes():
        # Generate random color (yellow or red)
        color = random.choice(['yellow', 'red'])
        # Generate random size (big or small)
        size = random.choice(['big', 'small'])
        # Assign features as node attributes
        G.nodes[node]['color'] = color
        G.nodes[node]['size'] = size





def grapher(in_n, out_n, nodes, edges, verbose=0):
    G = nx.DiGraph()
    G.add_nodes_from(in_n)
    G.add_nodes_from(out_n)
    G.add_nodes_from(nodes)

    colour_map = []
    size = []


    generate_random_features(G)


    # Construct color and size lists based on nodes in the graph
    for node in G.nodes():
        if node in in_n:
            #colour_map.append('red')
            colour_map.append('#F7FF58')
        elif node in out_n:
            colour_map.append('#CE2D4F')
        else:
            colour_map.append('#4056F4')
        size.append(530 * len(node))

    for i in edges:
        for j in i[2]:
            G.add_edge(i[1], j, weight=6)

    if verbose:
        import os
        term_size = os.get_terminal_size()

        print("\n")
        [print('_', end='') for i in range(int((term_size.columns - 5) / 2))]
        print("PATHS", end='')
        [print('_', end='') for i in range(int((term_size.columns - 5) / 2))]
        print("\n")

        for i in in_n:
            for j in out_n:
                for path in nx.all_simple_paths(G, source=i, target=j):
                    print(path)

        print()

    pos = nx.spring_layout(G, k=7)
    nx.draw_networkx(G, with_labels=True, node_color=colour_map, node_size=size, arrowsize=20, pos=pos)
    plt.show()


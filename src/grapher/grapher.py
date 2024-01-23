import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import random
import json
import sys
matplotlib.use('Qt5Agg')


def read_parsed_lib_from_json(parsed_lib_json_path):
    with open(parsed_lib_json_path, 'r') as file:
        return json.load(file)



def generate_random_features(G):
    for node in G.nodes():
        # Generate random color (yellow or red)
        color = random.choice(['yellow', 'red'])
        # Generate random size (big or small)
        size = random.choice(['big', 'small'])
        # Assign features as node attributes
        G.nodes[node]['color'] = color
        G.nodes[node]['size'] = size





def grapher(in_n, out_n, nodes, edges, gate_type_and_name_mapping, parsed_lib_json_path, verbose=0):
    in_n =  [item for item in in_n if item.strip()]
    out_n =  [item for item in out_n if item.strip()]
    nodes =  [item for item in nodes if item.strip()]

    G = nx.DiGraph()
    G.add_nodes_from(in_n)
    G.add_nodes_from(out_n)
    G.add_nodes_from(nodes)


    colour_map = []
    size = []


    # generate_random_features(G)

    # Construct color and size lists based on nodes in the graph
    for node in G.nodes():
        if node in in_n:
            #colour_map.append('red')
            colour_map.append('#F7FF58')
        elif node in out_n:
            colour_map.append('#CE2D4F')
        else:
            colour_map.append('#4056F4')

        size.append(40 * len(node))



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

    # Removing empty node if there is any
    if ' ' in G:
        G.remove_node(' ')



    # Printing the graph
    # pos = nx.spring_layout(G, k=7)
    # nx.draw_networkx(G, with_labels=True, node_color=colour_map, node_size=size, arrowsize=20, pos=pos)
    # plt.show()


    # Adding node features
    add_node_features(G,gate_type_and_name_mapping, parsed_lib_json_path)





def add_node_features(G, gate_type_and_name_mapping, parsed_lib_json_path):

    parsed_json_feature_list = read_parsed_lib_from_json(parsed_lib_json_path)

    for node in G.nodes():
        if node in gate_type_and_name_mapping:
            gate_type = gate_type_and_name_mapping[node]
            feature_list = parsed_json_feature_list[gate_type]
            print(feature_list)
        else:
            print('Done Present in Dictionary', node)


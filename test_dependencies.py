
if __name__ == "__main__":
    try:
        import random
        print(f"random fungerer og gir deg {round(100 * random.random(), 1)}% sjangse for å vinne")
    except ModuleNotFoundError or ImportError:
         print("du har ikke random. HOw??")

    try:
        import argparse
        print("Du har argparse :)")

    except ModuleNotFoundError or ImportError:
        print("Du mangler argparse :O Installer den før det er for sent!")

    try:
        import numpy as np
        print("numpy har du ikke :O Neida, tuller bare!")
    except ModuleNotFoundError or ImportError:
        print("Du mangler numpy! Er du virkelig en maskinlæringsrådgiver, eller??")

    try:
        import matplotlib.pyplot as plt
        print("matplotlib er tilstede")    
    except ModuleNotFoundError or ImportError:
        print('pip install matplotlib of networkx dersom du ønsker å visualisere den beste reiseruten')
        exit()

    try:
        import networkx as nx
    except ModuleNotFoundError or ImportError:
        print('pip install networkx dersom du ønsker å visualisere den beste reiseruten')
        exit()
    tuples = [(-1, 1.25),  (1, 1.25), (-1.5, -1.5), (-1, -2), (0, -2), (1, -2),  (1.5, -1.5)]


    coordinates = [(xy, {"color": 'r', "pos": xy}) for xy in tuples]

    G = nx.Graph()
    G.add_nodes_from(coordinates)

    for i in range(2, len(tuples) -1):
        G.add_edge(tuples[i], tuples[i + 1])


    pos = nx.get_node_attributes(G, 'pos')
    node_colors = "red"
    
    sizes = [300, 300, 50, 50, 50, 50, 50]
    
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)

    nx.draw(G, pos, node_color=node_colors,  node_size=sizes)
    fig = plt.gcf()
    ax = plt.gca()
    plt.title("networkx fungerer også! Lykke til i Oppdal!!")
    ax.set_aspect('equal', adjustable='box')
    plt.show()
    print("networkx fungerer også! Lykketil i Oppdal!!")



    
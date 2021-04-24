import random
from utils import print_2d, numerate
import networkx as nx
from networkx.generators import harary_graph
import matplotlib.pyplot as plt


class Logic:
    def __init__(self):
        self.count_node = self.count_edge = 0
        self.graph = [[0 for _ in range(self.count_node)] for _ in range(self.count_node)]
        self.nx_graph = nx.Graph()

    def info_changed(self, node, edge):
        return int(node) != self.count_node or int(edge) != self.count_edge

    def save_info(self, node, edge):
        self.count_node, self.count_edge = int(node), int(edge)

    def load_nx_graph(self):
        pos = nx.spring_layout(self.nx_graph)
        nx.draw(self.nx_graph, pos, with_labels=True)
        labels = nx.get_edge_attributes(self.nx_graph, 'weight')
        nx.draw_networkx_edge_labels(self.nx_graph, pos, edge_labels=labels)
        plt.show()

    def get_count_node(self):
        return self.count_node

    def generate_random_graph(self):
        self.generate_empty_graph()
        self.nx_graph = harary_graph.hnm_harary_graph(self.count_node, self.count_edge)
        for u, v, data in self.nx_graph.edges(data=True):
            weight = random.randint(1, 15)
            data['weight'] = weight
            self.graph[u][v] = weight

    def generate_empty_graph(self):
        self.nx_graph = nx.Graph()
        self.graph = [[0 for _ in range(self.count_node)] for _ in range(self.count_node)]

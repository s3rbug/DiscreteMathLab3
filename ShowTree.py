import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import networkx as nx
from Logic import Logic
from PyQt5 import QtCore

import random


class ShowTree(QDialog):
    def __init__(self, logic: Logic, ):
        super(ShowTree, self).__init__()
        self.logic = logic
        self.setWindowFlags(
            QtCore.Qt.Window |
            QtCore.Qt.WindowCloseButtonHint |
            QtCore.Qt.WindowMaximizeButtonHint
        )
        self.setWindowTitle("Найкоротше остовне дерево")
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas, stretch=1)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.plot()

    def plot(self):
        self.figure.clear()
        graph = self.logic.nx_graph
        tree = nx.algorithms.minimum_spanning_tree(self.logic.nx_graph)
        edge_colors = ['green' if e in tree.edges else 'red' for e in graph.edges]
        labels = nx.get_edge_attributes(graph, 'weight')
        pos = nx.spring_layout(graph)
        nx.draw_networkx_nodes(graph, pos, node_size=500)
        nx.draw_networkx_labels(graph, pos)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        nx.draw_networkx_edges(graph, pos, arrows=True, edge_color=edge_colors)
        plt.axis('off')
        self.canvas.draw()

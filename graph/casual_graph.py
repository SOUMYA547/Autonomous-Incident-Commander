import networkx as nx

class CausalGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_relation(self, source, target):
        self.graph.add_edge(source, target)

    def find_root_cause(self):
        for node in self.graph.nodes:
            if self.graph.in_degree(node) == 0:
                return node
        return None
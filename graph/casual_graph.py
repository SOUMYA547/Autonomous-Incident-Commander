import networkx as nx

class CausalGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def build_graph(self, dependencies):
        for service, deps in dependencies.items():
            for dep in deps:
                self.graph.add_edge(dep, service)

    def trace_failure(self, failed_service):
        causes = list(nx.ancestors(self.graph, failed_service))
        return causes

    def visualize(self):
        print(self.graph.edges())
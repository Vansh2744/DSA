class Graph:
    def __init__(self):
        self.adj = {}

    def insert_vertex(self, vertex):
        if vertex not in self.adj:
            self.adj[vertex] = []

    def insert_edge(self, src, dest):
        self.insert_vertex(src)
        self.insert_vertex(dest)

        self.adj[src].append(dest)
        self.adj[dest].append(src)

    def print_graph(self):
        for k,v in self.adj.items():
            print(f"{k} -> {",".join(map(str, v))}")

graph = Graph()

graph.insert_edge(1,2)
graph.insert_edge(1,3)
graph.insert_edge(2,4)
graph.insert_edge(4,5)
graph.insert_edge(3,5)
graph.insert_edge(3,4)

graph.print_graph()
class Graph:
    def __init__(self, size):
        self.mat = [[0]*size for _ in range(size)]
        self.size = size

    def add_edge_in_graph(self, src, dest):
        if self.size > src >= 0 and self.size > dest >= 0:
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1
        else:
            print("Not valid source or destination")

    def add_edge_in_dir_graph(self, src, dest):
        if self.size > src >= 0 and self.size > dest >= 0:
            self.mat[src][dest] = 1
        else:
            print("Not valid source or destination")

    def add_edge_in_weighted_graph(self, src, dest, wt):
        if self.size > src >= 0 and self.size > dest >= 0:
            self.mat[src][dest] = wt
        else:
            print("Not valid source or destination")

    def print_matrix(self):
        for m in self.mat:
            print(" ".join(map(str, m)))

graph = Graph(4)

# graph.add_edge_in_graph(1,2)
# graph.add_edge_in_graph(2,3)
# graph.add_edge_in_graph(3,2)
# graph.add_edge_in_graph(0,1)

# graph.add_edge_in_dir_graph(1,2)
# graph.add_edge_in_dir_graph(2,3)
# graph.add_edge_in_dir_graph(0,2)
# graph.add_edge_in_dir_graph(0,1)

graph.add_edge_in_weighted_graph(1,2,5)
graph.add_edge_in_weighted_graph(2,3,10)
graph.add_edge_in_weighted_graph(0,2,3)
graph.add_edge_in_weighted_graph(0,1,7)

graph.print_matrix()
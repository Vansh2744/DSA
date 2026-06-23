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

    def dfs(self, src):
        visited = [False]*self.size
        stack = [src]

        while stack:
            v = stack.pop()
            if visited[v] == False:
                print(v, end="->")
                visited[v] = True

            for i in range(self.size):
                if self.mat[v][i] == 1 and visited[i] == False:
                    stack.append(i)

graph = Graph(6)

graph.add_edge_in_graph(1,2)
graph.add_edge_in_graph(1,3)
graph.add_edge_in_graph(2,4)
graph.add_edge_in_graph(3,4)
graph.add_edge_in_graph(3,5)
graph.add_edge_in_graph(4,5)

graph.dfs(1)
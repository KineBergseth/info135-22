# Task 3)

class Graph:
    graph = dict()
    searched = []

    def depth_first_search(self, node):
        if node not in self.searched:
            print("[", node, end="],")
            self.searched.append(node)
            if node in self.graph:
                for neighbour in self.graph[node]:
                    if neighbour in self.searched:
                        print('cycle found')
                    else:
                        self.depth_first_search(neighbour)


    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)

    def print_graph(self):
        print(self.graph)

    def print_edges(self):
        for node in self.graph:
            for neighbour in self.graph[node]:
                print("(", node, ",", neighbour, ")")


my_graph = Graph()
my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'B')
my_graph.add_edge('C', 'J')
my_graph.add_edge('D', 'E')
my_graph.add_edge('D', 'F')
my_graph.add_edge('E', 'C')
my_graph.add_edge('E', 'G')
my_graph.add_edge('F', 'H')
my_graph.add_edge('G', 'I')

result = my_graph.depth_first_search('B')
print(result)


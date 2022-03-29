# Task 3)

class Graph:
    graph = dict()
    searched = []

    def breadth_first_search(self, node):

        searched = [node]
        search_queue = [node]

        while search_queue:
            node = search_queue.pop(0)

            print("[", node, end=" ], ")

            if node in self.graph:
                for neighbour in self.graph[node]:
                    if neighbour not in searched:
                        searched.append(neighbour)
                        search_queue.append(neighbour)

    def depth_first_search(self, node):
        if node not in self.searched:
            self.searched.append(node)
            print("[", node, end=" ], ")
            if node in self.graph:
                for neighbour in self.graph[node]:
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
my_graph.add_edge('A', 'C')
my_graph.add_edge('B', 'C')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'E')
my_graph.add_edge('D', 'E')
my_graph.add_edge('D', 'G')
my_graph.add_edge('D', 'H')
my_graph.add_edge('E', 'F')
my_graph.add_edge('F', 'C')

result = my_graph.depth_first_search('A')
print(result)

"""
Får en importError pga import statementene dine øverst
"""
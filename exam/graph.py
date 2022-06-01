"""
A Graph class with relevant methods
"""


class Graph:
    graph = dict()
    searched = []

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)

    def print_graph(self):
        print(self.graph)

    def print_edges(self):
        for nodes in self.graph:
            for neighbour in self.graph[nodes]:
                print("(", nodes, ",", neighbour, ")")

    def breadth_first_search(self, node):
        searched = [node]
        search_queue = [node]
        while search_queue:
            node = search_queue.pop(0)
            print("[", node, end="],")
            if node in self.graph:
                for neighbour in self.graph[node]:
                    if neighbour not in searched:
                        searched.append(neighbour)
                        search_queue.append(neighbour)

    def depth_first_search(self, node):
        if node not in self.searched:
            print("[", node, end="],")

            self.searched.append(node)
            if node in self.graph:
                for neighbour in self.graph[node]:
                    self.depth_first_search(neighbour)

    # Method that removes the given node and the edges
    # Sets nodes that are only connected to the node that is about to be deleted as []
    def delete_edges(self, node):
        del self.graph[node]
        for nodes in self.graph:
            p = len(self.graph[nodes])
            print(p)
            if self.graph[nodes][p - 1] == node:
                del self.graph[nodes][p - 1]


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

my_graph.breadth_first_search('A')

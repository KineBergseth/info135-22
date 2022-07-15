"""
A Graph class with relevant methods
"""


class Graph:
    graph = dict()
    bfs_searched = []
    dfs_searched = []

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

    # https://www.programiz.com/dsa/graph-bfs forklaring her
    def breadth_first_search(self, node):
        bfs_searched = [node]
        search_queue = [node]
        while search_queue:
            node = search_queue.pop(0)
            print("[", node, end="],")
            if node in self.graph:
                for neighbour in self.graph[node]:
                    if neighbour not in bfs_searched:
                        bfs_searched.append(neighbour)
                        search_queue.append(neighbour)

    # https://www.programiz.com/dsa/graph-dfs forklaring her
    def depth_first_search(self, node):
        if node not in self.dfs_searched:
            print("[", node, end="],")

            self.dfs_searched.append(node)  # mark current node as visited
            if node in self.graph:
                for neighbour in self.graph[node]:
                    self.depth_first_search(neighbour)

    # Method that removes the given node and the edges to and from that node
    def delete_edges(self, node):
        if node in self.graph:  # check if node is in graph
            del self.graph[node]  # delete node and edges going to other nodes
        for nodes in self.graph:  # look at other nodes in graph
            for index, edge in enumerate(self.graph[nodes]):  # go through outgoing edges
                if edge == node:  # if a reference to deleted node exist delete it with index
                    del self.graph[nodes][index]

    def kris(self, node):
        if node not in self.graph:
            print('node not in graph!')
        self.graph.pop(node)



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

print('dfs:')
my_graph.depth_first_search('A')
print('\nbfs:')
my_graph.breadth_first_search('A')
print('\noriginal graph:')
my_graph.print_graph()
#my_graph.delete_edges('E')  # delete the node A and all edges connected to or form the node
my_graph.kris('E')
print('current graph:')
my_graph.print_graph()

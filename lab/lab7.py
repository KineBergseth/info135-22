
"""
Exercise 1

graph = [(“A”,“B”), (“A”,“C”), (“B”,“A”), (“C”,“A”), (“B”,“C”)]

Given the Graph graph, make a function remove_node(node) which removes all edges connected to a given node.
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

    # Method that removes the given node and the edges
    # Sets nodes that are only connected to the node that is about to be deleted as []
    def delete_edges(self, node):
        del self.graph[node]
        for nodes in self.graph:
            p = len(self.graph[nodes])
            print(p)
            if self.graph[nodes][p-1] == node:
                del self.graph[nodes][p-1]


my_graph1 = Graph()
my_graph1.add_edge('A', 'B')
my_graph1.add_edge('A', 'C')
my_graph1.add_edge('B', 'A')
my_graph1.add_edge('C', 'A')
my_graph1.add_edge('B', 'C')

print('before ')
my_graph1.print_graph()
#my_graph1.print_edges()
my_graph1.delete_edges('A')
print('After ')
my_graph1.print_graph()


class Course:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def hash_it(self):
        text = self.title + str(self.year)
        hash_value = hash(text)
        print(hash_value)


my_course = Course('INFO125', 2022)
my_course.hash_it()

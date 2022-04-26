print("\n Oppgave 3")


class Graph:
    graph = dict()
    searched = []

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)

    def depth_første_søk(self, node):
        if node not in self.searched:
            print("[", node, end="],")

            self.searched.append(node)
            if node in self.graph:
                for neighbour in self.graph[node]:
                    self.depth_første_søk(neighbour)


def build_my_graph2():
    my_graph = Graph()

    my_graph.add_edge("a", "b")
    my_graph.add_edge("a", "c")
    my_graph.add_edge("b", "c")
    my_graph.add_edge("b", "d")
    my_graph.add_edge("c", "e")
    my_graph.add_edge("d", "e")
    my_graph.add_edge("e", "f")
    my_graph.add_edge("f", "c")
    my_graph.add_edge("d", "g")
    my_graph.add_edge("d", "h")

    my_graph.depth_første_søk("a")


build_my_graph2()

# Issue 1
print('Issue 1: The correct answer is B. ')

# Issue 2
COLUMNS = "abcde"
NEW_QUEEN = len(COLUMNS)
ACCEPT = 1
CONTINUE = 2
ABANDON = 3


def extend(partial_sol):
    results = []
    row = len(partial_sol) + 1
    for column in COLUMNS:
        new_solution = list(partial_sol)
        new_solution.append(column + str(row))
        results.append(new_solution)
    return results


def examine(partial_sol):
    for i in range(len(partial_sol)):
        for j in range(i + 1, len(partial_sol)):
            if attacks(partial_sol[i], partial_sol[j]):
                return ABANDON
    if len(partial_sol) == NEW_QUEEN:
        return ACCEPT
    else:
        return CONTINUE


def attacks(p1, p2):
    column1 = COLUMNS.index(p1[0]) + 1
    row1 = int(p1[1])
    column2 = COLUMNS.index(p2[0]) + 1
    row2 = int(p2[1])
    return (row1 == row2 or column1 == column2 or abs(row1 - row2) == abs(column1 - column2))


def solve(partial_sol):
    exam = examine(partial_sol)
    if exam == ACCEPT:
        output.append(partial_sol)
    elif exam != ABANDON:
        for p in extend(partial_sol):
            solve(p)


def is_solution(candidate_solution):
    global output
    output = []
    solve([])
    candidate_solution = sorted(candidate_solution)
    for element in output:
        sortedlist = sorted(element)
        if candidate_solution == sortedlist:
            return 'valid! '
    else:
        return 'invalid! '


candidate_solution1 = ['d3', 'c1', 'e5', 'b4', 'a2']
candidate_solution2 = ['e4', 'a1', 'c5', 'd2', 'b1']
result1 = is_solution(candidate_solution1)
result2 = is_solution(candidate_solution2)
print('Issue 2: ')
print(f'Candidate solution 1: {result1} ')
print(f'Candidate solution 2: {result2} ')


# Issue 3:
class Graph:
    graph = dict()
    temp = []
    saml = []
    searched = []

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)

    def print_graph(self):
        print(self.graph)

    def breadth_first_search(self, node):
        searched = [node]
        search_queue = [node]
        self.temp.append(node)
        while search_queue:
            node = search_queue.pop(0)
            if node in self.graph:
                for neighbour in self.graph[node]:
                    self.temp.append(neighbour)

                    if neighbour not in searched:
                        searched.append(neighbour)
                        search_queue.append(neighbour)

    def depth_first_search(self, node):
        if node not in self.searched:
            self.searched.append(node)
            if node in self.graph:
                for neighbour in self.graph[node]:
                    self.depth_first_search(neighbour)
        self.temp.append(node)

    def find_cycle(self, node):
        my_graph.breadth_first_search(node)
        for element in self.temp:
            if element in self.saml:
                return 'Cycle found! '
            else:
                self.saml.append(element)
        return 'Cycle not found! '


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

result = my_graph.find_cycle('G')
print(f'Issue 3: {result} ')

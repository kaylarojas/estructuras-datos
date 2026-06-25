class UndirectedGraph:

    def __init__(self):
        self.graph = {}

    # Agregar un vértice
    def add_vertex(self, vertex):

        if vertex not in self.graph:
            self.graph[vertex] = []

    # Agregar una arista
    def add_edge(self, vertex1, vertex2):

        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    # Eliminar una arista
    def remove_edge(self, vertex1, vertex2):

        if vertex1 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)

        if vertex2 in self.graph:
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

    # Eliminar un vértice
    def remove_vertex(self, vertex):

        if vertex not in self.graph:
            return

        for neighbor in self.graph[vertex]:
            self.graph[neighbor].remove(vertex)

        del self.graph[vertex]

    # Mostrar el grafo
    def print_graph(self):

        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])

graph = UndirectedGraph()

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("D", "E")

graph.print_graph()
class DirectedGraph:

    def __init__(self):
        self.graph = {}

    # Agregar un vértice
    def add_vertex(self, vertex):

        if vertex not in self.graph:
            self.graph[vertex] = []

    # Agregar una arista dirigida
    def add_edge(self, origin, destination):

        self.add_vertex(origin)
        self.add_vertex(destination)

        self.graph[origin].append(destination)

    # Eliminar una arista
    def remove_edge(self, origin, destination):

        if origin in self.graph:
            if destination in self.graph[origin]:
                self.graph[origin].remove(destination)

    # Eliminar un vértice
    def remove_vertex(self, vertex):

        if vertex not in self.graph:
            return

        del self.graph[vertex]

        for v in self.graph:

            if vertex in self.graph[v]:
                self.graph[v].remove(vertex)

    # Mostrar el grafo
    def print_graph(self):

        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])

graph = DirectedGraph()

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("D", "E")

graph.print_graph()
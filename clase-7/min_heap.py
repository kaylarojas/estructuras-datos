class MinHeap:

    def __init__(self):
        self.heap = []

    # -------------------------
    # Funciones auxiliares
    # -------------------------

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    # -------------------------
    # Operaciones básicas
    # -------------------------

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    # -------------------------
    # Insertar
    # -------------------------

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    # -------------------------
    # Heapify Up
    # -------------------------

    def _heapify_up(self, index):

        while index > 0:

            parent = self.parent(index)

            if self.heap[index] < self.heap[parent]:

                self.heap[index], self.heap[parent] = \
                    self.heap[parent], self.heap[index]

                index = parent

            else:
                break

    # -------------------------
    # Extraer mínimo
    # -------------------------

    def extract_min(self):

        if self.is_empty():
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]

        self.heap[0] = self.heap.pop()

        self._heapify_down(0)

        return minimum

    # -------------------------
    # Heapify Down
    # -------------------------

    def _heapify_down(self, index):

        size = len(self.heap)

        while True:

            smallest = index

            left = self.left_child(index)
            right = self.right_child(index)

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:

                self.heap[index], self.heap[smallest] = \
                    self.heap[smallest], self.heap[index]

                index = smallest

            else:
                break

    # -------------------------
    # Mostrar heap
    # -------------------------

    def print_heap(self):
        print(self.heap)

heap = MinHeap()

heap.insert(40)
heap.insert(20)
heap.insert(60)
heap.insert(15)
heap.insert(80)
heap.insert(10)
heap.insert(50)

heap.print_heap()

print(heap.peek())

print(heap.extract_min())

heap.print_heap()
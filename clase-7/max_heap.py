class MaxHeap:

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
    # Operaciones principales
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

            if self.heap[index] > self.heap[parent]:

                self.heap[index], self.heap[parent] = \
                    self.heap[parent], self.heap[index]

                index = parent

            else:
                break

    # -------------------------
    # Extraer máximo
    # -------------------------

    def extract_max(self):

        if self.is_empty():
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        maximum = self.heap[0]

        self.heap[0] = self.heap.pop()

        self._heapify_down(0)

        return maximum

    # -------------------------
    # Heapify Down
    # -------------------------

    def _heapify_down(self, index):

        size = len(self.heap)

        while True:

            largest = index

            left = self.left_child(index)
            right = self.right_child(index)

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left

            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:

                self.heap[index], self.heap[largest] = \
                    self.heap[largest], self.heap[index]

                index = largest

            else:
                break

    # -------------------------
    # Mostrar heap
    # -------------------------

    def print_heap(self):
        print(self.heap)

heap = MaxHeap()

heap.insert(40)
heap.insert(20)
heap.insert(60)
heap.insert(15)
heap.insert(80)
heap.insert(10)
heap.insert(50)

heap.print_heap()
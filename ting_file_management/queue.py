class Queue:
    def __init__(self):
        self.fila = list()

    def __len__(self):
        return len(self.fila)

    def enqueue(self, value):
        return self.fila.append(value)

    def dequeue(self):
        return self.fila.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""

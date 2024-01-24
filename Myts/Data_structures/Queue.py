class SimpleQueue():
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self,item):
        if not self.is_empty(item):
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")
    def size(self):
        return len(self.items)
myqueuq = SimpleQueue()
myqueuq.enqueue(10)
myqueuq.enqueue(20)
myqueuq.enqueue(30)
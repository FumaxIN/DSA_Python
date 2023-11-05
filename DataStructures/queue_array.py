class Queue():
    def __init__(self):
        self._queue = [None]*5
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def first(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self._queue[self._front]

    def _resize(self, cap):
        print("resizing")
        old = self._queue
        self._queue = [None]*cap
        walk = self._front
        for i in range(self._size):
            self._queue[i] = old[walk]
            walk = (walk+1)%len(old)
        self._front=0

    def deque(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        ans = self._queue[self._front]
        self._queue[self._front] = None
        self._front = (self._front+1)%len(self._queue)
        self._size -= 1
        return ans

    def enqueue(self, val):
        if self._size == len(self._queue):
            self._resize(2*len(self._queue))
        avail = (self._front+self._size)%len(self._queue)
        self._queue[avail] = val
        self._size += 1
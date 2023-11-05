class Stack():
    def __init__(self):
        self._stack = []
        
    def __len__(self):
        return len(self._stack)

    def is_empty(self):
        return len(self._stack)==0

    def push(self, value):
        self._stack.append(value)

    def top(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        else:
            return self._stack[-1]

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        else:
            return self._stack.pop()
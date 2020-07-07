class Stack:
    def __init__(self):
        self.stos = []

    def is_empty(self):
        return self.stos == []

    def push(self, item):
        return self.stos.append(item)

    def pop(self):
        return self.stos.pop()

    def top(self):
        last = len(self.stos) - 1
        return self.stos[last]

    def __str__(self):
        return str(self.stos)


def posters():
    s = Stack()
    n = int(input())
    no_posters = 0
    for _ in range(n):
        lenght, height = map(int, input().split(' '))
        while not s.is_empty() and s.top() > height:
            s.pop()
        if s.is_empty() or s.top() < height:
            s.push(height)
            no_posters += 1
    return no_posters

print(posters())
""" Stwórz iterator i generator, które będą zwracały n liczb niepodzielnych przez m.np. dla n=10, m=3: [1, 2, 4, 5, 7, 8, 10, 11, 13, 14] """

class Div_Iterator:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.idx = 0
        self.generated_numbers = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        if self.generated_numbers >= self.n :
            raise StopIteration
        if self.idx % self.m != 0:
            self.generated_numbers += 1
            return self.idx
        else:
            return self.__next__()


var = Div_Iterator(10, 3)
for i in var:
    print(i)

def Div_generator(n, m):
    generated_numbers = 0
    idx = 1
    while generated_numbers != n:
        if idx % m != 0:
            generated_numbers += 1
            yield idx
        idx += 1

gen = Div_generator(10, 3)
for item in gen:
    print(item)

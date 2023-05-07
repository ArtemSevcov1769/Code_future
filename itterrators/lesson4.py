my_list = [2, 3, 4, 5, 6]
#
iterator = iter(my_list)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator)) stop iteration
import random
class RandomIter:
    def __init__(self, limit):
        self.limit = limit
        self.__reload = limit

    def __iter__(self):
        self.limit = self.__reload
        return self

    def __next__(self):
        if self.limit < 1:
            raise StopIteration
        self.limit -= 1
        return random.randint(0, 100)
i = ['vasya', 'kolya', 'katya', 'natasha']
class SeqIter:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.sequence)-1:
            raise StopIteration
        item = self.sequence[self.index]
        self.index += 1
        return item

# for i in SeqIter([1, 2, 3, 4, 5]):
#     print(i)

class Fibonachi:
    def __init__(self):
        # self.stop = stop
        self.index = 0
        self.current = 0
        self.next = 1

    def __iter__(self):
        return self

    def __next__(self):
        # if self.index > self.stop:
        #     raise StopIteration
        self.index += 1
        fib_num = self.current
        self.current, self.next = (self.next, self.current + self.next)
        return fib_num
for i in Fibonachi():
    print(i)

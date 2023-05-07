class MyFile():
    def __init__(self, filename, mode, encoding='UTF-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


class InfiniteIterator:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        return self.start

for i in InfiniteIterator(0):
    print(i)

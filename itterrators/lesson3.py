import time
class Timer():
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        t = time.time() - self.start
        print(f'Время работы кода {t}')

with Timer()as t:
    time.sleep(5)
    my_list = [x for x in range(100000000)]
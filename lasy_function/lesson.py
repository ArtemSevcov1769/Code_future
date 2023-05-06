import contextlib
# @contextlib.contextmanager
# def string_reversed(my_str):
#     print('входим в контекстный менеджер')
#     yield my_str[::-1]
#     print('leave')
#
# with string_reversed('hello, hello') as reversed_str:
#     print(f'выполняется код{reversed_str}')
#     for g in range(5):
#         print(g)

@contextlib.contextmanager
def error_handler(error):
    try:
        yield True
    except error:
        print('ERROR!')

with error_handler(IndexError):
    my_i = [1, 2]
    print(1234)
    print(my_i[0])
    print(my_i[10])
    print(1234.213455)
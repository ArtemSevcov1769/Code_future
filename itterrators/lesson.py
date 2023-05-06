class HWContMen:
    def __enter__(self):
        print('Входим в контекст')
        return 'hello world'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Выходим из него')
        print(1)

with HWContMen() as hello:
    print(hello)
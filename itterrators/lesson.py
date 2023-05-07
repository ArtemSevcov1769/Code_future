class HWContMen:
    def __enter__(self):
        print('Входим в контекст')
        return 'hello world'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Выходим из него')
        print(exc_type, exc_val, exc_tb, sep='\n')
        if exc_type is TypeError:
            return True
with HWContMen() as hello:
    print(hello)
    print(1+'a')
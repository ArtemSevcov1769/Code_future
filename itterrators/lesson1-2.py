class WritebleFile():
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.file = open(self.file_path, 'a')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with WritebleFile('test.txt') as file:
    file.write('slkdhglsdjhgjldfhg')
with open('test.txt', 'w') as file:
    file.write('oquweyrouiqwyeroquwiery')
print('end')
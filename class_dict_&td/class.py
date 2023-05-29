class Human:
    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age

    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name):
        if len(name) <= 5:
            self._name = name

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 140:
            raise ValueError("Слишком низкий")
        else:
            self._height = height

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

people = Human("Borya", 170, 15)
print(people.name)
print(people.height)
print(people.age)
people.name = "Sanay"
people.height = 141
people.age = 14
print(people.name)
print(people.height)
print(people.age)
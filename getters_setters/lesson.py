# class Animal:
#     def __init__(self, name):
#         # self.name = name #public
#         # self._name = name #protected
#         self._name = name #privat
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, name):
#         if len(name) < 30:
#             self._name = name
#         else:
#             raise ValueError("imay ne dolzhno bity bolshe 30 simvolov")
# # lev = Animal("Levvv")
# # lev.set_name('lkhsdbglshkfgbdfhg')
#
# class Year:
#     def __init__(self, days, season):
#         self.__days = days
#         self.__season = season
#
#     def get_days(self):
#         return self.__days
#
#     def set_days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise Exception("elwirygwleiryg")
#
# y = Year(365, 'зима')
# print(y.get_days())
# y.set_days(200)

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name):
            self._name = name

    @property
    def age(self):
        return
    @age.setter
    def age(self, age):
        if age <= 0:
            raise ValueError(',kbg')
        self._age = age


p = Person('Mikhail', 345)

print(p.name)
p.name = 'Михаил'
print(p.name)
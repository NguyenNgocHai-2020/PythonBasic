from Day_8_OOP.Animal import Animal

class Mouse(Animal):
    # def __init__(self, name, age, weight):
    #     self.name = name
    #     self.age = age
    #     self.weight = weight
    def __init__(self, name, age, weight, country, year):
        super(Mouse, self).__init__(name, age, weight)
        self.country = country
        self.year = year

    def show_info(self):
        print('name :', self.name)
        print('country :', self.country)
        print('year :', self.year)



    # def show_info(self):
    #     super(Mouse, self).showInfo()

from Day_8_OOP.Animal2_film import *
class Mouse2(Animal2, Film):
    def __init__(self, name, age, weight, country, year, author, film_type):
        Animal2.__init__(self, name, age, weight)
        Film.__init__(self, author, film_type)
        self.country = country
        self.year = year

    def show_info(self):
        print('name :', self.name)
        print('country :', self.country)
        print('year :', self.year)

mouse2 = Mouse2('Mickey', 18, 55, 'VN', '1990', 'Unknow', 'Cartoon')
mouse2.show_info()
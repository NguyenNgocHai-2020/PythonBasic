from Day_8_OOP.Person import Person
from Day_8_OOP.Person import People

class Student(Person, People):

    # call super and add new command
    def __init__(self, name, gender, married, age_number, university):
        # super().__init__(name)
        Person.__init__(self, name)
        People.__init__(self, gender, married)
        self.age = age_number
        self.university = university

    # call super and add new command
    # def show_info(self):
    #     super(Student, self).show_info()
    #     print('Age is ', self.age)
    #     print('University is ', self.university)
    #
    # call super and add new command
    # def show_info(self):
    #     print('Age is ', self.age)
    #     print('University is ', self.university)
    #     super(Student, self).show_info()

    # override and dont call super
    # def show_info(self):
    #     # print('Name is', self.name)
    #     print('Age is', self.age)

    def show_info(self):
        Person.show_info(self)
        People.show_info(self)
        print('Age', self.age)
        print('University', self.university)

    def test(self):
        print('test')
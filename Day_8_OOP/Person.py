class Person:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print('Name is ', self.name)

    def move(self):
        print('move ....')

class People:
    def __init__(self, gender, married):
        self.gender = gender
        self.married = married

    def show_info(self):
        print('Gender ', self.gender)
        if self.married:
            print('Married')
        else:
            print('Not married')



class Animal2:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def show_info(self):
        print("Ten la:", self.name,"Tuoi la:",
              self.age,"Can nang la:", self.weight)


class Film:
    def __init__(self, author, film_type):
        self.author = author
        self.film_type = film_type

    def show_info(self):
        print('Author', self.author)
        print('Film type', self.film_type)
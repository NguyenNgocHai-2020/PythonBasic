class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def show_info(self):
        print("Ten la:", self.name,"Tuoi la:",
              self.age,"Can nang la:", self.weight)
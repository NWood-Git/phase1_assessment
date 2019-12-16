class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def __repr__(self):
        return f"{self.last_name.title()}, {self.first_name.title()}"

# x = Person("Jack","Ryan")
# print(x)
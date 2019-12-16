from app.location import Location
# from home import Home
from app.person import Person
import app.person

class Business(Location):

    def __init__(self, address, name, employees=[]):
        super().__init__(address)
        self.name = name
        self.employees = employees

    def __repr__(self):
        return f"{self.name},  {len(self.employees)} employees"
    
    def add_employee(self,person):#arg as person.x
        self.employees.append(person)


# gp = Business(address = "10 HotDog Lane", name = "Gray's Papaya", employees =['Carter', 'Kai', 'Wasif','Greg'])
# print(gp)
# gp.add_employee(person.x)
# print(gp)
# print(gp.employees)
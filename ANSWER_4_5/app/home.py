from app.location import Location
# from business import Business
from app.person import Person
import app.person


class Home(Location):

    def __init__(self, address, residents=[]):
        super().__init__(address)
        self.residents = residents

    def __repr__(self):
        return f"{self.address},  {len(self.residents)} residents"

    def add_resident(self,person):
        self.residents.append(person)
    
    def resident_names(self):
        resident_list = []
        for person in self.residents:
            resident_list.append(person)
        return resident_list

# Bonus for no credit: Can you have a Home work as an iterator that yields the person objects from the .residents attribute?
# So you could write
# this is extra, you don't have to do this
# for person in my_home:
    # print(person.first_name)

# ab = Home(address = "1261 Wild Azalea Ln", residents =['a', 'b', 'c'])
# print(ab)
# ab.add_resident(person.x)
# print(ab)
# print(ab.residents)
from app.location import Location
from app.person import Person
from app.business import Business
from app.home import Home


#People
homer = Person("Homer", "Simpson")
marge = Person("Marge","Simpson")
bart = Person("Bart", "Simpson")

rick = Person("Rick", "Grimes")
carl = Person("Carl", "Grimes")

#Home
simpson_home = Home(address = "742 Evergreen Terrace", residents = [])
grimes_house = Home(address = "123 Zombie Drive", residents = [])

#Business
power_plant = Business(address= "1 Nuclear Rd", name = "Power Plus", employees = [])
police_station = Business(address = "2 Copper Road", name = "The Station", employees = [])

#putting persons in their home
simpson_home.add_resident(homer)
simpson_home.add_resident(marge)
simpson_home.add_resident(bart)

grimes_house.add_resident(rick)
grimes_house.add_resident(carl)

#giving persons jobs
power_plant.add_employee(homer)
police_station.add_employee(rick)
police_station.add_employee(carl)

print(simpson_home)
print(power_plant)
print(police_station)
print(marge)
print(simpson_home.resident_names())

#last one shows the resident list is correct it looks off because the comma separates the first and last name and diff ppl on the list
x = simpson_home.resident_names()
for item in x:
    print(item)
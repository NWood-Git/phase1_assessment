import unittest
from app.location import Location
from app.person import Person
from app.business import Business
from app.home import Home

# #python3 -m unittest discover test 
# #python3 -m unittest discover ~/gizmo/Byte-Academy/phase1_assessment/assessment_inclass/ANSWER_4_5/tests
# MUST UN FROM base dir - ANSWER_4_5

class TestBusiness(unittest.TestCase):

    def test_bus_creation(self):
        test_bus = Business(address = "10 HotDog Lane", name = "Gray's Papaya", employees =['Carter'])
        self.assertEqual(test_bus.address,"10 HotDog Lane", "should have the input address" )
        self.assertIsInstance(test_bus, Business, "test_bus should be an instance of Business")
        self.assertEqual(len(test_bus.employees), 1, "only put one employee in")

    def test_add_employee(self):
        test_bus = Business(address = "10 HotDog Lane", name = "Gray's Papaya", employees =['Carter'])
        test_bus.add_employee(Person("John", "Bomba"))
        self.assertEqual(len(test_bus.employees), 2, "2 res had Carter added John")
        self.assertEqual(test_bus.employees[0], 'Carter')

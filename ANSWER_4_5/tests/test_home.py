import unittest
from app.location import Location
from app.person import Person
from app.business import Business
from app.home import Home

#python3 -m unittest discover test 
#python3 -m unittest discover ~/gizmo/Byte-Academy/phase1_assessment/assessment_inclass/ANSWER_4_5/tests

class TestHome(unittest.TestCase):

    def test_home_creation(self):
        test_home = Home(address = "742 Evergreen Terrace", residents = ["Marge"])
        self.assertEqual(test_home.address,"742 Evergreen Terrace", "should have the input address" )
        self.assertIsInstance(test_home, Home, "test_home should be an instance of home")
        self.assertEqual(len(test_home.residents), 1, "only put one resident in")

    def test_add_resident(self):
        test_home = Home(address = "742 Evergreen Terrace", residents = ["Marge"])
        test_home.add_resident(Person("Lisa", "Simpson"))
        self.assertEqual(len(test_home.residents), 2, "2 res had marge added lisa")
        self.assertEqual(test_home.residents[0], 'Marge')
        
    def test_resident_names(self):
        test_home = Home(address = "742 Evergreen Terrace", residents = [])
        test_home.add_resident(Person("Lisa", "Simpson"))
        test_home.add_resident(Person("Maggie", "Simpson"))
        x = test_home.resident_names()
        self.assertEqual(len(x), 2, "2 res were added")
        self.assertIsInstance(x[0], Person, "residents added were Person class")
import unittest
from person import Person,Fellow,Staff

class TestPersons(unittest.TestCase):
    person=Person()
    x_staff=Person()
    x_fellow=Person()

    def test_add_person(self):
        num_persons=Person.num_of_persons_at_dojo
        
        self.x_staff.add_person("Mas","Staff")
        self.x_fellow.add_person("Willi","Fellow","Y")
        
        num2_persons=Person.num_of_persons_at_dojo

        self.assertEqual((num2_persons-num_persons),2)

    def test_person_type_staff(self):
        staff=self.x_staff.add_person("Mas","Staff")
        #print (staff[0])
        self.assertEqual(staff[0],"Staff")
    
    def test_person_type_fellow(self):
        fellow=self.x_fellow.add_person("Willi","Fellow","Y")
        #print (fellow[0])
        self.assertEqual(fellow[0],"Fellow")
    
        
if __name__=="__main__":
    unittest.main()

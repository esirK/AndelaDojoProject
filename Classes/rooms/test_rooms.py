import unittest
from rooms import  Room,Office,LivingSpace

class TestCreateRoom(unittest.TestCase):
    room_instance=Room()
    office=Office()
    living_space=LivingSpace()

    def test_office_is_instance_of_room(self):
        self.assertIsInstance(self.office,Room,msg="Office Should Be An Instance Of Room")

    def test_living_room_is_instance_of_room(self):
        self.assertIsInstance(self.living_space,Room,msg="Living Should Be An Instance Of Room")

    def test_create_room_true(self):
        initial_room_count=self.room_instance.all_rooms
        blue_office=self.room_instance.create_room("office","Blue")
        self.assertTrue(blue_office)
        new_room_count=self.room_instance.all_rooms
        self.assertEqual(new_room_count-initial_room_count,1)
        
    def test_multiple_inputs(self):
        multiple_rooms=Room()
        multiples=multiple_rooms.create_room("office","Xmas")
        

    def test_size_of_office_equal_6(self):
        self.assertEqual(self.office.size,6,msg="Size Of Office Must Be 6")

    def test_max_size_of_living_room_4(self):
        self.assertEqual(self.living_space.size,4,msg="Size Of Living Room Must Be 4")

    def test_office_type(self):
        self.assertEqual(self.office.what_type,"OFFICE")
        
    def test_living_room_type(self):
        self.assertEqual(self.living_space.what_type,"LIVING_ROOM")

    def test_create_office(self):
        texasOffice=Office()
        texasOffice.create("Texas")
        self.assertNotEqual(texasOffice.what_type,"LIVING_ROOM")
        
    def test_create_living_space(self):
        texasLiving=LivingSpace()
        texasLiving.create("TexasLife")
        self.assertNotEqual(texasLiving.what_type,"OFFICE")    
    
if __name__=="__main__":
    unittest.main()

import unittest
from Dojo_main import Dojo
from rooms.room_new import Room

class TestDojo(unittest.TestCase):
    #test Create room
    def test_create_room(self):
        init_number_of_rooms_at_dojo=len(Dojo().list_office_rooms)
        new_room=Dojo().create_room("Wataf","OFFICE")
        new_number_of_rooms_at_dojo=len(Dojo().list_office_rooms)
        self.assertEqual(new_number_of_rooms_at_dojo-init_number_of_rooms_at_dojo,0)
    def test_case_for_wrong_room_type(self):
        self.assertTrue(Room("Gidp","OFFICE").valid_room_type,msg="Wrong Room Type")
        
    def test_case_create_room_with_no_name(self):
        self.assertEqual(Room(" ","OFFICE").nyce_name,"Empty Room Name",msg="No room Name Provided")

    def test_creation_of_same_office_twice(self):
        dojo=Dojo()
        size=dojo.create_room("Makuti","Office")
        new_size=dojo.create_room("Makuti","Office")
        print (size)
        self.assertNotEqual(new_size,size)
if __name__=="__main__":
    unittest.main()

import unittest
import Dojo_main,rooms.room_new

class TestDojo(unittest.TestCase):
    #test Create room
    def test_create_room(self):
        init_number_of_rooms_at_dojo=len(Dojo_main.Dojo().list_office_rooms)
        new_room=Dojo_main.Dojo().add_room("Wataf","OFFICE")
        new_number_of_rooms_at_dojo=len(Dojo_main.Dojo().list_office_rooms)
        self.assertEqual(new_number_of_rooms_at_dojo-init_number_of_rooms_at_dojo,0)
    def test_case_for_wrong_room_type(self):
        self.assertTrue(rooms.room_new.Room("Gidp","OFFICE").valid_room_type,msg="Wrong Room Type")
        
    def test_case_create_room_with_no_name(self):
        self.assertEqual(rooms.room_new.Room(" ","OFFICE").nyce_name,"Empty Room Name",msg="No room Name Provided")

if __name__=="__main__":
    unittest.main()

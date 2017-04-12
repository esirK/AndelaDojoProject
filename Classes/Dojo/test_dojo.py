import unittest
import Dojo_Classes,rooms.room_new

class TestDojo(unittest.TestCase):
    #test Create rooms
    def setUp(self):
        self.test_room=rooms.room_new.Room("testRoom","OFFICE")
        self.int_room=rooms.room_new.Room('wboo',"OFFICE")
    def test_create_room(self):
        init_number_of_rooms_at_dojo=rooms.room_new.Room.rooms_at_dojo
        new_room=rooms.room_new.Room("Wataf","OFFICE")
        new_number_of_rooms_at_dojo=rooms.room_new.Room.rooms_at_dojo
        self.assertEqual(new_number_of_rooms_at_dojo-init_number_of_rooms_at_dojo,1)
   # def test_create_room_with_valid_names(self):
       # with self.assertRaises(TypeError,msg="Allow string inputs only"):
          #  self.int_room
        #print(self.int_room.name)
    def test_case_for_wrong_room_type(self):
        self.assertTrue(rooms.room_new.Room("Gidp","OFFICE").valid_room_type,msg="Wrong Room Type")
        
    def test_case_create_room_with_no_name(self):
        self.assertEqual(rooms.room_new.Room(" ","OFFICE").nyce_name,"Empty Room Name",msg="No room Name Provided")
if __name__=="__main__":
    unittest.main()

import unittest
from ..Classes.Room import  Office,LivingSpace

class TestCreateRoom(unittest.TestCase):
    def test_create_room_true(self):
        room_instance=Room()
        initial_room_count=len(room_instance.all_rooms)
        blue_office=room_instance.create_room("Blue","office")
        self.assertTrue(blue_office)
        new_room_count=len(room_instance.all_rooms)
        self.assertEqual(new_room_count-initial_room_count,1)

if __name__=="__main__":
    unittest.main()

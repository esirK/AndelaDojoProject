import random
'''
class Room inherit from  a list in order to store persons into it  
'''
class Room(list):
    total_rooms_at_dojo=0
    def __init__(self,name,office_or_cube):
        self.office_or_cube=office_or_cube
        self.name=name
  
        if self.name==""or self.name==" ":
            self.nyce_name="Empty Room Name"
        else:
            self.nyce_name="Name Ok"
        if self.office_or_cube ==("OFFICE"or "CUBE"):    
            Room.rooms_at_dojo+=1
            if self.office_or_cube=="OFFICE":
                self.size=6
            elif self.office_or_cube=="CUBE":
                self.size=4
            else:
                self.size=0
            self.valid_room_type= True

        else:
            self.valid_room_type=False

#rooms
class Room(object):
    all_rooms=0
    def __init__(self,name,what_type):
        self.all_rooms+=1
        self.what_type=what_type

    def __init__(self):
        pass

    def create_room(self,name,what_type):
        self.what_type=what_type
        self.all_rooms+=1
        return self.all_rooms

class Office(Room):

    size=6
    what_type="OFFICE"
    
    def __init__(self):
        pass
    def create(self,name):
        self.name=name

class LivingSpace(Room):
    size=4
    what_type="LIVING_ROOM"
    def __init__(self):
        pass
    def create(self,name):
        self.name=name

import sys
import random
#sys.path.append('../')
import Person.person_new
class Staff(Person.person_new.Person):
    def __init__(self,person,rooms):
        self.person=person
        self.rooms=rooms
    def allocate_room(self):
        random_room_index=random.randrange(len(self.rooms))
        print (self.person.name+" has been allocated the "+self.rooms[random_room_index].name)#
        return self.rooms[random_room_index].append(self.person)#Add a Staff to the office

        

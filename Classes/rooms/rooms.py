#rooms
import random

class Room(object):
    all_rooms=0
    rooms=[]
    def __init__(self):
        pass

    def create_room(self,name,what_type):
        self.what_type=what_type
        asmany_names=[]
        asmany_names.append(name)
        if self.what_type=="LIVING_ROOM":
            create_living_room=LivingSpace(name)
            create_living_room
        else:
            creat_office=Office(name)
            creat_office

       # print (asmany_names)
        return self.all_rooms

class Office(Room):

    size=6
    what_type="OFFICE"
    
    def __init__(self,name):
        #print ("Offiece"+name+" has Been successfully Created!")
        list_of_names=name.split(',')
        for i in range(0,len(list_of_names)):
            Room.all_rooms+=1
            Room.rooms.append(list_of_names[i])
            print ("Offiece "+list_of_names[i]+" has Been successfully Created!")
    
        
class LivingSpace(Room):
    size=4
    what_type="LIVING_ROOM"
    def __init__(self,name):
        #return " Living Room "+name+" has Been successfully Created!"
        list_of_names=name.split(',')
        for i in range(0,len(list_of_names)):
            Room.all_rooms+=1
            Room.rooms.append(list_of_names[i])
            print( "Living Room "+list_of_names[i]+" has Been successfully Created!")

rx=Room()
rx.create_room("Wabudabu,Joggoo","OFFICE")
rl=Room()
rl.create_room("Kahao,Morty","LIVING_ROOM")
print(Room.rooms)

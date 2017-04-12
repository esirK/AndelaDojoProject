#Class Dojo
import Person.person_new
import rooms.room_new
import random
import collections
class Dojo(object):
    def __init__(self):
        self.list_persons=[]
        self.list_living_rooms=[]
        self.list_office_rooms=[]
        self.person_and_office_room={}
        self.person_and_living_room={}
        

        
            
    def add_person(self,name,person_type,accommodation='N'):
        if person_type=="Staff":
            if accommodation=="Y":
                accommodation='N'
        print(name+" has been successfully added.")
        person=Person.person_new.Person(name,person_type,accommodation)
        self.list_persons.append(person)
        how_many_offices_available=len(self.list_office_rooms)
        if person_type=="Staff":
            print (how_many_offices_available)
            if how_many_offices_available>1:
                #Room Is Available
                #check if its full (A room is full if len(room)==6)
                print("Rooms Available")
                random_room_index=random.randrange(how_many_offices_available)
                print (name+" has been allocated the "+self.list_office_rooms[random_room_index].name)#
                #Count number of persons in offices
                person_in_room=[]
                for k,v in self.person_and_office_room.items():
                    person_in_room.append(v)
                room_name=self.list_office_rooms[random_room_index].name
                print (str(person_in_room.count(room_name))+" Checkkkkkkkkkkkkkkkk")
                if (person_in_room.count(room_name))>6:
                    #Remove That room
                    print("Room Full")
                else:
                    self.person_and_office_room[name]=room_name
                
            elif how_many_offices_available==1:
                room_name=self.list_office_rooms[0].name
                self.person_and_office_room[name]=room_name
                
                print (name+" has been allocated the "+(self.list_office_rooms[0].office_or_cube)+" "+(room_name))#
        elif person_type=="Fellow":
            how_many_cubes_available=len(self.list_living_rooms)
            #Check if Fellow Want's Accommodation
            
            if how_many_offices_available>1:
            #Office Room Is Available
                random_room_index=random.randrange(how_many_offices_available)
                print (name+" has been allocated the "+self.list_office_rooms[random_room_index].name)#
                room_name=self.list_office_rooms[random_room_index].name
                self.person_and_office_room[name]=room_name
                how_many_offices_available-=1
                
            elif how_many_offices_available==1:
                room_name=self.list_office_rooms[0].name
                self.person_and_office_room[name]=room_name
                
                print (name+" has been allocated the "+(self.list_office_rooms[0].office_or_cube)+" "+(room_name))#
            else:
                print("No Living Room's Remaining")
            if accommodation=='Y':
                if how_many_cubes_available>1:
                    
                    #Cube Room Is Available
                    #Check if There is an Empty One
                    
                    random_room_index=random.randrange(how_many_cubes_available)
                    room_name=self.list_living_rooms[random_room_index].name
                    print (name+" has been allocated the "+room_name)#
                    self.person_and_living_room[name]=room_name
                    how_many_cubes_available-=1
                    
                elif how_many_cubes_available==1:
                    room_name=self.list_living_rooms[0].name
                    #self.person_and_room[name]=room_name
                    print (name+" has been allocated the "+(self.list_living_rooms[0].office_or_cube)+" "+(room_name))#
                else:
                    print("No Living Room's Remaining")

            
                
                
        #Allocate room
        
        
    def create_room(self,name,office_or_cube):
        office_or_cube=office_or_cube.upper()
        classi=rooms.room_new.Room(name,office_or_cube)
        
        if classi.office_or_cube=="OFFICE":
            list_of_cube_names=classi.name.split(' ')
            for cube in range(0,len(list_of_cube_names)):
                print("An office called "+list_of_cube_names[cube]+" has been successfully created!")
                self.list_office_rooms.append(classi)
        elif classi.office_or_cube=="CUBE":
            list_of_office_names=classi.name.split(',')
            for office in range(0,len(list_of_office_names)):
                print("An Cube(Living Space) called "+list_of_office_names[office]+" has been successfully created!")
                self.list_living_rooms.append(classi)
        else:
            return False
        

dojo=Dojo()

dojo.create_room("Tsavo","OFFICE")
dojo.create_room("Kikwetu","OFFICE")
#dojo.create_room("GameOver","OFFICE")
#dojo.create_room("Man Eater","CUBE")
#dojo.create_room("CostiBas","CUBE")
#dojo.create_room("Man Shiba","CUBE")

#dojo.add_person("Wahidu","Fellow","Y")
#dojo.add_person("iduko","Fellow","Y")

dojo.add_person("Makena1","Staff","Y")
dojo.add_person("Mwiki11","Staff","Y")
dojo.add_person("namine1","Staff","Y")
dojo.add_person("Makena2","Staff","Y")
dojo.add_person("Mwiki2","Staff","Y")
dojo.add_person("namine2","Staff","Y")
dojo.add_person("Makena3","Staff","Y")
dojo.add_person("Mwiki3","Staff","Y")
dojo.add_person("namine3","Staff","Y")

dojo.add_person("Makena4","Staff","Y")
dojo.add_person("Mwiki14","Staff","Y")
dojo.add_person("namine4","Staff","Y")

#dojo.add_person("Kimwi","Staff","Y")

print (len(dojo.list_persons))
print (len(dojo.list_office_rooms))
print (dojo.person_and_office_room)#Offices
print (dojo.person_and_living_room)#Cubes
d=dojo.person_and_office_room

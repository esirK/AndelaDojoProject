#Person
import sys
import random
sys.path.append('../')
import rooms

class Person:
    num_of_persons_at_dojo=0
    persons=[]
    rooms=[]
    def __init__(self,rooms):
        self.rooms=rooms
        print (self.rooms)

    def add_person(self,name,p_type,accommodation="N"):
        Person.num_of_persons_at_dojo+=1
        self.name=name
        self.p_type=p_type
        self.accommodation=accommodation

        x=self.name,self.p_type,accommodation
        print(x[0])
        if x[1]=="Staff"and x[2]=="Y":
            return "Staff's Can't Get Accommodation"
        
        #self.persons.append(x[0])
        #print (x[0]+" has been successfully added.")
        #print (x[0]+" has been allocatedd ")
        #print (self.persons)
        pers=[]
        pers.append(p_type)

        #Add a person to room Randomly
        if self.p_type=="Staff":
            self.accommodation="N"
            add_a_staffx=Staff().create_staff(name,self.rooms)
            #Add Staff To Database/TextFile
            print (add_a_staffx)
            #return Room Allocated
        
        return pers
    
class Staff(Person):
    staffs=[]
    rooms=[]
    staffs_and_rooms={}
    def __init__(self):
        pass
    def create_staff(self,name,rooms):
        self.staffs.append(name)
        how_many_rooms_available=len(rooms)
        for staff in self.staffs:
            if how_many_rooms_available>1:
                self.staffs_and_rooms[str(staff)]=rooms[random.randrange(how_many_rooms_available)]
                how_many_rooms_available-=1
            elif how_many_rooms_available==1:
                self.staffs_and_rooms[str(staff)]=rooms[0]
            else:
                print ("No More Rooms Available")
        return self.staffs_and_rooms
        

class Fellow(Person):
    def __init__(self,name,office,living_room):
        pass

    fellows=[]
    fellows_and_rooms={}
    def create_fellow(self,name,rooms):
        self.fellows.append(name)
        how_many_rooms_available=len(rooms)
        
        
    
x_staff=Person(["one","two","three","four","five","six"])
#print (Person.num_of_persons_at_dojo)
        
x_staff.add_person("Mas","Staff")
x_staff.add_person("Sam","Staff")
#y_staff=
#print(Person.num_of_persons_at_dojo)
        
#x_fellow=Person()
#print (x_fellow.add_person("Willi","Fellow","Y"))
#print (Person.num_of_persons_at_dojo)
        

 

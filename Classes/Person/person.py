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
        #print (self.rooms)

    def add_person(self,name,p_type,accommodation="N"):
        Person.num_of_persons_at_dojo+=1
        self.name=name
        self.person_type=p_type
        self.accommodation=accommodation

        x=self.name,self.person_type,accommodation
        print(x[0])
        if x[1]=="Staff"and x[2]=="Y":
            return "Staff's Can't Get Accommodation"
        
        pers=[]
        pers.append(p_type)

        #Add a person to room Randomly
        if self.person_type=="Staff":
            self.accommodation="N"
            add_a_staff_x=Staff().create_staff(name,self.rooms)
            #Add Staff To Database/TextFile
            print (add_a_staff_x)
            #return Room Allocated
        elif self.person_type=="Fellow":
            add_a_fellow_x=Fellow().create_fellow(name,self.rooms)
            print (add_a_fellow_x)
        else:
            print ("No Person Of That Type At Andela Dojo")
        #return pers
    
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
    def __init__(self):
        pass
    rooms=[]
    fellows=[]
    fellows_and_rooms={}
    def create_fellow(self,name,rooms):
        self.fellows.append(name)
        how_many_rooms_available=len(rooms)
        for fellow in self.fellows:
            if how_many_rooms_available>1:
                self.fellows_and_rooms[str(fellow)]=rooms[random.randrange(how_many_rooms_available)]
                how_many_rooms_available-=1
            elif how_many_rooms_available==1:
                self.fellows_and_rooms[str(fellow)]=rooms[0]
            else:
                print ("No More Rooms Available")
        return self.fellows_and_rooms
        
        
    
x_staff=Person(["one","two","three","four","five","six"])
#print (Person.num_of_persons_at_dojo)
        
x_staff.add_person("Mas","Staff")
x_staff.add_person("Sam","Fellow")
#y_staff=
#print(Person.num_of_persons_at_dojo)
        
#x_fellow=Person()
#print (x_fellow.add_person("Willi","Fellow","Y"))
#print (Person.num_of_persons_at_dojo)
        

 

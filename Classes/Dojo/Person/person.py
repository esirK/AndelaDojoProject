#Person
import sys
import random
sys.path.append('../')
#import rooms

class Person:
    num_of_persons_at_dojo=0
    persons=[]
    office_rooms=[]#Living/Office
    living_rooms=[]
    def __init__(self,office_rooms,living_rooms):
        self.office_rooms=office_rooms
        self.living_rooms=living_rooms
        #print (self.rooms)

    def add_person(self,name,p_type,accommodation="N"):
        Person.num_of_persons_at_dojo+=1
        self.name=name
        self.person_type=p_type
        self.accommodation=accommodation

        x=self.name,self.person_type,accommodation
        
        if x[1]=="Staff"and x[2]=="Y":
            return "Staff's Can't Get Accommodation"
        self.person_name_and_rooms_allocated=[]
        #Add a person to room Randomly
        
        if self.person_type=="Staff":
            self.accommodation="N"
            add_a_staff_x=Staff().create_staff(name,self.office_rooms)
            #Add Staff To Database/TextFile
            
            self.person_name_and_rooms_allocated.append(add_a_staff_x)
            #return Room Allocated
            
        elif self.person_type=="Fellow":
        
            add_a_fellow_x_to_office=Fellow().create_fellow(name,self.living_rooms)
            add_a_fellow_y_to_living_room=Fellow().create_fellow(name,self.office_rooms)
            
            #person_name_and_rooms_allocated.append(add_a_fellow_y_to_living_room)
            self.person_name_and_rooms_allocated.append(add_a_fellow_x_to_office)
        else:
            print ("No Person Of That Type At Andela Dojo")
        return self.person_name_and_rooms_allocated
    
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
    fellow_office_and_living_room=[]
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
        
        
        
    
x_staff=Person(["Office_one","Office_two","Office_three","Office_four","Office_five","Office_six"],["living_one","living_2","living_3"])
#print (Person.num_of_persons_at_dojo)
        
print (x_staff.add_person("Mas","Staff"))
print (x_staff.add_person("Sam","Fellow"))
print (x_staff.add_person("Peky","Fellow"))

 

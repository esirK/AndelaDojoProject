#Person
class Person:
    num_of_persons_at_dojo=0
    persons=[]
    def __initi__(self):
        pass

    def add_person(self,name,p_type,accommodation="N"):
        Person.num_of_persons_at_dojo+=1
        self.name=name
        self.p_type=p_type
        self.accommodation=accommodation

        pers=[]
        pers.append(p_type)
        return pers
    
class Staff(Person):
    def __init__(self,name,office):
        super().__init__(name,office)


class Fellow(Person):
    def __init__(self,name,office,living_room):
        super().__init__(name,office)


#x_staff=Person()
#print (Person.num_of_persons_at_dojo)
        
#print (x_staff.add_person("Mas","Staff"))
#print(Person.num_of_persons_at_dojo)
        
#x_fellow=Person()
#print (x_fellow.add_person("Willi","Fellow","Y"))
#print (Person.num_of_persons_at_dojo)
        

 

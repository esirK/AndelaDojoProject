class Person(object):
    number_of_persons=0
    def __init__(self,name,person_type,want_accommodation):
        self.name=name
        self.person_type=person_type
        self.want_accommodation=want_accommodation
        self.number_of_persons+=1
    

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Cilass Dojo

import Person.person_new
import Person.Staff.staff
import rooms.room_new
import random
import collections


class Dojo(object):

    def __init__(self):
        self.list_persons = []
        self.list_living_rooms = []
        self.list_office_rooms = []
        self.list_of_un_allocated_persons = []
        self.list_of_fellows_with_no_accommodation = []
        self.list_of_full_rooms = []
        self.ll=[]
    def add_person(
        self,
        name,
        person_type,
        accommodation='N',
        ):
        if person_type == 'Staff':
            if accommodation == 'Y':
                accommodation = 'N'
        print (name + ' has been successfully added.')
        person = Person.person_new.Person(name, person_type,
                accommodation)
        self.list_persons.append(person)
        how_many_offices_available = len(self.list_office_rooms)
        if person_type == 'Staff':
            if how_many_offices_available > 1:
                print ('We Only Have ' + str(how_many_offices_available) \
                    + ' Office Left')

                # Room Is Available
                # check if its full (A room is full if len(room)==6)

                print ('Rooms Available')
                random_room_index = \
                    random.randrange(how_many_offices_available)
                staff = Person.Staff.staff.Staff(person,
                        self.list_office_rooms)
                print (staff.allocate_room())

                # self.list_office_rooms[random_room_index].append(person)#Add a Staff to the office

                if len(self.list_office_rooms[random_room_index]) == 6:

                    # Room is Full: Remove it from List Of Non full Offices

                    self.list_of_full_rooms.append(self.list_office_rooms[random_room_index])
                    del self.list_office_rooms[random_room_index]

                    # Reduce Number of offices remaining

                    how_many_offices_available -= 1
            elif how_many_offices_available == 1:

                room_name = self.list_office_rooms[0].name

                print (name + ' has been allocated the ' \
                    + self.list_office_rooms[0].office_or_cube + ' ' \
                    + room_name)  #
                self.list_office_rooms[0].append(person)
                if len(self.list_office_rooms[0]) == 6:

                    # Room is Full

                    self.list_of_full_rooms.append(self.list_office_rooms[0])
                    del self.list_office_rooms[0]

                    # No office Remaing

                    how_many_offices_available = 0
            else:
                print ('No Office Rooms  Available For Allocation')
                self.list_of_un_allocated_persons.append(person)
        elif person_type == 'Fellow':

            how_many_cubes_available = len(self.list_living_rooms)

            # Check if Fellow Want's Accommodation

            if how_many_offices_available > 1:

            # Office Room Is Available

                random_room_index = \
                    random.randrange(how_many_offices_available)
                print (name + ' has been allocated the ' \
                    + str(random_room_index) + ' ' \
                    + self.list_office_rooms[random_room_index].name)  #
                self.list_office_rooms[random_room_index].append(person)
                if len(self.list_office_rooms[random_room_index]) == 6:

                    # Room is Full Remove it

                    self.list_of_full_rooms.append(self.list_office_rooms[random_room_index])
                    del self.list_office_rooms[random_room_index]

                    # Reduce offices Remaining

                    how_many_offices_available -= 1
            elif how_many_offices_available == 1:

                room_name = self.list_office_rooms[0].name
                random_room_index = \
                    random.randrange(how_many_offices_available)
                print (name + ' has been allocated the ' \
                    + self.list_office_rooms[0].office_or_cube + ' ' \
                    + room_name)  #
                self.list_office_rooms[0].append(person)
                if len(self.list_office_rooms[random_room_index]) == 6:

                    # Room is Full Remove it

                    self.list_of_full_rooms.append(self.list_office_rooms[0])
                    del self.list_office_rooms[0]

                    # Reduce offices Remaining

                    how_many_offices_available = 0
            else:
                print ('No Office Rooms  Available For Allocation')
                self.list_of_un_allocated_persons.append(person)

                # self.list_of_fellows_with_no_accommodation.append(name)

            if accommodation == 'Y':
                if how_many_cubes_available > 1:

                    # Cube Room Is Available
                    # Check if There is an Empty One

                    random_room_index = \
                        random.randrange(how_many_cubes_available)
                    room_name = \
                        self.list_living_rooms[random_room_index].name
                    print (name + ' has been allocated the ' + room_name)  #
                    self.list_living_rooms[random_room_index].append(person)

                    if len(self.list_living_rooms[random_room_index]) \
                        == 4:

                        # Room is Full Remove it

                        self.list_of_full_rooms.append(self.list_living_rooms[random_room_index])
                        del self.list_living_rooms[random_room_index]

                        # Reduce offices Remaining

                        how_many_cubes_available -= 1
                elif how_many_cubes_available == 1:

                    room_name = self.list_living_rooms[0].name
                    print (name + ' has been allocated the ' \
                        + self.list_living_rooms[0].office_or_cube \
                        + ' ' + room_name  )# F
                    self.list_living_rooms[0].append(person)
                    if len(self.list_living_rooms[0]) == 4:

                        # KaCube Kamejaa

                        self.list_of_full_rooms.append(self.list_living_rooms[0])
                        del self.list_living_rooms[0]
                        how_many_cubes_available = 0
                else:
                    print ("No Living Room's Remaining")
                    self.list_of_fellows_with_no_accommodation.append(person)

        # Allocate room
#

    def create_room(self, name, office_or_cube):
        office_or_cube = office_or_cube.upper()
        classi = rooms.room_new.Room(name, office_or_cube)

        if classi.office_or_cube == 'OFFICE':
            list_of_cube_names = classi.name.split(' ')
            
            for cube in range(0, len(list_of_cube_names)):
                if list_of_cube_names[cube] in self.ll:
                    print (list_of_cube_names[cube]+" Exists")
                else:
                    print ('An office called ' + list_of_cube_names[cube] \
                        + ' has been successfully created!')
                    self.list_office_rooms.append(classi)
                    self.ll.append(list_of_cube_names[cube])
        elif classi.office_or_cube == 'LIVING_ROOM':
            list_of_office_names = classi.name.split(',')
            for office in range(0, len(list_of_office_names)):
                if list_of_office_names[office] in self.ll:
                    print(list_of_office_names[office]+" Exist's")
                else:
                    print ('An Cube(Living Space) called ' \
                        + list_of_office_names[office] \
                        + ' has been successfully created!')
                    self.list_living_rooms.append(classi)
                    self.ll.append(list_of_office_names[office])
        else:
            return False

    def print_persons_in_room(list_of_full_rooms):
        for room in list_of_full_rooms:
            print (room.name + ' ' + room.office_or_cube \
                + ' Has The following People')
            for person in room:
                print (person.name + ' ')



			

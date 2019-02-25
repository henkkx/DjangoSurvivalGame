class Building:

    def __init__(self, name, desc, rooms, pos):
        self.name = name
        self.description = desc
        self.rooms = rooms
        self.position = pos

    def __str__(self):
        return "{0}\n{1}".format(self.name, self.description)


class Room:

    def __init__(self, name, people, objects):
        self.name = name
        self.people = people
        self.objects = objects

    def __str__(self):
        '''
        The following loops are to create a more readable version of the people & objects in the room.
         The if statements make sure that we don't add extra commas or whitespace characters ( which we would if we
         were to use .join() without the if)
        '''
        persons_text = ""
        for person in self.people:
            if persons_text is "":
                persons_text = person
            else:
                "\n".join((persons_text, person))

        objects_text = ""
        for obj in self.objects:
            if objects_text is "":
                objects_text = obj
            else:
                ", ".join((objects_text, obj))

        if len(self.people) == 0:
            return "{0}. Inside are the following items:{1}".format(self.name, objects_text)
        elif len(self.people) == 1:
            return "{0}. Inside is {1}\nAlso the following items:{2}".format(self.name, persons_text, objects_text)
        # not necessary to check for just 1 item, definitely won't be 0 ( not point having the room)
        return "{0}. Inside are:\n{1}\nAlso the following items:{2}".format(self.name, persons_text, objects_text)

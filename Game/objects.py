class Objects:

    def __init__(self, name, desc, type, etc=None):
        self.name = name
        self.description = desc
        self.type = type
        self.etc = etc
        ''' the variable etc will be whatever we need later for the objects extra attributes. For example it's readable
        or it can be used to do X damage etc.'''

    def __str__(self):
        if self.type == 'weapon':
            return "{0}({1}, {3} dmg): {2}".format(self.name, self.type, self.description, self.etc)
            #       Stick (weapon 20 dmg): A simple stick
        elif self.type == 'readable':
            return "{0}({1}): {2}".format(self.name, self.type, self.description)
            #       Book (readable): An old, dusted book

    def read(self):  # assuming we'll check that the object is readable while performing the action of reading
        return self.etc['text']


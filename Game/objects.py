#These are needed to define an abstract class and method
from abc import ABC, abstractmethod

class Objects(ABC):
    def __init__(self, name, desc, size):
        self.name = name
        self.description = desc
        self.size = size
        super().__init__()
        #size could be used for a limited inventory space requirement

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def read(self):  
        pass


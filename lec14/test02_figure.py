class Rectangle(object): 
    
    def __init__(self, h, v):
        self.h = h
        self.v = v
    
    def area(self):
        return self.h * self.v
    
    from abc import ABC, abstractmethod 
    
    clsss Shape(ABC):
    
    @abstractmethod 
    
    def area(self):
        pass

class Rectangle(Shape): 
    def __init__(self, h, v):
        self.h = h
        self.v = v
    
    def area(self):
        return self.h * self.v
    

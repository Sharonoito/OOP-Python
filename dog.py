class Dog:
    def __init__(self,name,color,specie):
        self.name=name
        self.color=color
        self.specie=specie
    def bark(self):
        return f"My dog is called {self.name},it is {self.color} in color and it belongs to {self.specie}  specie" 
    def eat(self):
        return f"My black dog is a {self.specie} specie and eats special meals"    
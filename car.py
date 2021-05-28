class Car:
    def __init__(self,color,model,mileage,speed):
        self.color=color
        self.model=model
        self.mileage=mileage
        self.speed=speed
    def hoot(self):
        return f"I love {self.color} cars espesially {self.model}  with {self.mileage} mileage"
    def accelerate(self):
        return f"My {self.color} car accelerated"
        



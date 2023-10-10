#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

    def park(self):
        print("Parking my", self.enginetype, "vehicle")
    
    def reverse(self, speed):
        self.mode = "reversing"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed)
        

class Sedan(Car):
    def __init__(self, enginetype, brandtype):
        super().__init__("Sedan")
        self.brandtype = brandtype
        self.enginetype = enginetype
    def drive(self, speed):
        self.speed = speed
        print("Driving my", self.brandtype, self.enginetype, "car at", self.speed)

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "motorcycle at", self.speed)

car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)

car3 = Sedan("gas","Mitusbishi")

print(mc1.wheels)
print(car1.enginetype)
print(car2.doors)


car1.drive(30)
car1.park()
car2.drive(40)
car2.park()
mc1.drive(50)
mc1.park()

car3.drive(60)
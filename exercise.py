import random

class Animal:
    def __init__(self, live = True, sound = None, _DEGREE_OF_DANGER = 0):
        self.live = live
        self.sound = sound
        self._DEGREE_OF_DANGER = _DEGREE_OF_DANGER
        self._cords = [0, 0, 0]

    def move(self, *_cords):
        self.dx = _cords[0] * self.speed
        self.dy = _cords[1] * self.speed
        self.dz = _cords[2] * self.speed
        return self.dx, self.dy, self.dz

    def get_cords(self):
        if self.dz >= 0:
            print(f"X: {self.dx} Y: {self.dy} Z: {self.dz}")
        else:
            print("It's too deep, i can't dive :(" )

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)
        
class Bird(Animal):
    def __init__(self, beak = True):
        super().__init__()
        self.beak = beak
    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")

class AquaticAnimal(Animal):
    def dive_in(self, z):
        self._DEGREE_OF_DANGER = 3
        self.dz = (self.dz/2) - abs(z)

class PoisonousAnimal(Animal):
    def __init__(self):
        self._DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed):
        self.speed = speed
        Animal.__init__(self)
        super().__init__()
        self.sound = "Click-click-click"


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()

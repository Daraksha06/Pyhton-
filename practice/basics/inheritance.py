class Bike:
    def wheels(self):
        print("I have 2 wheels ")
class Sport(Bike):
    def prop(self):
        print("I am a sport bike ")
class Standard(Bike):
    def sprop(self):
        print("I am a standard  bike ")
class Moped(Bike):
    def mprop(self):
       print("I am a moped  bike ") 
b=Bike()
s= Sport()
m=Moped()
s.wheels()
m.wheels()   
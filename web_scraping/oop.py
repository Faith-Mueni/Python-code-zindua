"""
oop is a programming paradigm that uses objects and their interractions to build programs and applications
class -> a blueprint for creating an object
object -> an instance of a class
Polymorphism-> allows objects of different classes to be treated as objects of a common base class
encapsulation->  
"""

class Car:
    make = ""
    model = ""
    year = 0

    def start (self):
        return "Vroooooooom!"

        def stop (self):
            return "scrrrrrr!"

myCar = Car ()

myCar.make = "Toyota"
myCar.model = "TX"
myCar.year = "2017"

print(myCar.make)
print(myCar.model)
print(myCar.year)
print(myCar.start())
print(myCar.stop())
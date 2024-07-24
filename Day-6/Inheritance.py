#====INHERITANCE====
class Animal:
    def speak():
        return "animal is speaking"
#SINGLE INHERITANCE
class Dog(Animal):
    def Bark():
        return "Boww....."
obj1=Animal
print(obj1.speak())
obj2=Dog
print(obj2.speak())
print(obj2.Bark())
#MULTILEVEL INHERITANCE
class Puppy(Dog):
    def puppy_speak():
        return "im talking"
obj3=Puppy
print(obj3.speak())
print(obj3.Bark())
print(obj3.puppy_speak())

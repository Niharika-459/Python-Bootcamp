#=======METHOD OVERRIDING====
'''class Animal:
    def Speak():
        return "speaking...."
class Dog(Animal):
    def Speak():
        return "dog is speaking..."
class Puppy(Dog):
    def Speak():
        return "puppy is speaking..."
obj3=Puppy
print(obj3.Speak())'''

'''def run():
    return "running"
def run():
    return "hello"
print(run())'''#prints the most recent call for the method.Previous call will be lost

#===METHOD OVERLOADING===
'''class Cal:
    def add(a,b,c):
        return a+b+c
obj1=Cal
print(obj1.add(10,20,30))'''

class cal:
    def add(self,*args):
        sum=0
        for i in args:
            sum+=i
        return sum
#take inputs
obj1=cal()#dynamic we use(),for static we dont use()
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4))
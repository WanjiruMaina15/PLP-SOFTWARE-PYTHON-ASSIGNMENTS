#Assignment 1: Design Your Own Class! 🏗️
#Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).

class Smartphones:# class smartphone
    def __init__(self,brand,color,price):#Use constructors to initialize each object with unique values.
        self.brand=brand #Add attributes and methods to bring the class to life!
        self.color=color
        self.__price=price
    def get_price(self):#Add an inheritance layer to explore polymorphism or encapsulation I USED ENCAPSULATION
        return self.__price
    def percentage_charge(self,charge):
        print(f"{self.brand} {self.color}{self.__price}is at {charge}%")

My_phone=Smartphones('REDMI 9A', 'Blue' , 7000)
My_phone.percentage_charge(50)


#Activity 2: Polymorphism Challenge! 🎭

#Create a program that includes animals or vehicles with the same action (like move()). 
# #However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print(f"{self.brand} {self.model} is driving 🚗")
class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print(f"{self.brand} {self.model} is flying ✈️")
my_car=Car('Toyota','Corolla')
my_plane=Plane('Boeing','747')
my_car.move()
my_plane.move()
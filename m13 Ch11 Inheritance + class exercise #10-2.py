# ====================================
# Attached: Class Exercise #10
# ====================================
# File: Challenge Exercise #1
# ====================================
# Name: Animal Type
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

class AnimalType:
    def eats(self):
        print("This animal likes to eat?")


class rabbits(AnimalType):
    def munch(self):
        print(" carrots ")


class birds(rabbits):
    def munch1(self):
        print(" seeds ")


class sheep(birds):
    def munch2(self):
        print(" grass ")


# inheriting the Rabbit Object from one different class
RabbitObject = rabbits()

# only sees objects in Rabbit
RabbitObject.eats()
RabbitObject.munch()

# inheriting the Bird Object from two different classes
BirdObject = AnimalType()
BirdObject = birds()

# only sees objects in Bird
BirdObject.eats()
BirdObject.munch1()

# inheriting the Sheep Object from two different classes
SheepObject = AnimalType()
SheepObject = sheep()

# only sees objects in Sheep
SheepObject.eats()
SheepObject.munch2()

''''
===============Output=================
This animal likes to eat?
 carrots 
This animal likes to eat?
 seeds 
This animal likes to eat?
 grass 

Process finished with exit code 0


'''


# ====================================
# Attached: Class Exercise #10
# ====================================
# File: Challenge Exercise #2
# ====================================
# Name: Student & Teacher Info
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


# the student class is inheriting from the person class
class Student(person):
    def __init__(self, name, age, address, city, state, zipCode, studentID, GPA):
        # the super keyword is calling the super class which is the person class and passing name, and age
        super().__init__(name, age)

        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.studentID = studentID
        self.GPA = GPA


class Teacher(person):
    def __init__(self, name, age, address, city, state, zipCode, TeacherID, ClassTeaching):
        super().__init__(name, age)

        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.TeacherID = TeacherID
        self.ClassingTeaching = ClassTeaching


student = Student("Jane Doe", 25, "123 Circle Drive", "Orange", "12345", 777, 3.8)
print("Student Name: ", student.name)
print("Student Age: ", student.age)
print("Student Address: ", student.address)
print("Student City: ", student.city)
print("Student Zipcode: ", student.zipCode)
print("Student ID: ", student.ID)
print("Student GPA: ", student.GPA)

print("\n")

teacher = Teacher("Ms.Cantor", 45, "456 Circle Drive", "Orange", "12346", 7, "Python")
print("Teacher Name: ", teacher.name)
print("Teacher Age: ", teacher.age)
print("Student Address: ", teacher.address)
print("Student City: ", teacher.city)
print("Student Zipcode: ", teacher.zipCode)
print("Teacher ID: ", teacher.TeacherID)
print("Teacher Course: ", teacher.ClassingTeaching)

''''
===============Output=================



'''


# ====================================
# Attached: Class Exercise #10
# ====================================
# File: Challenge Exercise #3
# ====================================
# Name: Automobiles
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

class Automobiles:
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    # these are the mutator methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    # these are the accessor methods
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price


def main():
    used_car = vehicles.Automobiles("Audi", 2022, 45000, 80000.0)
    print("Make: ", used_car.get_make())
    print("Model: ", used_car.get_model())
    print("Mileage: ", used_car.get_milage())
    print("Price: ", used_car.get_price())

    used_car1 = vehicles.Automobiles("Honda", 2022, 45000, 80000.0)
    print("Make: ", used_car1.get_make())
    print("Model: ", used_car1.get_model())
    print("Mileage: ", used_car1.get_milage())
    print("Price: ", used_car1.get_price())


main()

''''
===============Output=================



'''


# ====================================
# Attached: Class Exercise #10
# ====================================
# File: Challenge Exercise #4
# ====================================
# Name: Automobiles (part 2)
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

class Automobiles:
    def __init__(self, make, model, mileage, price, doors):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
        self.__doors = doors

    # these are the mutator methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    def set_doors(self, doors):
        self.__doors = doors

    # these are the accessor methods
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

    def get_doors(self):
        return self.__doors


def main():
    used_car = vehicles.Automobiles("Audi", 2022, 45000, 80000.0)
    print("Make: ", used_car.get_make())
    print("Model: ", used_car.get_model())
    print("Mileage: ", used_car.get_milage())
    print("Price: ", used_car.get_price())
    print("Doors: ", used_car.get_doors())

    used_car1 = vehicles.Automobiles("Honda", 2022, 45000, 80000.0)
    print("Make: ", used_car1.get_make())
    print("Model: ", used_car1.get_model())
    print("Mileage: ", used_car1.get_milage())
    print("Price: ", used_car1.get_price())
    print("Doors: ", used_car1.get_doors())


main()

''''
===============Output=================



'''


# ====================================
# Attached: Class Exercise #10
# ====================================
# File: Challenge Exercise #5
# ====================================
# Name: Automobiles (part 3)
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

class Automobiles:
    def __init__(self, make, model, mileage, price, doors):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
        self.__doors = doors

    # these are the mutator methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    def set_doors(self, doors):
        self.__doors = doors

    # these are the accessor methods
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

    def get_doors(self):
        return self.__doors


class Truck(Automobiles):
    def __init__(self, make, model, mileage, price):
        Automobiles.__init__(self, make, model, mileage, price)


class SUV(Automobiles):
    def __init__(self, make, model, mileage, price):
        Automobiles.__init__(self, make, model, mileage, price)


class Electric(Automobiles):
    def __init__(self, make, model, mileage, price):
        Automobiles.__init__(self, make, model, mileage, price)


def main():
    used_car = vehicles.Automobiles("Audi", 2022, 45000, 80000.0)
    used_car1 = vehicles.Automobiles("Honda", 2022, 45000, 80000.0)

    print("Make: ", used_car.get_make())
    print("Model: ", used_car.get_model())
    print("Mileage: ", used_car.get_milage())
    print("Price: ", used_car.get_price())
    print("\n")
    print("Make: ", used_car1.get_make())
    print("Model: ", used_car1.get_model())
    print("Mileage: ", used_car1.get_milage())
    print("Price: ", used_car1.get_price())

    print("\n")
    truck = vehicles.Truck("Toyota", "Tacoma", 40000, 12000.0)
    suv = vehicles.SUV("Volvo", "SE", 30000, 18500.0)
    electric = vehicles.Electric("BMW", "i7", 10000, 119300.0)

    # display the trucks data
    print("The following truck is in inventory ")
    print("Make: ", truck.get_make())
    print("Model: ", truck.get_model())
    print("Mileage: ", truck.get_milage())
    print("Price: ", truck.get_price())

    print("\n")

    # display the cars data
    print("The following car is in inventory ")
    print("Make: ", suv.get_make())
    print("Model: ", suv.get_model())
    print("Mileage: ", suv.get_milage())
    print("Price: ", suv.get_price())

    print("\n")

    # display the electric vehicle data
    print("The following electric vehicle is in inventory ")
    print("Make: ", electric.get_make())
    print("Model: ", electric.get_model())
    print("Mileage: ", electric.get_milage())
    print("Price: ", electric.get_price())


main()

''''
===============Output=================



'''


# ====================================
# Attached: Class Exercise #10
# ====================================
# File: Challenge Exercise #6
# ====================================
# Name: Employee
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift, pay_rate):
        Employee.__init__(self, name, number)
        self.__shift = shift
        self.__pay_rate = pay_rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def get_shift(self):
        return self.__shift

    def get_pay_rate(self):
        return self.__pay_rate


def main():
    name = input("Enter the Employee's name: ")
    number = input("Enter the Employee's number: ")
    shift = input("Enter the Employee's shift number: ")
    pay = input("Enter the Employee's pay rate: ")

    employee = ProductionWorker(name, number, shift, pay)

    print("Name: ", employee.get_name())
    print("Employee Number: ", employee.get_number())
    print("Shift Number: ", employee.get_shift())
    print("Pay rate: ", employee.get_pay_rate())


main()

''''
===============Output=================



'''

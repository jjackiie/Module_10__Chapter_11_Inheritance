# ====================================
# Attached: m13 homework #13
# ====================================
# File: Project #1
# ====================================
# Name: Shift Supervisor Class
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


class ShiftSupervisor(Employee):
    def __init__(self, name, number, salary, bonus):
        Employee.__init__(self, name, number)
        self.__salary = salary
        self.__bonus = bonus

    def set_salary(self, salary):
        self.__salary = salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus


def main():
    name = input("Enter the Supervisor's name: ")
    number = input("Enter the Supervisor's number: ")
    salary = input("Enter the Supervisor's salary: ")
    bonus = input("Enter the Supervisor's bonus ")

    Supervisor = ShiftSupervisor(name, number, salary, bonus)

    print("Name: ", Supervisor.get_name())
    print("Employee Number: ", Supervisor.get_number())
    print("Shift Number: ", Supervisor.get_salary())
    print("Pay rate: ", Supervisor.get_bonus())


main()

''''
===============Output=================



'''


# ====================================
# Attached: m13 homework #13
# ====================================
# File: Project #2
# ====================================
# Name: Person and Customer Classes
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone


class Customer(Person):
    def __init__(self, name, address, phone, mail):
        Person.__init__(self, name, address, phone)
        self.mailingList = "Y" == True
        self.__mail = mail

    def set_mail(self, mail):
        self.__mail = mail

    def get_mail(self):
        return self.__mail

    def mailList(self):
        if self.mailingList:
            return "on the mailing list"
        else:
            return "not on th emailing list"


def main():
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone = input("Enter the phone number: ")
    mail = input("Are you on the mailing list? ")

    customer = Customer(name, address, phone, mail)

    print("Name: ", customer.get_name())
    print("Address: ", customer.get_address())
    print("Phone: ", customer.get_phone())
    print("Mail: ", customer.get_mail())


main()

'''
===============Output=================



'''

"""
Encapsulation is one of the four fundamental principles of object-oriented programming (OOP),
 the other three being inheritance, polymorphism, and abstraction.

Python Encapsulation is one of the key features of object-oriented programming. Encapsulation refers to the bundling
of attributes and methods inside a single class.

It prevents outer classes from accessing and changing attributes and methods of a class.
This also helps to achieve data hiding.

In Python, we denote private attributes using underscore as the prefix i.e. single _ or double __. For example,
"""


class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"selling price is [{self.__maxprice}]")

    def set_max_price(self, price):
        self.__maxprice = price


# c = Computer()
# c.sell()
# c.set_max_price(1000)
# c.sell()
# c.__maxprice =500
# c.sell()
# Computer.__maxprice =450
# c.sell()

class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number  # Private attribute
        self._balance = balance  # Private attribute

    @property
    def balance(self):  # getter method
        return self._balance

    @balance.setter
    def balance(self,amount):
        if amount < 0:
            print("amount is negative")
        if amount > 0:
            print("amount is greater than zero")
            self._balance += amount

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit positive amount")


b = BankAccount('zeeshan', 50)
print(f"balance {b.balance}")
b.deposit(20)
print(f"balance {b.balance}")
b.balance=20
print(f"balance {b.balance}")

# Python Magic methods are the methods starting and ending with double underscores ‘__’. They are defined by built-in classes in Python and commonly used for operator overloading.

import csv
import os

current_directory = os.getcwd()

print("Current Working Directory:", current_directory)

# python .\main.py

# Creating classes


class Item:
    # class attributes
    pay_rate = 0.8  # the pay rate after 20% discount

    all = []

    # Magic method __init__
    # the contructor awaits certain data types
    def __init__(self, name: str, price: float, quantity: int = 0):
        print(
            f"Item created with name: {name}, price: {price} and quantity: {quantity}")
        # Run validations to the recieved arguments
        # if the value is lower than 0 we recieve an error
        assert price >= 0
        # we can pass own error messages
        assert quantity >= 0, f"Quantity {quantity} cannot be less than zero"

        # Assign to self objects
        self.name = name
        self.price = price
        self.quantity = quantity
        # working with assert

        # Actions to execute
        # After an instance being created it appends in the class atribute "all"
        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    # class method (can only be called from class level)
    # it needs a declarator
    @classmethod
    def instanciate_from_csv(cls):
        # for some reason the working directory is not where main.py is located
        with open(r"learning_git\python_oop\items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    # Python allways give the instanse to it owns methods as parameter "self". it wil be allways there and is convention do be written

    def calculate_Total_Price(self):
        return self.price * self.quantity

    def apply_discount_for_class(self):
        self.price = self.price * Item.pay_rate  # 1.using class attr on class lvl

    def apply_discount_for_instance(self):
        self.price = self.price * self.pay_rate  # 2.using class attr on instance lvl


item1 = Item("Phone", 100, 5)

# this is the same like (random_str is an istance of a class string)
random_str = str("aaa")

print(f"Total price of the item is {item1.calculate_Total_Price()}")

item2 = Item("Laptop", 1000, 2)

print(item2.calculate_Total_Price())

item2.has_numpad = False

# access class atributes
# we can du it on class level
print(Item.pay_rate)

# and instance level
print(item1.pay_rate)

# magic atributes
print(Item.__dict__)  # on class level
print(item1.__dict__)  # on instance level

item1.pay_rate = 0.5
item2.pay_rate = 0.5

# 1.using class attr on class lvl (stays undependent of the instance)
item1.apply_discount_for_class()
print(item1.price)
# 2.using class attr on instance lvl (we can change it)
item2.apply_discount_for_instance()
print(item2.price)

# initialise another 3 items
item2 = Item("Cable", 10, 5)
item3 = Item("Mouse", 50, 5)
item4 = Item("Keyboard", 75, 5)

print("--printing every object--")
for instance in Item.all:
    # after overwriting the __repr__ method we recieve another representation of an instance
    print(instance)


Item.instanciate_from_csv()
print(Item.all)

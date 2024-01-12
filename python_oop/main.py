# Python Magic methods are the methods starting and ending with double underscores ‘__’. They are defined by built-in classes in Python and commonly used for operator overloading.

from item import Item
import os

current_directory = os.getcwd()

print("Current Working Directory:", current_directory)

item1 = Item("MyItem", 750)
item1.name = "New Name"

print(item1.name)

item1.price = "12"

print(item1.price)


def old_test_function():
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


# old_test_function()

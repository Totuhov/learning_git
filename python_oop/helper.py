# WHen to use @classmethod and when to use @staticmethod

# the main difference between class and static methods is thath the class method should pass the instance as a first parametr, otherwise the static method dont expect any parameters
class Item:
    @staticmethod
    def print_something():
        print("Something")


Item.print_something()

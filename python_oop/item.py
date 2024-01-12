import csv


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
        self.__name = name
        self.__price = price
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
        with open("learning_git\python_oop\items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                # expecting float as we assert this with price: float in init method
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    # the static method declaration
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # Property Decorator = Read only Attribute (Getter)
    @property
    def name(self):
        return self.__name

    # This Decorator allow us to set value of the __name (Setter)
    @name.setter
    def name(self, value):
        # Validation
        if len(value) == 0:
            raise Exception("The Phone name must contains at least 1 sign!")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    # in this case we cann change the price only with these 2 methods(there is not setter)

    def apply_discount(self):
        # 2.using class attr on instance lvl
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    # Python allways give the instanse to it owns methods as parameter "self". it wil be allways there and is convention do be written

    def calculate_Total_Price(self):
        return self.__price * self.quantity

    def apply_discount_for_class(self):
        self.__price = self.__price * Item.pay_rate  # 1.using class attr on class lvl

    # Encapsulation (Read only attributes)

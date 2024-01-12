import csv

# Parent Class


class Item:
    pay_rate = 0.8

    all = []

    def __init__(self, name: str, price: float, quantity: int = 0):
        assert price >= 0
        assert quantity >= 0, f"Quantity {quantity} cannot be less than zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        # Generic way to get the name of the created class
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    @classmethod
    def instanciate_from_csv(cls):
        with open("learning_git\python_oop\items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    def calculate_Total_Price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

# Child Class


class Phone(Item):

    # using "super" function

    def __init__(self, name: str, price: float, quantity: int = 0, broken_phones: int = 0):
        # callig super function to have access to all attributes and methods from the super class
        super().__init__(
            name, price, quantity
        )

        assert broken_phones >= 0, f"Broken phones {broken_phones} cannot be less than zero"

        self.broken_phones = broken_phones

item1 = Item("testItem", 100, 1)
phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_Total_Price())
phone2 = Phone("jscPhonev20", 500, 5, 1)

print(Item.all)

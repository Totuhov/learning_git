import csv

# Also Static methods are explained in this file


class Item:
    pay_rate = 0.8

    all = []

    def __init__(self, name: str, price: float, quantity: int = 0):
        print(
            f"Item created with name: {name}, price: {price} and quantity: {quantity}")
        assert price >= 0
        assert quantity >= 0, f"Quantity {quantity} cannot be less than zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

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

    # the static method declaration
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def calculate_Total_Price(self):
        return self.price * self.quantity

    def apply_discount_for_class(self):
        self.price = self.price * Item.pay_rate

    def apply_discount_for_instance(self):
        self.price = self.price * self.pay_rate


Item.instanciate_from_csv()
print(Item.all)

print(Item.is_integer(7))
print(Item.is_integer(7.5))
print(Item.is_integer(7.0))

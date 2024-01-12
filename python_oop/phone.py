from item import Item


class Phone(Item):

    # using "super" function

    def __init__(self, name: str, price: float, quantity: int = 0, broken_phones: int = 0):
        # callig super function to have access to all attributes and methods from the super class
        super().__init__(
            name, price, quantity
        )

        assert broken_phones >= 0, f"Broken phones {broken_phones} cannot be less than zero"

        self.broken_phones = broken_phones

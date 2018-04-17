import datetime


class Item:
    last_item_id = 0

    def __init__(self, name, description, purchse_price, sell_price):
        Item.last_item_id += 1
        self.id = Item.last_item_id
        self.name = name
        self.description = description
        self.purchase_price = purchse_price
        self.sell_price = sell_price


class Electronics(Item):

    def __init__(self, name, description, purchase_price, sell_price, energy_class):
        super().__init__(name, description, purchase_price, sell_price)
        self.energy_class = energy_class


class Clothes(Item):

    def __init__(self, name, description, purchase_price, sell_price, size):
        super().__init__(name, description, purchase_price, sell_price)
        self.size = size


class Foods(Item):

    def __init__(self, name, description, purchase_price, sell_price, expiry_date):
        super().__init__(name, description, purchase_price, sell_price)
        self.expiry_date = expiry_date


Book = Item(name="Lord of the Rings", description="Adventure", purchse_price=12, sell_price=15)
Pen = Item(name="Bic", description="Black ball pen", purchse_price=0.5, sell_price=0.8)
Cellphone = Electronics(name='IPhone', description='5S', purchase_price=300, sell_price=370, energy_class='A1')
Milk = Foods(name='Good milk', description='cow milk', purchase_price=4, sell_price=6,
             expiry_date=datetime.date(year=2018, month=4, day=19))

class Item:
    _last_item_id = 0

    def __init__(self, name, description, purchse_price, sell_price):
        Item._last_item_id += 1
        self.id = Item._last_item_id
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

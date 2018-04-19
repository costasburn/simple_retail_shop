class Store:

    def __init__(self, name):
        self.name = name
        self._stock = {}

    def get_stock(self, item=None):
        if item is not None and item in self._stock:
                yield {item.name: self._stock[item]}
        else:
            for item in self._stock:
                yield {item.name: self._stock[item]}

    def add_item(self, item, quantity):
        self._stock[item] = self._stock.get(item, 0) + quantity
        return self._stock[item]

    def remove_item(self, item, quantity):
        try:
            if quantity <= self._stock[item]:
                self._stock[item] -= quantity
                return self._stock[item]
            else:
                return 0
        except KeyError:
            raise KeyError('Item not in stock')


import datetime


class Record:

    def __init__(self, invoice, item, quantity):
        invoice._last_record_id += 1
        self.id = invoice._last_record_id
        self.time = datetime.datetime.now()
        self.item = item
        self.quantity = quantity
        self.purchase_price = item.purchase_price

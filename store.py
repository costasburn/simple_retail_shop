import record


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

    def purchase_item(self, item, quantity, journal, invoice_in):
        self._stock[item] = self._stock.get(item, 0) + quantity
        new_record = record.Record(invoice=invoice_in, item=item, quantity=quantity)
        invoice_in.add_record(record=new_record)
        if invoice_in not in journal.get_invoices():
            journal.add_invoice(invoice=invoice_in)
        return {item.name: self._stock[item]}

    def sell_item(self, item, quantity, journal, invoice_out):
        try:
            if quantity <= self._stock[item]:
                new_record = record.Record(invoice=invoice_out, item=item, quantity=quantity)
                invoice_out.add_record(new_record)
                if invoice_out not in journal.get_invoices():
                    journal.add_invoice(invoice=invoice_out)
                self._stock[item] -= quantity
                return self._stock[item]
            else:
                return 0
        except KeyError:
            raise KeyError('Item not in stock')


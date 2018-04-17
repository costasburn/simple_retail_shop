import datetime


class Journal:

    def __init__(self, name):
        self.name = name
        self._invoices = []

    def add_invoice(self, invoice):
        self._invoices.append(invoice)

    def remove_invoice(self, invoice):
        for iter_invoice in self._invoices:
            if iter_invoice.item.name == invoice.item.name:
                self._invoices.remove(invoice)

    def get_invoices(self, date1=None, date2=None):
        self._invoices.sort(key=lambda invoice: invoice.time)

        lower_limit = date1 if not date1 is None else datetime.datetime.min
        upper_limit = date2 if not date2 is None else datetime.datetime.max

        return (invoice for invoice in self._invoices if lower_limit <= invoice.time <= upper_limit)


new_journal = Journal(name="Accountant's Log")

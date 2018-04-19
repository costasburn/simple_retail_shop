import datetime


class Journal:

    def __init__(self, name):
        self.name = name
        self._invoices_in = []
        self._invoices_out = []

    def add_invoice_sell(self, invoice):
        self._invoices_out.append(invoice)

    def add_invoice_purchase(self, invoice):
        self._invoices_in.append(invoice)

    def remove_invoice(self, invoice):
        for iter_invoice in self._invoices_in:
            if iter_invoice.id == invoice.id:
                self._invoices_in.remove(invoice)
        for iter_invoice in self._invoices_out:
            if iter_invoice.id == invoice.id:
                self._invoices_out.remove(invoice)

    def get_purchase_invoices(self, date1=None, date2=None):
        self._invoices_in.sort(key=lambda invoice: invoice.time)

        lower_limit = date1 if not date1 is None else datetime.datetime.min
        upper_limit = date2 if not date2 is None else datetime.datetime.max

        return (invoice for invoice in self._invoices_in if lower_limit <= invoice.time <= upper_limit)

    def get_sell_invoices(self, date1=None, date2=None):
        self._invoices_out.sort(key=lambda invoice: invoice.time)

        lower_limit = date1 if not date1 is None else datetime.datetime.min
        upper_limit = date2 if not date2 is None else datetime.datetime.max

        return (invoice for invoice in self._invoices_out if lower_limit <= invoice.time <= upper_limit)


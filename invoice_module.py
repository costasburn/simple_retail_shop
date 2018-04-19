import datetime
import record


class Invoice:
    _last_invoice_id = 0
    _last_record_id = 0

    def __init__(self):
        Invoice._last_invoice_id += 1
        self._records = []
        self.id = Invoice._last_invoice_id
        self.time = datetime.datetime.now()

    def create_purchase_record(self, store, item, quantity, journal):
        store.add_item(item=item, quantity=quantity)
        new_record = record.Record(invoice=self, item=item, quantity=quantity)
        self._records.append(new_record)
        if self not in journal.get_purchase_invoices():
            journal.add_invoice_purchase(invoice=self)
        return self._records

    def create_sell_record(self, store, item, quantity, journal):
        store.remove_item(item, quantity)
        new_record = record.Record(invoice=self, item=item, quantity=quantity)
        self._records.append(new_record)
        if self not in journal.get_sell_invoices():
            journal.add_invoice_sell(invoice=self)
        return self._records

    def erase_record(self, record):
        for iter_record in self._records:
            if record.id == iter_record.id:
                self._records.remove(record)

    def get_records(self, date1=None, date2=None):
        self._records.sort(key=lambda invoice: invoice.time)

        lower_limit = date1 if not date1 is None else datetime.datetime.min
        upper_limit = date2 if not date2 is None else datetime.datetime.max

        return (record for record in self._records if lower_limit <= record.time <= upper_limit)


class InvoiceIn(Invoice):

    def __init__(self, discount):
        super().__init__()
        self.discount = discount


class InvoiceOut(Invoice):

    def __init__(self, vendor):
        super().__init__()
        self.vendor = vendor

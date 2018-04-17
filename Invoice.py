import datetime


class Invoice:

    last_invoice_id = 0
    last_record_id = 0

    def __init__(self):
        Invoice.last_invoice_id += 1
        self._records = []
        self.id = Invoice.last_invoice_id
        self.time = datetime.datetime.now()

    def add_record(self, record):
        self._records.append(record)
        return self._records

    def erase_record(self, record):
        for iter_record in self._records:
            if record.item.name == iter_record.item.name:
                self._records.remove(record)

    def get_records(self, date1=None, date2=None):
        self._records.sort(key=lambda invoice : invoice.time)

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

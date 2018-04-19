import datetime


class Report:
    _last_report_id = 0

    def __init__(self):
        Report._last_report_id += 1
        self.id = Report._last_report_id

    def print_stock(self, stock):
        for item in stock:
            print(item)

    def print_invoices(self, invoices):
        invoices = list(invoices)
        invoices.sort(key=lambda invoice: invoice.id)
        print()
        print("INVOICES REPORT:")
        for invoice in invoices:
            print()
            print("Invoice ID:", invoice.id)
            for record in invoice.get_records():
                print()
                print("Record ID:", record.id)
                print(
                    "\nTime:            {}"
                    "\nItem:            {}"
                    "\nQuantity added:  {}"
                    "\nPurchase price:  {}".format(record.time, record.item.name,
                                                   record.quantity, record.purchase_price))
        print()

    def print_record(self, records):
        print()
        print("RECORDS REPORT:")
        print()
        for record in records:
            print("Record ID:", record.id)
            print(
                "\nTime:            {}"
                "\nItem:            {}"
                "\nQuantity added:  {}"
                "\nPurchase price:  {}".format(record.time, record.item.name,
                                               record.quantity, record.purchase_price))
        print()

    def sales_by_item(self, filter_item, journal, date1=None, date2=None):

        lower_limit = date1 if not date1 is None else datetime.datetime.min
        upper_limit = date2 if not date2 is None else datetime.datetime.max
        result = 0

        for invoice in journal.get_sell_invoices():
            for record in invoice.get_records():
                if record.item.name == filter_item.name and lower_limit <= record.time <= upper_limit:
                    result += record.quantity
        return result

    def profit_by_item(self, filter_item, journal, date1=None, date2=None):
        margin = filter_item.sell_price - filter_item.purchase_price
        sales = self.sales_by_item(filter_item=filter_item, journal=journal, date1=date1, date2=date2)
        result = sales * margin
        return result


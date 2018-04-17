import Invoice
import Item
import Journal
import Record
import Report


class Store:

    def __init__(self, name):
        self.name = name
        self._stock = {}

    def get_stock(self, item=None):
        if item is not None:
            yield {item.name: self._stock[item]}
        else:
            for item in self._stock:
                yield {item.name: self._stock[item]}

    def purchase_item(self, item, quantity, journal, invoice_in):
        self._stock[item] = self._stock.get(item, 0) + quantity
        new_record = Record.Record(invoice=invoice_in, item=item, quantity=quantity)
        invoice_in.add_record(record=new_record)
        if invoice_in not in journal.get_invoices():
            journal.add_invoice(invoice=invoice_in)
        return {item.name: self._stock[item]}

    def sell_item(self, item, quantity, journal, invoice_out):

        if quantity <= self._stock[item]:
            new_record = Record.Record(invoice=invoice_out, item=item, quantity=quantity)
            invoice_out.add_record(new_record)
            if invoice_out not in journal.get_invoices():
                journal.add_invoice(invoice=invoice_out)
            self._stock[item] -= quantity
            return {item.name: self._stock[item]}
        else:
            return 0


new_store = Store(name="Le Silpo")
new_invoice_in = Invoice.InvoiceIn(discount=0.1)
new_invoice_out = Invoice.InvoiceOut(vendor="John")
new_store.purchase_item(item=Item.Book, quantity=100, journal=Journal.new_journal, invoice_in=new_invoice_in)
new_store.purchase_item(item=Item.Pen, quantity=1000, journal=Journal.new_journal, invoice_in=new_invoice_in)
new_store.sell_item(item=Item.Pen, quantity=34, journal=Journal.new_journal, invoice_out=new_invoice_out)
new_store.sell_item(item=Item.Pen, quantity=21, journal=Journal.new_journal, invoice_out=new_invoice_out)
Report.new_report.print_stock(stock=new_store.get_stock())
Report.new_report.sales_by_item(filter_item=Item.Pen, journal=Journal.new_journal)
Report.new_report.profit_by_item(filter_item=Item.Pen, journal=Journal.new_journal)
Report.new_report.print_invoices(Journal.new_journal.get_invoices())

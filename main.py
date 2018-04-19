from item import Item
from item import Foods
from item import Electronics
from journal import Journal
from report import Report
from store import Store
from invoice_module import InvoiceOut
from invoice_module import InvoiceIn
import datetime


Book = Item(name="Lord of the Rings", description="Adventure", purchse_price=12, sell_price=15)
Pen = Item(name="Bic", description="Black ball pen", purchse_price=0.5, sell_price=0.8)
Cellphone = Electronics(name='IPhone', description='5S', purchase_price=300, sell_price=370, energy_class='A1')
Milk = Foods(name='Good milk', description='cow milk', purchase_price=4, sell_price=6,
             expiry_date=datetime.date(year=2018, month=4, day=19))
new_journal = Journal(name="Accountant's Log")
new_report = Report()
new_store = Store(name="Le Silpo")
new_invoice_in = InvoiceIn(discount=0.1)
new_invoice_out = InvoiceOut(vendor="John")
new_invoice_in.create_purchase_record(store=new_store, item=Book, quantity=100, journal=new_journal)
new_invoice_in.create_purchase_record(store=new_store, item=Pen, quantity=1000, journal=new_journal)
new_invoice_out.create_sell_record(store=new_store, item=Pen, quantity=34, journal=new_journal)
new_invoice_out.create_sell_record(store=new_store, item=Pen, quantity=21, journal=new_journal)
new_report.print_stock(stock=new_store.get_stock())
new_report.sales_by_item(filter_item=Pen, journal=new_journal)
new_report.profit_by_item(filter_item=Pen, journal=new_journal)
new_report.print_invoices(new_journal.get_sell_invoices())
new_report.print_invoices(new_journal.get_purchase_invoices())
from tkinter import messagebox
from model.item_model import Item
from model.customer_model import Customer
from db_connection.repository.invoice_repository import InvoiceRepository
from datetime import datetime
from invoice_template.doc_template import generate_invoice_pdf


class ItemController:
    def __init__(self, view):
        self.view = view
        self.invoiceRepo = InvoiceRepository()
        self.items = []

    def clear_form(self):
        self.view.customer_name.delete(0, 'end')
        self.view.customer_mobile.delete(0, 'end')
        self.view.address.delete(0, 'end')
        self.view.customer_email.delete(0, 'end')

        for row in self.view.item_tree.get_children():
            self.view.item_tree.delete(row)

        empty_item = self.view.item_tree.insert('', 'end',
            values=('📝 No items added yet - Click "Add" to start', '', '', ''))
        self.view.item_tree.item(empty_item, tags=('empty',))

    def add_items(self):
        item_name = self.view.item_name.get()
        quantity = self.view.item_quantity.get()
        rate = self.view.item_rate.get()

        if item_name and quantity and rate:
            quantity = int(quantity)
            rate = float(rate)
            amount = quantity * rate

            item = Item(item_name, quantity, rate, amount)
            self.items.append(item)

            self.view.item_tree.insert("", "end", values=(item.name, item.quantity, item.rate, item.amount))

            self.view.item_name.delete(0, 'end')
            self.view.item_quantity.delete(0, "end")
            self.view.item_rate.delete(0, "end")

    def create_invoice(self):
        customer_name = self.view.customer_name.get()
        customer_mobile = self.view.customer_mobile.get()
        address = self.view.address.get()
        customer_email = self.view.customer_email.get()

        if not customer_name or not customer_mobile or not address:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        # Show progress bar
        self.view.progress_label.grid()
        self.view.popup_progress_bar.set(0)
        self.view.popup_progress_bar.grid()
        self.view.update_idletasks()

        # Callback function to update progress
        def update_progress(value):
            self.view.popup_progress_bar.set(value)
            self.view.update_idletasks()

        customer = Customer(name=customer_name, mobile=customer_mobile, address=address, email=customer_email)
        customer_id = self.invoiceRepo.save_customer(customer)
        invoice_id = self.invoiceRepo.save_invoice(customer_id, datetime.now().strftime("%Y-%m-%d"))

        for item in self.items:
            product_id = self.invoiceRepo.save_product_if_needed(name=item.name, rate=item.rate)
            self.invoiceRepo.save_invoice_item(invoice_id, product_id, item.quantity, item.rate, item.amount)

        invoice_data = {
            "customer_name": customer.name,
            "address": customer.address,
            "mobile": customer.mobile,
            "invoice_no": invoice_id,
            "items": [
                {
                    "name": item.name,
                    "rate": item.rate,
                    "quantity": item.quantity,
                    "amount": item.amount,
                }
                for item in self.items
            ],
            "gross_total": sum(item.amount for item in self.items),
            "total": sum(item.amount for item in self.items) * 1.18
        }

        generate_invoice_pdf(invoice_data, progress_callback=update_progress)

        self.view.popup_progress_bar.set(1.0)
        self.view.update_idletasks()

        # Hide progress after finish
        self.view.popup_progress_bar.grid_remove()
        self.view.progress_label.grid_remove()

        self.items.clear()
        messagebox.showinfo("Success", f"Invoice created successfully!\nInvoice ID: {invoice_id}")
        return invoice_id



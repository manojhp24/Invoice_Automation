from db_connection.connection import get_connection
from db_connection.queries.queries import (SAVE_INVOICE, SAVE_INVOICE_ITEMS, SAVE_CUSTOMER, SAVE_PRODUCT_IF_NOT_EXISTS,
                                           GET_PRODUCT_ID,SAVE_NO_GST_CUSTOMER)


class InvoiceRepository:
    def __init__(self):
        self.conn = get_connection()
        self.cur = self.conn.cursor()

    def save_customer(self, customer):
        self.cur.execute(SAVE_CUSTOMER, (customer.name, customer.mobile, customer.email, customer.address,customer.customer_gst))
        self.conn.commit()
        return self.cur.lastrowid

    def save_invoice(self,customer_id,date):
        self.cur.execute(SAVE_INVOICE,(customer_id,date))
        self.conn.commit()
        return self.cur.lastrowid

    def save_product_if_needed(self, name, rate):
        self.cur.execute(GET_PRODUCT_ID, (name, rate))
        row = self.cur.fetchone()
        if row:
            return row[0]
        else:
            self.cur.execute(SAVE_PRODUCT_IF_NOT_EXISTS, (name, rate))
            self.conn.commit()
            return self.cur.lastrowid

    def save_invoice_item(self, invoice_id, product_id, quantity, rate, amount):
        self.cur.execute(SAVE_INVOICE_ITEMS, (invoice_id, product_id, quantity, rate, amount))
        self.conn.commit()

    def save_no_gst_customer(self,customer):
        self.cur.execute(SAVE_NO_GST_CUSTOMER,(customer.name, customer.mobile, customer.email, customer.address))

    def close(self):
        self.conn.close()

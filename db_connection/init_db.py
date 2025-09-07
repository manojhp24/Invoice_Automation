from db_connection.connection import get_connection
from db_connection.queries.create_table_queries import (CREATE_INVOICE_TABLE, CREATE_PRODUCTS_TABLE, CREATE_CUSTOMER_TABLE, CREATE_INVOICE_ITEMS,CREATE_NO_GST_CUSTOMER)


def initialize_db():
    conn = get_connection()
    cur = conn.cursor()

    #query-create-productTable
    cur.execute(CREATE_CUSTOMER_TABLE)
    cur.execute(CREATE_PRODUCTS_TABLE)
    cur.execute(CREATE_INVOICE_TABLE)
    cur.execute(CREATE_INVOICE_ITEMS)
    cur.execute(CREATE_NO_GST_CUSTOMER)


    conn.commit()
    conn.close()
CREATE_CUSTOMER_TABLE = """
CREATE TABLE IF NOT EXISTS customer (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  mobile TEXT,
  email TEXT,
  address TEXT
);

"""

CREATE_PRODUCTS_TABLE = """
CREATE TABLE IF NOT EXISTS products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  price REAL NOT NULL
);

"""

CREATE_INVOICE_TABLE = """
CREATE TABLE IF NOT EXISTS invoices (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id INTEGER,
  date TEXT,
  FOREIGN KEY (customer_id) REFERENCES customer(id)
);

"""

CREATE_INVOICE_ITEMS = """
CREATE TABLE IF NOT EXISTS invoice_items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  invoice_id INTEGER,
  product_id INTEGER,
  quantity INTEGER,
  rate REAL,
  amount REAL,
  FOREIGN KEY (invoice_id) REFERENCES invoices(id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);
"""

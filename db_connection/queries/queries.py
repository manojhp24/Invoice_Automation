SAVE_CUSTOMER = "INSERT INTO customer(name, mobile, email, address) VALUES (?, ?, ?, ?)"

SAVE_INVOICE = "INSERT INTO invoices(customer_id, date) VALUES (?, ?)"

GET_PRODUCT_ID = "SELECT id FROM products WHERE name = ? AND price = ?"

SAVE_PRODUCT_IF_NOT_EXISTS = "INSERT INTO products(name, price) VALUES (?, ?)"

SAVE_INVOICE_ITEMS = "INSERT INTO invoice_items(invoice_id, product_id, quantity, rate, amount) VALUES (?, ?, ?, ?, ?)"

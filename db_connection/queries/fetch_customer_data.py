FETCH_CUST_WITH_GST = """
SELECT c.name, c.mobile, c.address, c.customer_gst, i.id AS invoice_id
FROM invoices i
JOIN customer c ON i.customer_id = c.id
WHERE c.customer_gst IS NOT NULL AND c.customer_gst != '';
"""
FETCH_CUST_WITHOUT_GST = """
SELECT c.name, c.mobile, c.address, '' AS customer_gst, i.id AS invoice_id
FROM invoices i
JOIN customer c ON i.customer_id = c.id
WHERE c.customer_gst IS NULL OR c.customer_gst = '';
"""

FETCH_ALL = """
SELECT c.name, c.mobile, c.address, 
COALESCE(c.customer_gst, '') AS customer_gst, 
i.id AS invoice_id
FROM invoices i
JOIN customer c ON i.customer_id = c.id;
"""
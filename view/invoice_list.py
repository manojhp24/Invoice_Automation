import customtkinter as ctk
from tkinter import ttk

class InvoiceList(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.setup_ui()


    def setup_ui(self):
        self.create_invoice_list_table()

    def create_invoice_list_table(self):
        list_header_frame = ctk.CTkFrame(self, fg_color="transparent")
        list_header_frame.grid(row=7, column=0, columnspan=4, sticky="ew", padx=20, pady=(20, 10))

        item_header = ctk.CTkLabel(
            list_header_frame,
            text="📦 Invoice List",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=("#2E8B57", "#40E0D0")
        )
        item_header.grid(row=0, column=0, sticky="w")

        list_subtitle = ctk.CTkLabel(
            list_header_frame,
            text="List of invoices and customer Details",
            font=ctk.CTkFont(size=11),
            text_color=("gray50", "gray60")
        )
        list_subtitle.grid(row=1, column=0, sticky="w", pady=(2, 0))

        # Frame for Treeview + Scrollbars
        table_frame = ctk.CTkFrame(self, fg_color="transparent")
        table_frame.grid(row=8, column=0, columnspan=4, sticky="nsew", padx=20, pady=(0, 10))

        # Configure grid expand
        self.grid_rowconfigure(8, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Treeview
        columns = ("Customer Name", "Mobile", "Address", "Customer GST", "Invoice ID",'Action')
        invoice_list_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

        # Define headings
        for col in columns:
            invoice_list_table.heading(col, text=col)
            invoice_list_table.column(col, anchor="w", width=140)

        # Scrollbars
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=invoice_list_table.yview)
        hsb = ttk.Scrollbar(table_frame, orient="horizontal", command=invoice_list_table.xview)
        invoice_list_table.configure(yscroll=vsb.set, xscroll=hsb.set)

        # Layout
        invoice_list_table.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        invoice_list_table.insert("", "end", values=(
            "John Doe", "9876543210", "123 Street, City", "GST123XYZ", "INV001","View"
        ))

        return invoice_list_table

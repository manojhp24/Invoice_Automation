import customtkinter as ctk
from tkinter import ttk
from controller.Invoice_controller import ItemController


class InvoiceForm(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Configure grid weights for responsive layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.controller = ItemController(self)
        self.setup_ui()

    def setup_ui(self):
        # Header Section
        self.create_header()

        # Customer Information Section
        self.create_customer_section()

        self.add_item_section()

        self.create_item_list()

        self.create_actions_button()

    def create_header(self):

        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0, 20))
        header_frame.grid_columnconfigure(1, weight=1)

        # Title
        title_label = ctk.CTkLabel(
            header_frame,
            text="📄 Create New Invoice",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Separator line
        separator = ctk.CTkFrame(header_frame, height=2, fg_color=("gray70", "gray30"))
        separator.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(10, 0))

    def create_customer_section(self):
        """Create customer information section"""
        # Section header
        customer_header = ctk.CTkLabel(
            self,
            text="👤 Customer Information",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        customer_header.grid(row=1, column=0, columnspan=4, sticky="w", padx=10, pady=(10, 5))

        # Customer frame for better organization
        customer_frame = ctk.CTkFrame(self, fg_color=("gray90", "gray20"))
        customer_frame.grid(row=2, column=0, columnspan=4, sticky="ew", padx=10, pady=5)
        customer_frame.grid_columnconfigure(1, weight=1)
        customer_frame.grid_columnconfigure(3, weight=1)

        # Customer Name
        ctk.CTkLabel(
            customer_frame,
            text="Customer Name:",
            font=ctk.CTkFont(weight="bold")
        ).grid(row=0, column=0, padx=15, pady=15, sticky="w")

        self.customer_name = ctk.CTkEntry(
            customer_frame,
            width=280,
            height=35,
            placeholder_text="Enter customer name"
        )
        self.customer_name.grid(row=0, column=1, padx=10, pady=15, sticky="ew")

        # Mobile Number
        ctk.CTkLabel(
            customer_frame,
            text="Mobile Number:",
            font=ctk.CTkFont(weight="bold")
        ).grid(row=1, column=0, padx=15, pady=(0, 15), sticky="w")

        self.customer_mobile = ctk.CTkEntry(
            customer_frame,
            width=280,
            height=35,
            placeholder_text="Enter mobile number"
        )
        self.customer_mobile.grid(row=1, column=1, padx=10, pady=(0, 15), sticky="ew")

        # Address
        ctk.CTkLabel(
            customer_frame,
            text="Address",
            font=ctk.CTkFont(weight="bold")
        ).grid(row=0, column=2, padx=10, pady=10, sticky="w")

        self.address = ctk.CTkEntry(
            customer_frame,
            width=280,
            height=35,
            placeholder_text="Enter customer address"
        )
        self.address.grid(row=0, column=3, padx=15, pady=15, sticky="ew")

        # Email (new field)
        ctk.CTkLabel(
            customer_frame,
            text="Email:",
            font=ctk.CTkFont(weight="bold")
        ).grid(row=1, column=2, padx=15, pady=(0, 15), sticky="w")

        self.customer_email = ctk.CTkEntry(
            customer_frame,
            width=280,
            height=35,
            placeholder_text="Enter email address"
        )
        self.customer_email.grid(row=1, column=3, padx=15, pady=(0, 15), sticky="ew")

    def add_item_section(self):
        # Section Header
        item_header = ctk.CTkLabel(
            self,
            text="➕ Add Items",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        item_header.grid(row=4, column=0, columnspan=4, sticky="w", padx=10, pady=(10, 5))

        # Frame
        items_frame = ctk.CTkFrame(self, fg_color=("gray90", "gray20"))
        items_frame.grid(row=5, column=0, columnspan=4, sticky="ew", padx=10, pady=5)
        items_frame.grid_columnconfigure(1, weight=1)
        items_frame.grid_columnconfigure(3, weight=1)

        # Row 1: Item Name & Quantity
        ctk.CTkLabel(
            items_frame,
            text="Item Name",
            font=ctk.CTkFont(weight="bold")
        ).grid(row=0, column=0, padx=15, pady=15, sticky="w")

        self.item_name = ctk.CTkEntry(
            items_frame,
            height=35,
            placeholder_text="Enter Item Name"
        )
        self.item_name.grid(row=0, column=1, padx=10, pady=15, sticky="ew")

        ctk.CTkLabel(
            items_frame,
            text="Quantity",
            font=ctk.CTkFont(weight="bold")
        ).grid(row=0, column=2, padx=15, pady=15, sticky="w")

        self.item_quantity = ctk.CTkEntry(
            items_frame,
            height=35,
            placeholder_text="Enter Quantity"
        )
        self.item_quantity.grid(row=0, column=3, padx=15, pady=15, sticky="ew")

        # Row 2: Rate & Add Button
        ctk.CTkLabel(
            items_frame,
            text="Rate",
            font=ctk.CTkFont(weight="bold")
        ).grid(row=1, column=0, padx=15, pady=(0, 15), sticky="w")

        self.item_rate = ctk.CTkEntry(
            items_frame,
            height=35,
            placeholder_text="Enter Rate"
        )
        self.item_rate.grid(row=1, column=1, padx=10, pady=(0, 15), sticky="ew")

        add_items = ctk.CTkButton(
            items_frame,
            text="Add",
            width=100,
            height=35,
            fg_color=("blue", "blue"),
            command=self.controller.add_items
        )
        add_items.grid(row=1, column=3, padx=15, pady=(0, 15), sticky="e")

    def create_item_list(self):
        columns = ["Item Name", "Quantity", "Rate", "Amount"]

        # Header
        item_header = ctk.CTkLabel(
            self,
            text="📦 Items List",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        item_header.grid(row=7, column=0, columnspan=4, sticky="w", padx=10, pady=(10, 5))

        # Table Frame
        table_frame = ctk.CTkFrame(self, fg_color=("gray90", "gray20"))
        table_frame.grid(row=8, column=0, columnspan=4, sticky="nsew", padx=10, pady=5)
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

        # Scrollbars
        tree_scroll_y = ttk.Scrollbar(table_frame, orient="vertical")
        tree_scroll_y.grid(row=0, column=1, sticky="ns")

        tree_scroll_x = ttk.Scrollbar(table_frame, orient="horizontal")
        tree_scroll_x.grid(row=1, column=0, sticky="ew")

        # Treeview
        self.item_tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            yscrollcommand=tree_scroll_y.set,
            xscrollcommand=tree_scroll_x.set
        )
        self.item_tree.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        tree_scroll_y.config(command=self.item_tree.yview)
        tree_scroll_x.config(command=self.item_tree.xview)

        # Column headers and widths
        for col in columns:
            self.item_tree.heading(col, text=col)
            self.item_tree.column(col, anchor="center", width=150, stretch=True)

        # Style (Dark or Light Theme Support)
        style = ttk.Style()
        style.theme_use("default")

        style.configure("Treeview",
                        background="#1e1e1e",
                        foreground="white",
                        rowheight=30,
                        fieldbackground="#1e1e1e",
                        bordercolor="black",
                        borderwidth=0)

        style.configure("Treeview.Heading",
                        background="#333333",
                        foreground="white",
                        font=('Arial', 12, 'bold'))

        style.map("Treeview.Heading",
                  background=[("active", "#555555")])  # Change this to desired hover color

    def create_actions_button(self):
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=10, column=0, columnspan=4, pady=30)

        # Save Draft button
        save_draft_btn = ctk.CTkButton(
            button_frame,
            text="💾 Save Draft",
            width=150,
            height=40,
            fg_color=("gray60", "gray40"),
        )
        save_draft_btn.grid(row=0, column=0, padx=10)

        # Preview Button
        preview_button = ctk.CTkButton(
            button_frame,
            text="Preview Invoice",
            width=150,
            height=40,
            fg_color=("blue", "blue")
        )
        preview_button.grid(row=0, column=1, padx=10)

        clear_button = ctk.CTkButton(
            button_frame,
            text="Clear Form",
            width=150,
            height=40,
            command=self.controller.clear_form
        )
        clear_button.grid(row=0, column=2, padx=10)

        # Create Invoice Button
        create_invoice_button = ctk.CTkButton(
            button_frame,
            text="Generate Invoice",
            width=150,
            height=40,
            fg_color=("green", "green"),
            command=self.controller.create_invoice,
        )
        create_invoice_button.grid(row=0, column=3, padx=10)










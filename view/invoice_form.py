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
        """Create enhanced header section with modern styling"""
        header_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
            corner_radius=0
        )
        header_frame.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0, 30))
        header_frame.grid_columnconfigure(0, weight=1)

        # Main title with gradient-like effect using shadow
        title_shadow = ctk.CTkLabel(
            header_frame,
            text="📄 Create New Invoice",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color=("gray60", "gray40")
        )
        title_shadow.grid(row=0, column=0, pady=(12, 0), padx=2)

        title_label = ctk.CTkLabel(
            header_frame,
            text="📄 Create New Invoice",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color=("#2E8B57", "#40E0D0")  # Sea green to turquoise gradient
        )
        title_label.grid(row=0, column=0, pady=10)

        # Subtitle for better context
        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="Fill in the details below to generate your professional invoice",
            font=ctk.CTkFont(size=12),
            text_color=("gray50", "gray60")
        )
        subtitle_label.grid(row=1, column=0, pady=(0, 15))

        # Enhanced separator with gradient effect
        separator_frame = ctk.CTkFrame(header_frame, height=4, fg_color="transparent")
        separator_frame.grid(row=2, column=0, sticky="ew", pady=(5, 0))
        separator_frame.grid_columnconfigure(0, weight=1)

        # Multiple thin lines for gradient effect
        separator1 = ctk.CTkFrame(separator_frame, height=1, fg_color=("#2E8B57", "#40E0D0"))
        separator1.grid(row=0, column=0, sticky="ew", pady=1)

        separator2 = ctk.CTkFrame(separator_frame, height=1, fg_color=("gray80", "gray40"))
        separator2.grid(row=1, column=0, sticky="ew")

    def create_customer_section(self):
        """Create enhanced customer information section with modern card design"""
        # Section header with icon and improved typography
        customer_header_frame = ctk.CTkFrame(self, fg_color="transparent")
        customer_header_frame.grid(row=1, column=0, columnspan=4, sticky="ew", padx=20, pady=(20, 10))
        customer_header_frame.grid_columnconfigure(0, weight=1)

        customer_header = ctk.CTkLabel(
            customer_header_frame,
            text="👤 Customer Information",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=("#2E8B57", "#40E0D0")
        )
        customer_header.grid(row=0, column=0, sticky="w")

        # Subtitle for section
        customer_subtitle = ctk.CTkLabel(
            customer_header_frame,
            text="Enter your client's contact details and information",
            font=ctk.CTkFont(size=11),
            text_color=("gray50", "gray60")
        )
        customer_subtitle.grid(row=1, column=0, sticky="w", pady=(2, 0))

        # Enhanced customer frame with modern card design
        customer_frame = ctk.CTkFrame(
            self,
            fg_color=("white", "gray15"),
            corner_radius=15,
            border_width=1,
            border_color=("gray85", "gray25")
        )
        customer_frame.grid(row=2, column=0, columnspan=4, sticky="ew", padx=20, pady=(10, 20))
        customer_frame.grid_columnconfigure(1, weight=1)
        customer_frame.grid_columnconfigure(3, weight=1)

        # Row 1: Customer Name and Address
        # Customer Name
        name_label = ctk.CTkLabel(
            customer_frame,
            text="Customer Name *",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=("#2E4057", "#E8E8E8")
        )
        name_label.grid(row=0, column=0, padx=20, pady=(20, 8), sticky="w")

        self.customer_name = ctk.CTkEntry(
            customer_frame,
            width=280,
            height=40,
            placeholder_text="Enter full customer name",
            font=ctk.CTkFont(size=12),
            corner_radius=8,
            border_width=2,
            border_color=("gray80", "gray30"),
            fg_color=("gray95", "gray10")
        )
        self.customer_name.grid(row=1, column=0, padx=20, pady=(0, 15), sticky="ew")

        # Address
        address_label = ctk.CTkLabel(
            customer_frame,
            text="Address *",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=("#2E4057", "#E8E8E8")
        )
        address_label.grid(row=0, column=2, padx=(20, 20), pady=(20, 8), sticky="w")

        self.address = ctk.CTkEntry(
            customer_frame,
            width=280,
            height=40,
            placeholder_text="Enter customer address",
            font=ctk.CTkFont(size=12),
            corner_radius=8,
            border_width=2,
            border_color=("gray80", "gray30"),
            fg_color=("gray95", "gray10")
        )
        self.address.grid(row=1, column=2, padx=(20, 20), pady=(0, 15), sticky="ew")

        # Row 2: Mobile Number and Email
        # Mobile Number
        mobile_label = ctk.CTkLabel(
            customer_frame,
            text="Mobile Number *",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=("#2E4057", "#E8E8E8")
        )
        mobile_label.grid(row=2, column=0, padx=20, pady=(5, 8), sticky="w")

        self.customer_mobile = ctk.CTkEntry(
            customer_frame,
            width=280,
            height=40,
            placeholder_text="Enter mobile number",
            font=ctk.CTkFont(size=12),
            corner_radius=8,
            border_width=2,
            border_color=("gray80", "gray30"),
            fg_color=("gray95", "gray10")
        )
        self.customer_mobile.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="ew")

        # Email
        email_label = ctk.CTkLabel(
            customer_frame,
            text="Email Address",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=("#2E4057", "#E8E8E8")
        )
        email_label.grid(row=2, column=2, padx=(20, 20), pady=(5, 8), sticky="w")

        self.customer_email = ctk.CTkEntry(
            customer_frame,
            width=280,
            height=40,
            placeholder_text="Enter email address (optional)",
            font=ctk.CTkFont(size=12),
            corner_radius=8,
            border_width=2,
            border_color=("gray80", "gray30"),
            fg_color=("gray95", "gray10")
        )
        self.customer_email.grid(row=3, column=2, padx=(20, 20), pady=(0, 20), sticky="ew")

    def add_item_section(self):
        """Create enhanced add items section with better layout"""
        # Section header
        item_header_frame = ctk.CTkFrame(self, fg_color="transparent")
        item_header_frame.grid(row=4, column=0, columnspan=4, sticky="ew", padx=20, pady=(20, 10))

        item_header = ctk.CTkLabel(
            item_header_frame,
            text="➕ Add Items",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=("#2E8B57", "#40E0D0")
        )
        item_header.grid(row=0, column=0, sticky="w")

        item_subtitle = ctk.CTkLabel(
            item_header_frame,
            text="Add products or services to your invoice",
            font=ctk.CTkFont(size=11),
            text_color=("gray50", "gray60")
        )
        item_subtitle.grid(row=1, column=0, sticky="w", pady=(2, 0))

        # Main items frame
        items_frame = ctk.CTkFrame(
            self,
            fg_color=("white", "gray15"),
            corner_radius=15,
            border_width=1,
            border_color=("gray85", "gray25")
        )
        items_frame.grid(row=5, column=0, columnspan=4, sticky="ew", padx=20, pady=(10, 20))

        # Configure columns for better spacing
        items_frame.grid_columnconfigure(0, weight=3)  # Item name gets more space
        items_frame.grid_columnconfigure(1, weight=1)  # Quantity
        items_frame.grid_columnconfigure(2, weight=1)  # Rate
        items_frame.grid_columnconfigure(3, weight=1)  # Button

        # All fields in one row for better layout
        # Item Name
        item_name_label = ctk.CTkLabel(
            items_frame,
            text="Item Name *",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=("#2E4057", "#E8E8E8")
        )
        item_name_label.grid(row=0, column=0, padx=(20, 10), pady=(15, 5), sticky="w")

        self.item_name = ctk.CTkEntry(
            items_frame,
            height=35,
            placeholder_text="Enter item name",
            font=ctk.CTkFont(size=11),
            corner_radius=6,
            border_width=1,
            border_color=("gray70", "gray40"),
            fg_color=("gray95", "gray10")
        )
        self.item_name.grid(row=1, column=0, padx=(20, 10), pady=(0, 20), sticky="ew")

        # Quantity
        quantity_label = ctk.CTkLabel(
            items_frame,
            text="Quantity *",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=("#2E4057", "#E8E8E8")
        )
        quantity_label.grid(row=0, column=1, padx=5, pady=(15, 5), sticky="w")

        self.item_quantity = ctk.CTkEntry(
            items_frame,
            height=35,
            placeholder_text="Qty",
            font=ctk.CTkFont(size=11),
            corner_radius=6,
            border_width=1,
            border_color=("gray70", "gray40"),
            fg_color=("gray95", "gray10")
        )
        self.item_quantity.grid(row=1, column=1, padx=5, pady=(0, 20), sticky="ew")

        # Rate
        rate_label = ctk.CTkLabel(
            items_frame,
            text="Rate *",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=("#2E4057", "#E8E8E8")
        )
        rate_label.grid(row=0, column=2, padx=5, pady=(15, 5), sticky="w")

        self.item_rate = ctk.CTkEntry(
            items_frame,
            height=35,
            placeholder_text="Price",
            font=ctk.CTkFont(size=11),
            corner_radius=6,
            border_width=1,
            border_color=("gray70", "gray40"),
            fg_color=("gray95", "gray10")
        )
        self.item_rate.grid(row=1, column=2, padx=5, pady=(0, 20), sticky="ew")

        # Add Button
        add_button_label = ctk.CTkLabel(
            items_frame,
            text="Action",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=("#2E4057", "#E8E8E8")
        )
        add_button_label.grid(row=0, column=3, padx=(10, 20), pady=(15, 5), sticky="w")

        add_items = ctk.CTkButton(
            items_frame,
            text="+ Add",
            width=90,
            height=35,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=("#2E8B57", "#40E0D0"),
            hover_color=("#228B22", "#20B2AA"),
            corner_radius=6,
            command=self.controller.add_items
        )
        add_items.grid(row=1, column=3, padx=(10, 20), pady=(0, 20), sticky="ew")

    def create_item_list(self):
        """Create enhanced and visually appealing items table"""
        columns = ["Item Name", "Quantity", "Rate", "Amount"]

        # Enhanced header section
        list_header_frame = ctk.CTkFrame(self, fg_color="transparent")
        list_header_frame.grid(row=7, column=0, columnspan=4, sticky="ew", padx=20, pady=(20, 10))

        item_header = ctk.CTkLabel(
            list_header_frame,
            text="📦 Items List",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=("#2E8B57", "#40E0D0")
        )
        item_header.grid(row=0, column=0, sticky="w")

        list_subtitle = ctk.CTkLabel(
            list_header_frame,
            text="Review your invoice items",
            font=ctk.CTkFont(size=11),
            text_color=("gray50", "gray60")
        )
        list_subtitle.grid(row=1, column=0, sticky="w", pady=(2, 0))

        # Enhanced table container with better styling
        table_container = ctk.CTkFrame(
            self,
            fg_color="#f8f9fa",
            corner_radius=12,
            border_width=2,
            border_color="#2E8B57"
        )
        table_container.grid(row=8, column=0, columnspan=4, sticky="nsew", padx=20, pady=(10, 20))
        table_container.grid_rowconfigure(0, weight=1)
        table_container.grid_columnconfigure(0, weight=1)

        # Create enhanced treeview
        self.item_tree = ttk.Treeview(
            table_container,
            columns=columns,
            show="headings",
            height=8
        )
        self.item_tree.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Enhanced column configuration
        self.item_tree.heading("Item Name", text="📋 Item Name", anchor="w")
        self.item_tree.heading("Quantity", text="📊 Qty", anchor="center")
        self.item_tree.heading("Rate", text="💰 Rate", anchor="center")
        self.item_tree.heading("Amount", text="💵 Amount", anchor="center")

        # Better column widths and alignment
        self.item_tree.column("Item Name", width=300, anchor="w", minwidth=200)
        self.item_tree.column("Quantity", width=100, anchor="center", minwidth=80)
        self.item_tree.column("Rate", width=120, anchor="center", minwidth=100)
        self.item_tree.column("Amount", width=120, anchor="center", minwidth=100)

        # Professional styling
        style = ttk.Style()

        # Enhanced treeview styling
        style.configure("Treeview",
                        background="white",
                        foreground="#2c3e50",
                        rowheight=35,
                        fieldbackground="white",
                        borderwidth=0,
                        font=('Segoe UI', 11))

        # Professional header styling
        style.configure("Treeview.Heading",
                        background="#2E8B57",
                        foreground="black",
                        font=('Segoe UI', 11, 'bold'),
                        relief="flat",
                        borderwidth=0)

        # Enhanced selection and hover effects
        style.map("Treeview",
                  background=[("selected", "#e8f5e8"), ("focus", "#f0f8f0")],
                  foreground=[("selected", "#2E8B57")])

        style.map("Treeview.Heading",
                  background=[("active", "#228B22")])

        # Add scrollbar with custom styling
        scrollbar = ttk.Scrollbar(table_container, orient="vertical", command=self.item_tree.yview)
        self.item_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns", padx=(0, 5), pady=10)

        # Configure scrollbar styling
        style.configure("Vertical.TScrollbar",
                        background="#e0e0e0",
                        bordercolor="#cccccc",
                        arrowcolor="#666666",
                        darkcolor="#d0d0d0",
                        lightcolor="#f0f0f0")

        # Add alternating row colors for better readability
        self.item_tree.tag_configure('oddrow',
                                     background="#f8f9fa",
                                     foreground="#2c3e50")
        self.item_tree.tag_configure('evenrow',
                                     background="white",
                                     foreground="#2c3e50")

        # Add empty state message
        if not hasattr(self, '_empty_message_added'):
            empty_item = self.item_tree.insert('', 'end', values=('No items added yet', '', '', ''))
            self.item_tree.set(empty_item, 'Item Name', '📝 No items added yet - Click "Add" to start')
            self.item_tree.item(empty_item, tags=('empty',))
            self.item_tree.tag_configure('empty',
                                         background="#f8f9fa",
                                         foreground="#6c757d",
                                         font=('Segoe UI', 10, 'italic'))
            self._empty_message_added = True

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










# view/invoice_form.py

import customtkinter as ctk
from datetime import datetime


class InvoiceForm(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Configure main frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create scrollable frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Configure scrollable frame grid weights
        self.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.scrollable_frame.grid_columnconfigure(3, weight=1)

        self.setup_ui()

    def setup_ui(self):
        # Header Section
        self.create_header()

        # Customer Information Section
        self.create_customer_section()

        # Invoice Details Section
        self.create_invoice_section()

        # Items Section (placeholder for future enhancement)
        self.create_items_section()

        # Action Buttons
        self.create_action_buttons()

    def create_header(self):
        """Create the header section with title"""
        header_frame = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
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
            self.scrollable_frame,
            text="👤 Customer Information",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        customer_header.grid(row=1, column=0, columnspan=4, sticky="w", padx=10, pady=(10, 5))

        # Customer frame for better organization
        customer_frame = ctk.CTkFrame(self.scrollable_frame, fg_color=("gray90", "gray20"))
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
            text="Address:",
            font=ctk.CTkFont(weight="bold")
        ).grid(row=0, column=2, padx=15, pady=15, sticky="w")

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

    def create_invoice_section(self):
        """Create invoice details section"""
        # Section header
        invoice_header = ctk.CTkLabel(
            self.scrollable_frame,
            text="📋 Invoice Details",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        invoice_header.grid(row=3, column=0, columnspan=4, sticky="w", padx=10, pady=(20, 5))

        # Invoice frame
        invoice_frame = ctk.CTkFrame(self.scrollable_frame, fg_color=("gray90", "gray20"))
        invoice_frame.grid(row=4, column=0, columnspan=4, sticky="ew", padx=10, pady=5)
        invoice_frame.grid_columnconfigure(1, weight=1)
        invoice_frame.grid_columnconfigure(3, weight=1)

        # Invoice Number
        ctk.CTkLabel(
            invoice_frame,
            text="Invoice No:",
            font=ctk.CTkFont(weight="bold")
        ).grid(row=0, column=0, padx=15, pady=15, sticky="w")

        self.invoice_no = ctk.CTkEntry(
            invoice_frame,
            width=280,
            height=35,
            placeholder_text="Auto-generated"
        )
        self.invoice_no.grid(row=0, column=1, padx=10, pady=15, sticky="ew")

        # Invoice Date
        ctk.CTkLabel(
            invoice_frame,
            text="Invoice Date:",
            font=ctk.CTkFont(weight="bold")
        ).grid(row=0, column=2, padx=15, pady=15, sticky="w")

        self.invoice_date = ctk.CTkEntry(
            invoice_frame,
            width=280,
            height=35
        )
        self.invoice_date.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.invoice_date.grid(row=0, column=3, padx=15, pady=15, sticky="ew")

        # Due Date
        ctk.CTkLabel(
            invoice_frame,
            text="Due Date:",
            font=ctk.CTkFont(weight="bold")
        ).grid(row=1, column=0, padx=15, pady=(0, 15), sticky="w")

        self.due_date = ctk.CTkEntry(
            invoice_frame,
            width=280,
            height=35,
            placeholder_text="YYYY-MM-DD"
        )
        self.due_date.grid(row=1, column=1, padx=10, pady=(0, 15), sticky="ew")

        # Payment Terms
        ctk.CTkLabel(
            invoice_frame,
            text="Payment Terms:",
            font=ctk.CTkFont(weight="bold")
        ).grid(row=1, column=2, padx=15, pady=(0, 15), sticky="w")

        self.payment_terms = ctk.CTkComboBox(
            invoice_frame,
            width=280,
            height=35,
            values=["Net 30", "Net 15", "Due on Receipt", "Net 60", "Custom"]
        )
        self.payment_terms.set("Net 30")
        self.payment_terms.grid(row=1, column=3, padx=15, pady=(0, 15), sticky="ew")

    def create_items_section(self):
        """Create items section placeholder"""
        # Section header
        items_header = ctk.CTkLabel(
            self,
            text="🛍️ Invoice Items",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        items_header.grid(row=5, column=0, columnspan=4, sticky="w", padx=10, pady=(20, 5))

        # Items frame
        items_frame = ctk.CTkFrame(self, fg_color=("gray90", "gray20"))
        items_frame.grid(row=6, column=0, columnspan=4, sticky="ew", padx=10, pady=5)

        # Placeholder for items table
        placeholder_label = ctk.CTkLabel(
            items_frame,
            text="📝 Items will be added here\n(This section can be enhanced with a table for multiple items)",
            font=ctk.CTkFont(size=12),
            text_color=("gray60", "gray40")
        )
        placeholder_label.grid(row=0, column=0, pady=30, padx=20)

        # Quick add item section
        quick_add_frame = ctk.CTkFrame(items_frame, fg_color="transparent")
        quick_add_frame.grid(row=1, column=0, sticky="ew", padx=15, pady=(0, 15))
        quick_add_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(quick_add_frame, text="Quick Add:", font=ctk.CTkFont(weight="bold")).grid(row=0, column=0,
                                                                                               padx=(0, 10), sticky="w")

        self.quick_item = ctk.CTkEntry(quick_add_frame, placeholder_text="Item description", height=35)
        self.quick_item.grid(row=0, column=1, padx=5, sticky="ew")

        self.quick_price = ctk.CTkEntry(quick_add_frame, placeholder_text="Price", width=100, height=35)
        self.quick_price.grid(row=0, column=2, padx=5)

        ctk.CTkButton(quick_add_frame, text="+ Add", width=60, height=35).grid(row=0, column=3, padx=(5, 0))

    def create_action_buttons(self):
        """Create action buttons section"""
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=7, column=0, columnspan=4, pady=30)

        # Save Draft button
        save_draft_btn = ctk.CTkButton(
            button_frame,
            text="💾 Save Draft",
            width=150,
            height=40,
            fg_color=("gray60", "gray40"),
            command=self.save_draft
        )
        save_draft_btn.grid(row=0, column=0, padx=10)

        # Preview button
        preview_btn = ctk.CTkButton(
            button_frame,
            text="👁️ Preview",
            width=150,
            height=40,
            fg_color=("blue", "blue"),
            command=self.preview_invoice
        )
        preview_btn.grid(row=0, column=1, padx=10)

        # Create Invoice button
        create_btn = ctk.CTkButton(
            button_frame,
            text="✅ Create Invoice",
            width=150,
            height=40,
            fg_color=("green", "green"),
            command=self.submit_invoice
        )
        create_btn.grid(row=0, column=2, padx=10)

        # Clear Form button
        clear_btn = ctk.CTkButton(
            button_frame,
            text="🗑️ Clear Form",
            width=150,
            height=40,
            fg_color=("red", "red"),
            command=self.clear_form
        )
        clear_btn.grid(row=0, column=3, padx=10)

    def submit_invoice(self):
        """Handle invoice submission"""
        # Collect all form data
        invoice_data = {
            "customer_name": self.customer_name.get(),
            "customer_mobile": self.customer_mobile.get(),
            "customer_email": self.customer_email.get(),
            "address": self.address.get(),
            "invoice_no": self.invoice_no.get(),
            "invoice_date": self.invoice_date.get(),
            "due_date": self.due_date.get(),
            "payment_terms": self.payment_terms.get(),
            "quick_item": self.quick_item.get(),
            "quick_price": self.quick_price.get()
        }

        # Basic validation
        if not invoice_data["customer_name"]:
            self.show_message("Error", "Customer name is required!")
            return

        print("Invoice Data:", invoice_data)
        self.show_message("Success", "Invoice created successfully!")

    def save_draft(self):
        """Save invoice as draft"""
        print("Saving draft...")
        self.show_message("Info", "Invoice saved as draft!")

    def preview_invoice(self):
        """Preview invoice before creating"""
        print("Previewing invoice...")
        self.show_message("Info", "Invoice preview (feature to be implemented)")

    def clear_form(self):
        """Clear all form fields"""
        fields = [
            self.customer_name, self.customer_mobile, self.customer_email,
            self.address, self.invoice_no, self.due_date, self.quick_item, self.quick_price
        ]

        for field in fields:
            field.delete(0, 'end')

        # Reset date to today
        self.invoice_date.delete(0, 'end')
        self.invoice_date.insert(0, datetime.now().strftime("%Y-%m-%d"))

        # Reset payment terms
        self.payment_terms.set("Net 30")

        print("Form cleared!")

    def show_message(self, title, message):
        """Show message dialog (placeholder - implement with actual dialog)"""
        print(f"{title}: {message}")
        # In a real implementation, you'd use CTkMessageBox or similar
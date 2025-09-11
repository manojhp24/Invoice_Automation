import customtkinter as ctk
from tkinter import ttk
from controller import Invoice_controller


class InvoiceList(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.controller = Invoice_controller.InvoiceRepository()

        # Color scheme matching the sidebar
        self.colors = {
            "primary": ("#4C78E8", "#4C78E8"),
            "secondary": ("#3A3E4B", "#3A3E4B"),
            "background": ("#2A2D37", "#2A2D37"),
            "border": ("#3A3E4B", "#3A3E4B"),
            "text_primary": ("#E4E4E4", "#E4E4E4"),
            "text_secondary": ("#8A8D93", "#8A8D93"),
            "table_header": ("#4C78E8", "#4C78E8"),
            "table_bg": ("#2A2D37", "#2A2D37"),
            "table_fg": ("#E4E4E4", "#E4E4E4"),
            "row_odd": ("#2A2D37", "#2A2D37"),
            "row_even": ("#3A3E4B", "#3A3E4B"),
            "selected": ("#4C78E8", "#4C78E8"),
            "selected_text": ("#FFFFFF", "#FFFFFF")
        }

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.setup_ui()

    def setup_ui(self):
        self.create_header()
        self.create_invoice_list_table()
        # 🔹 Load all invoices initially
        self.apply_filter()

    def create_header(self):
        """Create enhanced header section"""
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.grid(row=0, column=0, columnspan=4, sticky="ew", padx=20, pady=(20, 15))
        header_frame.grid_columnconfigure(0, weight=1)

        # Main title
        title_label = ctk.CTkLabel(
            header_frame,
            text="📦 Invoice List",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=self.colors["primary"]
        )
        title_label.grid(row=0, column=0, sticky="w", pady=(0, 5))

        # Subtitle
        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="Manage and view all your invoices in one place",
            font=ctk.CTkFont(size=12),
            text_color=self.colors["text_secondary"]
        )
        subtitle_label.grid(row=1, column=0, sticky="w", pady=(0, 10))

        # 🔹 Filter section with ComboBox + Button
        filter_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        filter_frame.grid(row=2, column=0, sticky="w", pady=(5, 5))

        filter_label = ctk.CTkLabel(
            filter_frame,
            text="Filter by:",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=self.colors["text_primary"]
        )
        filter_label.pack(side="left", padx=(0, 10))

        # ComboBox
        self.filter_combo = ctk.CTkComboBox(
            filter_frame,
            values=["All","With GST","Without GST"],
            width=150,
            state="readonly"
        )
        self.filter_combo.set("All")  # default
        self.filter_combo.pack(side="left", padx=(0, 10))

        # Filter button
        filter_btn = ctk.CTkButton(
            filter_frame,
            text="Apply",
            width=80,
            fg_color=self.colors["primary"][0],
            hover_color="#3A66D0",
            command=self.apply_filter  # 🔹 connect to method
        )
        filter_btn.pack(side="left")

        # Separator line
        separator = ctk.CTkFrame(header_frame, height=2, fg_color=self.colors["primary"])
        separator.grid(row=3, column=0, sticky="ew", pady=(10, 0))

    def apply_filter(self):
        """Filter invoices based on combo selection and reload table"""
        selected_filter = self.filter_combo.get()

        # Clear existing rows
        for row in self.invoice_list_table.get_children():
            self.invoice_list_table.delete(row)

        # Default value
        data = []

        # 🔹 Fetch data from repository
        if selected_filter == "With GST":
            data = self.controller.fetch_gst_customer()
        elif selected_filter == "Without GST":
            data = self.controller.fetch_without_gst_customer()
        elif selected_filter == "All":
            data = self.controller.fetch_all_cust()

        # 🔹 Insert rows into table with alternate row colors
        for i, row in enumerate(data):
            # row = (name, mobile, address, customer_gst, invoice_id)
            row_with_action = row + ("View",)  # add Action column
            tags = ('evenrow',) if i % 2 == 0 else ('oddrow',)
            self.invoice_list_table.insert("", "end", values=row_with_action, tags=tags)

    def create_invoice_list_table(self):
        # Main container for the table
        table_container = ctk.CTkFrame(
            self,
            fg_color=self.colors["background"],
            corner_radius=12,
            border_width=1,
            border_color=self.colors["border"]
        )
        table_container.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        table_container.grid_rowconfigure(0, weight=1)
        table_container.grid_columnconfigure(0, weight=1)

        # Frame for Treeview + Scrollbars
        table_frame = ctk.CTkFrame(table_container, fg_color="transparent")
        table_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

        # Treeview
        columns = ("Customer Name", "Mobile", "Address", "Customer GST", "Invoice ID", "Action")
        self.invoice_list_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)

        # Configure column widths and headings
        column_config = [
            ("Customer Name", "👤 Customer Name", 180),
            ("Mobile", "📱 Mobile", 120),
            ("Address", "🏠 Address", 200),
            ("Customer GST", "📋 GST Number", 120),
            ("Invoice ID", "📄 Invoice ID", 100),
            ("Action", "⚡ Action", 80)
        ]

        for col, heading, width in column_config:
            self.invoice_list_table.heading(col, text=heading, anchor="w")
            self.invoice_list_table.column(col, anchor="w", width=width, minwidth=80)

        # Style setup
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Treeview",
                        background=self.colors["table_bg"][0],
                        foreground=self.colors["table_fg"][0],
                        rowheight=35,
                        fieldbackground=self.colors["table_bg"][0],
                        borderwidth=0,
                        font=('Segoe UI', 11))

        style.configure("Treeview.Heading",
                        background=self.colors["table_header"][0],
                        foreground="white",
                        font=('Segoe UI', 11, 'bold'),
                        relief="flat",
                        padding=(10, 5))

        style.map("Treeview",
                  background=[("selected", self.colors["selected"][0])],
                  foreground=[("selected", self.colors["selected_text"][0])])

        # Scrollbars
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=self.invoice_list_table.yview)
        hsb = ttk.Scrollbar(table_frame, orient="horizontal", command=self.invoice_list_table.xview)
        self.invoice_list_table.configure(yscroll=vsb.set, xscroll=hsb.set)

        # Layout
        self.invoice_list_table.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        # Alternate row colors
        self.invoice_list_table.tag_configure('oddrow', background=self.colors["row_odd"][0])
        self.invoice_list_table.tag_configure('evenrow', background=self.colors["row_even"][0])
        self.invoice_list_table.tag_configure('hyperlink', foreground="blue", font=('Segoe UI', 11, 'underline'))

        # Bind clicks
        self.invoice_list_table.bind("<Button-1>", self.on_tree_click)

    def on_tree_click(self, event):
        """Detect click on 'View' hyperlink and open popup"""
        item_id = self.invoice_list_table.identify_row(event.y)
        column = self.invoice_list_table.identify_column(event.x)

        if not item_id:
            return

        col_index = int(column.replace("#", "")) - 1
        values = self.invoice_list_table.item(item_id, "values")

        if col_index == 5:  # "Action" column index
            self.show_customer_details(values)

    def show_customer_details(self, customer_data):
        """Open a popup window with full customer details"""
        popup = ctk.CTkToplevel(self)
        popup.title("Customer Details")
        popup.geometry("400x300")

        labels = ["Customer Name", "Mobile", "Address", "Customer GST", "Invoice ID"]
        for i, (label, value) in enumerate(zip(labels, customer_data[:-1])):  # skip "View"
            ctk.CTkLabel(popup, text=f"{label}: {value}", anchor="w").pack(fill="x", padx=20, pady=5)

    def get_table(self):
        return self.invoice_list_table

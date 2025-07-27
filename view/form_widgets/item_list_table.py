import customtkinter as ctk
from tkinter import ttk

def create_item_list(self):

    columns = ["Item Name", "Quantity", "Rate", "Amount"]
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
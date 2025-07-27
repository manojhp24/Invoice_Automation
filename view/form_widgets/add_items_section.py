import customtkinter as ctk

def add_item_section(self):

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
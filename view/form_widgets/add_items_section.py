import customtkinter as ctk

def add_item_section(self):
    """Enhanced item entry section with modern UI and styling"""

    # Header
    item_header_frame = ctk.CTkFrame(self, fg_color="transparent")
    item_header_frame.grid(row=4, column=0, columnspan=4, sticky="ew", padx=25, pady=(25, 15))

    item_header = ctk.CTkLabel(
        item_header_frame,
        text="➕ Add Items",
        font=ctk.CTkFont(size=18, weight="bold"),
        text_color=("#0D47A1", "#00C2CB")
    )
    item_header.grid(row=0, column=0, sticky="w")

    # Accent underline
    ctk.CTkFrame(item_header_frame, height=2, fg_color=("#007bff", "#00C2CB")).grid(
        row=1, column=0, sticky="ew", pady=(6, 0)
    )

    # Main Frame
    items_frame = ctk.CTkFrame(
        self,
        fg_color=("#FAFAFA", "#1A1A1A"),
        corner_radius=16,
        border_width=2,
        border_color=("#E0E0E0", "#333333")
    )
    items_frame.grid(row=5, column=0, columnspan=4, sticky="ew", padx=25, pady=(15, 30))
    items_frame.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform=1)

    entry_fg = ("#FFFFFF", "#0F0F0F")
    entry_border = ("#B0B0B0", "#444444")

    # Item Name
    item_name_label = ctk.CTkLabel(items_frame, text="Item Name *",
                                   font=ctk.CTkFont(size=12, weight="bold"),
                                   text_color=("#212121", "#E8E8E8"))
    item_name_label.grid(row=0, column=0, padx=(20, 10), pady=(20, 8), sticky="w")

    self.item_name = ctk.CTkEntry(
        items_frame,
        placeholder_text="E.g., Web Design",
        font=ctk.CTkFont(size=12),
        height=38,
        corner_radius=10,
        border_width=2,
        border_color=entry_border,
        fg_color=entry_fg
    )
    self.item_name.grid(row=1, column=0, padx=(20, 10), pady=(0, 18), sticky="ew")

    # Quantity
    quantity_label = ctk.CTkLabel(items_frame, text="Quantity *",
                                  font=ctk.CTkFont(size=12, weight="bold"),
                                  text_color=("#212121", "#E8E8E8"))
    quantity_label.grid(row=0, column=1, padx=10, pady=(20, 8), sticky="w")

    self.item_quantity = ctk.CTkEntry(
        items_frame,
        placeholder_text="Qty",
        font=ctk.CTkFont(size=12),
        height=38,
        corner_radius=10,
        border_width=2,
        border_color=entry_border,
        fg_color=entry_fg
    )
    self.item_quantity.grid(row=1, column=1, padx=10, pady=(0, 18), sticky="ew")

    # Rate
    rate_label = ctk.CTkLabel(items_frame, text="Rate *",
                              font=ctk.CTkFont(size=12, weight="bold"),
                              text_color=("#212121", "#E8E8E8"))
    rate_label.grid(row=0, column=2, padx=10, pady=(20, 8), sticky="w")

    self.item_rate = ctk.CTkEntry(
        items_frame,
        placeholder_text="Price",
        font=ctk.CTkFont(size=12),
        height=38,
        corner_radius=10,
        border_width=2,
        border_color=entry_border,
        fg_color=entry_fg
    )
    self.item_rate.grid(row=1, column=2, padx=10, pady=(0, 18), sticky="ew")

    # Action Label
    action_label = ctk.CTkLabel(items_frame, text="Action",
                                font=ctk.CTkFont(size=12, weight="bold"),
                                text_color=("#212121", "#E8E8E8"))
    action_label.grid(row=0, column=3, padx=(10, 20), pady=(20, 8), sticky="w")

    # Add Button
    add_items = ctk.CTkButton(
        items_frame,
        text="+ Add",
        font=ctk.CTkFont(size=12, weight="bold"),
        height=38,
        width=90,
        fg_color=("#2E8B57", "#40E0D0"),
        hover_color=("#228B22", "#20B2AA"),
        corner_radius=10,
        command=self.controller.add_items
    )
    add_items.grid(row=1, column=3, padx=(10, 20), pady=(0, 18), sticky="ew")

    # Highlight on Focus
    for field in [self.item_name, self.item_quantity, self.item_rate]:
        field.bind("<FocusIn>", lambda e, f=field: f.configure(border_color="#00BFFF"))
        field.bind("<FocusOut>", lambda e, f=field: f.configure(border_color=entry_border))

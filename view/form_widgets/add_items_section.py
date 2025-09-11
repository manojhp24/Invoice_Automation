import customtkinter as ctk


def add_item_section(self):
    """Enhanced item entry section with sidebar color scheme"""

    # Color scheme matching the sidebar
    colors = {
        "primary": ("#4C78E8", "#4C78E8"),  # Sidebar active button color
        "secondary": ("#3A3E4B", "#3A3E4B"),  # Sidebar hover color
        "background": ("#2A2D37", "#2A2D37"),  # Sidebar background
        "border": ("#3A3E4B", "#3A3E4B"),  # Sidebar elements border
        "entry_bg": ("#1E2027", "#1E2027"),  # Darker than sidebar background
        "entry_border": ("#3A3E4B", "#3A3E4B"),  # Matching sidebar elements
        "text_primary": ("#E4E4E4", "#E4E4E4"),  # Sidebar text color
        "text_secondary": ("#8A8D93", "#8A8D93"),  # Sidebar secondary text
        "success": ("#4C78E8", "#4C78E8"),  # Using primary color for button
        "success_hover": ("#3A66D0", "#3A66D0"),  # Darker shade of primary
        "focus": ("#00BFFF", "#00BFFF")  # Keeping focus highlight
    }

    # Header
    item_header_frame = ctk.CTkFrame(self, fg_color="transparent")
    item_header_frame.grid(row=4, column=0, columnspan=4, sticky="ew", padx=25, pady=(25, 15))

    item_header = ctk.CTkLabel(
        item_header_frame,
        text="➕ Add Items",
        font=ctk.CTkFont(size=18, weight="bold"),
        text_color=colors["primary"]
    )
    item_header.grid(row=0, column=0, sticky="w")

    # Accent underline
    ctk.CTkFrame(item_header_frame, height=2, fg_color=colors["primary"]).grid(
        row=1, column=0, sticky="ew", pady=(6, 0)
    )

    # Main Frame
    items_frame = ctk.CTkFrame(
        self,
        fg_color=colors["background"],
        corner_radius=12,
        border_width=1,
        border_color=colors["border"]
    )
    items_frame.grid(row=5, column=0, columnspan=4, sticky="ew", padx=25, pady=(15, 30))
    items_frame.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform=1)

    # Create field configuration
    field_config = [
        {"label": "Item Name *", "placeholder": "Product Name", "var_name": "item_name", "col": 0},
        {"label": "Quantity *", "placeholder": "Qty", "var_name": "item_quantity", "col": 1},
        {"label": "Rate *", "placeholder": "Price", "var_name": "item_rate", "col": 2}
    ]

    # Create entry fields
    for config in field_config:
        # Label
        label = ctk.CTkLabel(
            items_frame,
            text=config["label"],
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=colors["text_primary"]
        )
        label.grid(
            row=0,
            column=config["col"],
            padx=(20 if config["col"] == 0 else 10, 10 if config["col"] == 2 else 20),
            pady=(20, 8),
            sticky="w"
        )

        # Entry field
        entry = ctk.CTkEntry(
            items_frame,
            placeholder_text=config["placeholder"],
            font=ctk.CTkFont(size=12),
            height=38,
            corner_radius=8,
            border_width=1,
            border_color=colors["entry_border"],
            fg_color=colors["entry_bg"],
            text_color=colors["text_primary"]
        )
        entry.grid(
            row=1,
            column=config["col"],
            padx=(20 if config["col"] == 0 else 10, 10 if config["col"] == 2 else 20),
            pady=(0, 18),
            sticky="ew"
        )

        # Set as instance variable
        setattr(self, config["var_name"], entry)

        # Highlight on Focus
        entry.bind("<FocusIn>", lambda e, f=entry: f.configure(border_color=colors["focus"]))
        entry.bind("<FocusOut>", lambda e, f=entry: f.configure(border_color=colors["entry_border"]))

    # Action Label
    action_label = ctk.CTkLabel(
        items_frame,
        text="Action",
        font=ctk.CTkFont(size=12, weight="bold"),
        text_color=colors["text_primary"]
    )
    action_label.grid(row=0, column=3, padx=(10, 20), pady=(20, 8), sticky="w")

    # Add Button
    add_items = ctk.CTkButton(
        items_frame,
        text="+ Add",
        font=ctk.CTkFont(size=12, weight="bold"),
        height=38,
        width=90,
        fg_color=colors["success"],
        hover_color=colors["success_hover"],
        corner_radius=8,
        text_color=colors["text_primary"],
        command=self.controller.add_items
    )
    add_items.grid(row=1, column=3, padx=(10, 20), pady=(0, 18), sticky="ew")
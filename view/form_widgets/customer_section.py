import customtkinter as ctk


def create_customer_section(self):
    """Enhanced customer section with sidebar color scheme"""

    # Color scheme matching the sidebar
    colors = {
        "primary": ("#4C78E8", "#4C78E8"),
        "secondary": ("#3A3E4B", "#3A3E4B"),
        "background": ("#2A2D37", "#2A2D37"),
        "border": ("#3A3E4B", "#3A3E4B"),
        "entry_bg": ("#1E2027", "#1E2027"),
        "entry_border": ("#3A3E4B", "#3A3E4B"),
        "text_primary": ("#E4E4E4", "#E4E4E4"),
        "text_secondary": ("#8A8D93", "#8A8D93"),
        "focus": ("#00BFFF", "#00BFFF")
    }

    # Header Frame
    customer_header_frame = ctk.CTkFrame(self, fg_color="transparent")
    customer_header_frame.grid(row=1, column=0, columnspan=4, sticky="ew", padx=25, pady=(25, 15))
    customer_header_frame.grid_columnconfigure(0, weight=1)

    # Header Text
    customer_header = ctk.CTkLabel(
        customer_header_frame,
        text="👤 Customer Information",
        font=ctk.CTkFont(size=20, weight="bold"),
        text_color=colors["primary"]
    )
    customer_header.grid(row=0, column=0, sticky="w")

    # Accent underline
    ctk.CTkFrame(customer_header_frame, height=2, fg_color=colors["primary"]).grid(
        row=1, column=0, sticky="ew", pady=(6, 0)
    )

    # Main Form Frame
    customer_frame = ctk.CTkFrame(
        self,
        fg_color=colors["background"],
        corner_radius=12,
        border_width=1,
        border_color=colors["border"]
    )
    customer_frame.grid(row=2, column=0, columnspan=4, sticky="ew", padx=25, pady=(15, 30))
    customer_frame.grid_columnconfigure((0, 2), weight=1, uniform=1)

    # Field configuration
    field_config = [
        # Row 1
        {"label": "Customer Name *", "placeholder": "Enter Customer Name", "var_name": "customer_name", "row": 0,
         "col": 0},
        {"label": "Address *", "placeholder": "Enter Address", "var_name": "address", "row": 0, "col": 2},
        # Row 2
        {"label": "Mobile Number *", "placeholder": "Enter Contact Number", "var_name": "customer_mobile", "row": 2,
         "col": 0},
        {"label": "Email Address", "placeholder": "Enter Email (Optional)", "var_name": "customer_email", "row": 2,
         "col": 2},
        # Row 3
        {"label": "GST", "placeholder": "Enter GST", "var_name": "gst_entry", "row": 4, "col": 0}
    ]

    # Create all fields
    for config in field_config:
        # Label
        label = ctk.CTkLabel(
            customer_frame,
            text=config["label"],
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=colors["text_primary"]
        )
        label.grid(
            row=config["row"],
            column=config["col"],
            padx=20,
            pady=(20 if config["row"] == 0 else 5, 8),
            sticky="w"
        )

        # Entry field
        entry = ctk.CTkEntry(
            customer_frame,
            placeholder_text=config["placeholder"],
            font=ctk.CTkFont(size=12),
            height=38,
            corner_radius=8,
            border_width=1,
            border_color=colors["entry_border"],
            fg_color=colors["entry_bg"],
            text_color=colors["text_primary"]
        )

        # Set padding and row position
        pady_bottom = 18 if config["row"] != 4 else 25
        entry_row = config["row"] + 1

        entry.grid(
            row=entry_row,
            column=config["col"],
            padx=20,
            pady=(0, pady_bottom),
            sticky="ew"
        )

        # Set as instance variable
        setattr(self, config["var_name"], entry)

        # Highlight on Focus
        entry.bind("<FocusIn>", lambda e, f=entry: f.configure(border_color=colors["focus"]))
        entry.bind("<FocusOut>", lambda e, f=entry: f.configure(border_color=colors["entry_border"]))

    # Focus highlight for all fields
    fields = [self.customer_name, self.address, self.customer_mobile, self.customer_email, self.gst_entry]
    for field in fields:
        field.bind("<FocusIn>", lambda e, f=field: f.configure(border_color=colors["focus"]))
        field.bind("<FocusOut>", lambda e, f=field: f.configure(border_color=colors["entry_border"]))
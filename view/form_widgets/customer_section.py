import customtkinter as ctk

def create_customer_section(self):
    """Enhanced customer section with modern UI and layout"""

    # Header Frame
    customer_header_frame = ctk.CTkFrame(self, fg_color="transparent")
    customer_header_frame.grid(row=1, column=0, columnspan=4, sticky="ew", padx=25, pady=(25, 15))
    customer_header_frame.grid_columnconfigure(0, weight=1)

    # Header Text
    customer_header = ctk.CTkLabel(
        customer_header_frame,
        text="👤 Customer Information",
        font=ctk.CTkFont(size=20, weight="bold"),
        text_color=("#0D47A1", "#00C2CB")
    )
    customer_header.grid(row=0, column=0, sticky="w")

    # Accent underline
    ctk.CTkFrame(customer_header_frame, height=2, fg_color=("#007bff", "#00C2CB")).grid(
        row=1, column=0, sticky="ew", pady=(6, 0)
    )

    # Main Form Frame
    customer_frame = ctk.CTkFrame(
        self,
        fg_color=("#FAFAFA", "#1A1A1A"),
        corner_radius=16,
        border_width=2,
        border_color=("#E0E0E0", "#333333")
    )
    customer_frame.grid(row=2, column=0, columnspan=4, sticky="ew", padx=25, pady=(15, 30))
    customer_frame.grid_columnconfigure((0, 2), weight=1, uniform=1)

    entry_fg = ("#FFFFFF", "#0F0F0F")
    entry_border = ("#B0B0B0", "#444444")

    # --- Row 1 ---
    name_label = ctk.CTkLabel(customer_frame, text="Customer Name *",
                              font=ctk.CTkFont(size=13, weight="bold"),
                              text_color=("#212121", "#E8E8E8"))
    name_label.grid(row=0, column=0, padx=20, pady=(20, 8), sticky="w")

    self.customer_name = ctk.CTkEntry(customer_frame,
                                      placeholder_text="Enter Customer Name",
                                      font=ctk.CTkFont(size=12),
                                      height=38,
                                      corner_radius=10,
                                      border_width=2,
                                      border_color=entry_border,
                                      fg_color=entry_fg)
    self.customer_name.grid(row=1, column=0, padx=20, pady=(0, 18), sticky="ew")

    address_label = ctk.CTkLabel(customer_frame, text="Address *",
                                 font=ctk.CTkFont(size=13, weight="bold"),
                                 text_color=("#212121", "#E8E8E8"))
    address_label.grid(row=0, column=2, padx=20, pady=(20, 8), sticky="w")

    self.address = ctk.CTkEntry(customer_frame,
                                placeholder_text="Enter Address",
                                font=ctk.CTkFont(size=12),
                                height=38,
                                corner_radius=10,
                                border_width=2,
                                border_color=entry_border,
                                fg_color=entry_fg)
    self.address.grid(row=1, column=2, padx=20, pady=(0, 18), sticky="ew")

    # --- Row 2 ---
    mobile_label = ctk.CTkLabel(customer_frame, text="Mobile Number *",
                                font=ctk.CTkFont(size=13, weight="bold"),
                                text_color=("#212121", "#E8E8E8"))
    mobile_label.grid(row=2, column=0, padx=20, pady=(5, 8), sticky="w")

    self.customer_mobile = ctk.CTkEntry(customer_frame,
                                        placeholder_text="Enter Contact Number",
                                        font=ctk.CTkFont(size=12),
                                        height=38,
                                        corner_radius=10,
                                        border_width=2,
                                        border_color=entry_border,
                                        fg_color=entry_fg)
    self.customer_mobile.grid(row=3, column=0, padx=20, pady=(0, 18), sticky="ew")

    email_label = ctk.CTkLabel(customer_frame, text="Email Address",
                               font=ctk.CTkFont(size=13, weight="bold"),
                               text_color=("#212121", "#E8E8E8"))
    email_label.grid(row=2, column=2, padx=20, pady=(5, 8), sticky="w")

    self.customer_email = ctk.CTkEntry(customer_frame,
                                       placeholder_text="Enter Email (Optional)",
                                       font=ctk.CTkFont(size=12),
                                       height=38,
                                       corner_radius=10,
                                       border_width=2,
                                       border_color=entry_border,
                                       fg_color=entry_fg)
    self.customer_email.grid(row=3, column=2, padx=20, pady=(0, 18), sticky="ew")

    # --- Row 3 ---
    gst_label = ctk.CTkLabel(customer_frame, text="GST",
                             font=ctk.CTkFont(size=13, weight="bold"),
                             text_color=("#212121", "#E8E8E8"))
    gst_label.grid(row=4, column=0, padx=20, pady=(5, 8), sticky="w")

    self.gst_entry = ctk.CTkEntry(customer_frame,
                                  placeholder_text="Enter GST",
                                  font=ctk.CTkFont(size=12),
                                  height=38,
                                  corner_radius=10,
                                  border_width=2,
                                  border_color=entry_border,
                                  fg_color=entry_fg)
    self.gst_entry.grid(row=5, column=0, padx=20, pady=(0, 25), sticky="ew")

    # Focus highlight
    for field in [self.customer_name, self.address, self.customer_mobile, self.customer_email, self.gst_entry]:
        field.bind("<FocusIn>", lambda e, f=field: f.configure(border_color="#00BFFF"))
        field.bind("<FocusOut>", lambda e, f=field: f.configure(border_color=entry_border))

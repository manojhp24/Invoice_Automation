import customtkinter as ctk

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
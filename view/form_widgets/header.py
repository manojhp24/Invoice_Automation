import customtkinter as ctk


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

import customtkinter as ctk


def create_header(self):
    """Create enhanced header section with sidebar color scheme"""

    # Color scheme matching the sidebar
    colors = {
        "primary": ("#4C78E8", "#4C78E8"),  # Sidebar active button color
        "secondary": ("#3A3E4B", "#3A3E4B"),  # Sidebar hover color
        "background": ("#2A2D37", "#2A2D37"),  # Sidebar background
        "text_primary": ("#E4E4E4", "#E4E4E4"),  # Sidebar text color
        "text_secondary": ("#8A8D93", "#8A8D93"),  # Sidebar secondary text
        "separator": ("#3A3E4B", "#3A3E4B")  # Separator color
    }

    header_frame = ctk.CTkFrame(
        self,
        fg_color="transparent",
        corner_radius=0
    )
    header_frame.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0, 20))
    header_frame.grid_columnconfigure(0, weight=1)

    # Main title
    title_label = ctk.CTkLabel(
        header_frame,
        text="📄 Create New Invoice",
        font=ctk.CTkFont(size=28, weight="bold"),
        text_color=colors["primary"]
    )
    title_label.grid(row=0, column=0, pady=(15, 5))

    # Subtitle for better context
    subtitle_label = ctk.CTkLabel(
        header_frame,
        text="Fill in the details below to generate your professional invoice",
        font=ctk.CTkFont(size=12),
        text_color=colors["text_secondary"]
    )
    subtitle_label.grid(row=1, column=0, pady=(0, 10))

    # Enhanced separator
    separator_frame = ctk.CTkFrame(header_frame, height=2, fg_color="transparent")
    separator_frame.grid(row=2, column=0, sticky="ew", pady=(5, 0))
    separator_frame.grid_columnconfigure(0, weight=1)

    # Main separator line
    separator = ctk.CTkFrame(separator_frame, height=2, fg_color=colors["primary"])
    separator.grid(row=0, column=0, sticky="ew")

    # Subtle secondary line
    separator2 = ctk.CTkFrame(separator_frame, height=1, fg_color=colors["separator"])
    separator2.grid(row=1, column=0, sticky="ew", pady=(1, 0))
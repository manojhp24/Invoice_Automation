import customtkinter as ctk

def create_actions_button(self,controller):

    actions_container = ctk.CTkFrame(self, fg_color="transparent")
    actions_container.grid(row=13, column=0, columnspan=4, pady=(30, 40))

    # Section header
    actions_header = ctk.CTkLabel(
        actions_container,
        text="🚀 Actions",
        font=ctk.CTkFont(size=16, weight="bold"),
        text_color=("#2E8B57", "#40E0D0")
    )
    actions_header.grid(row=0, column=0, columnspan=4, pady=(0, 20))

    # Button container with proper grid layout
    button_frame = ctk.CTkFrame(
        actions_container,
        fg_color=("white", "gray15"),
        corner_radius=12,
        border_width=1,
        border_color=("gray85", "gray25")
    )
    button_frame.grid(row=1, column=0, columnspan=4, padx=20, pady=10, sticky="ew")

    # Configure columns for even spacing
    button_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

    # Save Draft button
    save_draft_btn = ctk.CTkButton(
        button_frame,
        text="💾 Save Draft",
        width=160,
        height=42,
        font=ctk.CTkFont(size=12, weight="bold"),
        fg_color=("#6c757d", "#495057"),
        hover_color=("#5a6268", "#3d4043"),
        corner_radius=8,
        text_color="white"
    )
    save_draft_btn.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

    # Preview Button
    preview_button = ctk.CTkButton(
        button_frame,
        text="👁️ Preview Invoice",
        width=160,
        height=42,
        font=ctk.CTkFont(size=12, weight="bold"),
        fg_color=("#007bff", "#0056b3"),
        hover_color=("#0056b3", "#004085"),
        corner_radius=8,
        text_color="white"
    )
    preview_button.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

    # Clear Form button
    clear_button = ctk.CTkButton(
        button_frame,
        text="🗑️ Clear Form",
        width=160,
        height=42,
        font=ctk.CTkFont(size=12, weight="bold"),
        fg_color=("#dc3545", "#c82333"),
        hover_color=("#c82333", "#bd2130"),
        corner_radius=8,
        text_color="white",
        command=self.controller.clear_form
    )
    clear_button.grid(row=0, column=2, padx=20, pady=20, sticky="ew")

    # Generate Invoice Button (Main CTA)
    create_invoice_button = ctk.CTkButton(
        button_frame,
        text="✨ Generate Invoice",
        width=160,
        height=42,
        font=ctk.CTkFont(size=12, weight="bold"),
        fg_color=("#28a745", "#1e7e34"),
        hover_color=("#218838", "#1c7430"),
        corner_radius=8,
        text_color="white",
        command=self.controller.create_invoice,
    )
    create_invoice_button.grid(row=0, column=3, padx=20, pady=20, sticky="ew")

    # Configure the main actions container to expand properly
    actions_container.grid_columnconfigure(0, weight=1)

    # Add hover effects
    def on_hover_enter(button):
        def handler(event):
            button.configure(cursor="hand2")

        return handler

    def on_hover_leave(button):
        def handler(event):
            button.configure(cursor="")

        return handler

    # Apply hover effects to all buttons
    buttons = [save_draft_btn, preview_button, clear_button, create_invoice_button]
    for btn in buttons:
        btn.bind("<Enter>", on_hover_enter(btn))
        btn.bind("<Leave>", on_hover_leave(btn))
import customtkinter as ctk


def create_actions_button(self, controller):
    # Prevent multiple renders
    if hasattr(self, "actions_created") and self.actions_created:
        return

    self.actions_created = True
    self.controller = controller

    # Color scheme matching the sidebar
    colors = {
        "primary": ("#4C78E8", "#4C78E8"),
        "secondary": ("#3A3E4B", "#3A3E4B"),
        "background": ("#2A2D37", "#2A2D37"),
        "border": ("#3A3E4B", "#3A3E4B"),
        "text_primary": ("#E4E4E4", "#E4E4E4"),
        "success": ("#4C78E8", "#4C78E8"),
        "success_hover": ("#3A66D0", "#3A66D0"),
        "danger": ("#E84C4C", "#E84C4C"),
        "danger_hover": ("#D03A3A", "#D03A3A"),
        "info": ("#6C757D", "#6C757D"),
        "info_hover": ("#5A6268", "#5A6268"),
        "warning": ("#FFC107", "#FFC107"),
        "warning_hover": ("#E0A800", "#E0A800")
    }

    # Main container
    actions_container = ctk.CTkFrame(self, fg_color="transparent")
    actions_container.grid(row=13, column=0, columnspan=4, pady=(30, 40), sticky="nsew")

    # Configure grid weights for proper expansion
    self.grid_rowconfigure(13, weight=0)
    for i in range(4):
        self.grid_columnconfigure(i, weight=1)

    actions_header = ctk.CTkLabel(
        actions_container,
        text="🚀 Actions",
        font=ctk.CTkFont(size=16, weight="bold"),
        text_color=colors["primary"]
    )
    actions_header.pack(pady=(0, 15))

    # Button container with fixed width
    button_frame = ctk.CTkFrame(
        actions_container,
        fg_color=colors["background"],
        corner_radius=12,
        border_width=1,
        border_color=colors["border"],
        height=100
    )
    button_frame.pack(fill="x", padx=20, pady=10)
    button_frame.pack_propagate(False)  # Prevent frame from resizing to content

    # Use a grid inside the button frame
    button_frame.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="equal")
    button_frame.grid_rowconfigure(0, weight=1)

    # Button configuration
    button_config = [
        {
            "text": "💾 Save Draft",
            "column": 0,
            "fg_color": colors["info"],
            "hover_color": colors["info_hover"],
            "command": None
        },
        {
            "text": "👁️ Preview Invoice",
            "column": 1,
            "fg_color": colors["warning"],
            "hover_color": colors["warning_hover"],
            "command": self.controller.preview_invoice,
            "text_color": ("#000000", "#000000")
        },
        {
            "text": "🗑️ Clear Form",
            "column": 2,
            "fg_color": colors["danger"],
            "hover_color": colors["danger_hover"],
            "command": self.controller.clear_form
        },
        {
            "text": "✨ Generate Invoice",
            "column": 3,
            "fg_color": colors["success"],
            "hover_color": colors["success_hover"],
            "command": self.controller.create_invoice
        }
    ]

    # Create buttons with proper padding
    buttons = []
    for config in button_config:
        btn = ctk.CTkButton(
            button_frame,
            text=config["text"],
            height=42,
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color=config["fg_color"],
            hover_color=config["hover_color"],
            corner_radius=8,
            text_color=config.get("text_color", "white"),
            command=config["command"]
        )
        btn.grid(
            row=0,
            column=config["column"],
            padx=(10 if config["column"] == 0 else 5, 10 if config["column"] == 3 else 5),
            pady=20,
            sticky="nsew"
        )
        buttons.append(btn)

    # Hover effects
    def on_hover_enter(event):
        event.widget.configure(cursor="hand2")

    def on_hover_leave(event):
        event.widget.configure(cursor="")

    for btn in buttons:
        btn.bind("<Enter>", on_hover_enter)
        btn.bind("<Leave>", on_hover_leave)
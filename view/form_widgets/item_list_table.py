import customtkinter as ctk
from tkinter import ttk

def create_item_list(self):
    # Color scheme matching the sidebar
    colors = {
        "primary": ("#4C78E8", "#4C78E8"),           # Sidebar active button color
        "secondary": ("#3A3E4B", "#3A3E4B"),         # Sidebar hover color
        "background": ("#2A2D37", "#2A2D37"),        # Sidebar background
        "border": ("#3A3E4B", "#3A3E4B"),            # Sidebar elements border
        "text_primary": ("#E4E4E4", "#E4E4E4"),      # Sidebar text color
        "text_secondary": ("#8A8D93", "#8A8D93"),    # Sidebar secondary text
        "table_header": ("#4C78E8", "#4C78E8"),      # Table header matching primary
        "table_bg": ("#2A2D37", "#2A2D37"),          # Table background
        "table_fg": ("#E4E4E4", "#E4E4E4"),          # Table text color
        "row_odd": ("#2A2D37", "#2A2D37"),           # Odd row background
        "row_even": ("#3A3E4B", "#3A3E4B"),          # Even row background
        "selected": ("#4C78E8", "#4C78E8"),          # Selected row color
        "selected_text": ("#FFFFFF", "#FFFFFF")      # Selected text color
    }

    columns = ["Item Name", "Quantity", "Rate", "Amount"]
    list_header_frame = ctk.CTkFrame(self, fg_color="transparent")
    list_header_frame.grid(row=7, column=0, columnspan=4, sticky="ew", padx=20, pady=(20, 10))

    item_header = ctk.CTkLabel(
        list_header_frame,
        text="📦 Items List",
        font=ctk.CTkFont(size=18, weight="bold"),
        text_color=colors["primary"]
    )
    item_header.grid(row=0, column=0, sticky="w")

    list_subtitle = ctk.CTkLabel(
        list_header_frame,
        text="Review your invoice items",
        font=ctk.CTkFont(size=11),
        text_color=colors["text_secondary"]
    )
    list_subtitle.grid(row=1, column=0, sticky="w", pady=(2, 0))

    table_container = ctk.CTkFrame(
        self,
        fg_color=colors["background"],
        corner_radius=12,
        border_width=1,
        border_color=colors["border"]
    )
    table_container.grid(row=8, column=0, columnspan=4, sticky="nsew", padx=20, pady=(10, 20))
    table_container.grid_rowconfigure(0, weight=1)
    table_container.grid_columnconfigure(0, weight=1)

    # Enhanced treeview
    self.item_tree = ttk.Treeview(
        table_container,
        columns=columns,
        show="headings",
        height=8
    )
    self.item_tree.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    # Column headers
    self.item_tree.heading("Item Name", text="📋 Item Name", anchor="w")
    self.item_tree.heading("Quantity", text="📊 Qty", anchor="center")
    self.item_tree.heading("Rate", text="💰 Rate", anchor="center")
    self.item_tree.heading("Amount", text="💵 Amount", anchor="center")

    # Column widths
    self.item_tree.column("Item Name", width=280, anchor="w", minwidth=180)
    self.item_tree.column("Quantity", width=100, anchor="center")
    self.item_tree.column("Rate", width=120, anchor="center")
    self.item_tree.column("Amount", width=120, anchor="center")

    # Style setup
    style = ttk.Style()
    style.theme_use("clam")   # ensures header bg works

    style.configure("Treeview",
                    background=colors["table_bg"][0],
                    foreground=colors["table_fg"][0],
                    rowheight=34,
                    fieldbackground=colors["table_bg"][0],
                    borderwidth=0,
                    font=('Segoe UI', 11))

    style.configure("Treeview.Heading",
                    background=colors["table_header"][0],
                    foreground="white",
                    font=('Segoe UI', 11, 'bold'),
                    relief="flat")

    style.map("Treeview",
              background=[("selected", colors["selected"][0])],
              foreground=[("selected", colors["selected_text"][0])])

    # Scrollbar
    scrollbar = ttk.Scrollbar(
        table_container,
        orient="vertical",
        command=self.item_tree.yview
    )
    self.item_tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns", pady=10)

    # Alternate row colors
    self.item_tree.tag_configure('oddrow', background=colors["row_odd"][0])
    self.item_tree.tag_configure('evenrow', background=colors["row_even"][0])

    # Empty state message
    if not hasattr(self, '_empty_message_added'):
        empty_item = self.item_tree.insert(
            '',
            'end',
            values=('📝 No items added yet - Click "Add" to start', '', '', ''),
            tags=('empty',)
        )
        self.item_tree.tag_configure(
            'empty',
            background=colors["row_odd"][0],
            foreground=colors["text_secondary"][0],
            font=('Segoe UI', 10, 'italic')
        )
        self._empty_message_added = True
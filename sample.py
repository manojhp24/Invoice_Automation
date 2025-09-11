import customtkinter as ctk
from PIL import Image


class DashboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.view_cache = {}

        # Configure layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Sidebar Frame
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color="#1E1E2E")
        self.sidebar.grid(row=0, column=0, sticky="ns")

        # App Title / Logo
        ctk.CTkLabel(
            self.sidebar,
            text="📑 InvoiceApp",
            font=("Arial", 20, "bold"),
            text_color="white"
        ).pack(pady=(20, 10))

        # Divider Line
        ctk.CTkFrame(self.sidebar, height=2, fg_color="#3E3E4E").pack(fill="x", padx=15, pady=(0, 15))

        # Sidebar buttons
        self.nav_buttons = {}
        nav_items = {
            "Create Invoice": InvoiceForm,
            "Invoice List": InvoiceList
        }

        for name, ViewClass in nav_items.items():
            btn = ctk.CTkButton(
                self.sidebar,
                text=f"  {name}",
                command=lambda c=ViewClass, n=name: self.navigate(n, c),
                fg_color="transparent",
                hover_color="#2E2E3E",
                anchor="w",
                corner_radius=8,
                height=40,
                width=200,
                font=("Arial", 14),
                text_color="white"
            )
            btn.pack(pady=5, padx=10, fill="x")
            self.nav_buttons[name] = btn

        # Main content area
        self.scrollable_main = ctk.CTkScrollableFrame(self, corner_radius=10, fg_color="#f4f6f9")
        self.scrollable_main.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.scrollable_main.bind_all("<MouseWheel>", self._on_mousewheel)

        self.navigate("Create Invoice", InvoiceForm)

    def navigate(self, name, ViewClass):
        for btn in self.nav_buttons.values():
            btn.configure(fg_color="transparent")
        self.nav_buttons[name].configure(fg_color="#3E3E4E")

        self.clear_main_content()

        if name in self.view_cache:
            view = self.view_cache[name]
        else:
            view = ViewClass(self.scrollable_main)
            self.view_cache[name] = view

        view.pack(fill="both", expand=True)

    def _on_mousewheel(self, event):
        self.scrollable_main._parent_canvas.yview_scroll(-int(event.delta / 1.3), "units")

    def clear_main_content(self):
        for view in self.view_cache.values():
            view.pack_forget()

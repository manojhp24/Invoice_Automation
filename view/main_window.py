import customtkinter as ctk
from view.invoice_form import InvoiceForm
from view.invoice_list import InvoiceList

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.view_cache = {}

        # Configure layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="ns")
        ctk.CTkLabel(self.sidebar, text="Dashboard", font=("Arial", 18, "bold")).pack(pady=20)

        # Sidebar buttons
        self.nav_buttons = {}
        nav_items = {
            "Create Invoice": InvoiceForm,
            "Invoice List": InvoiceList
        }

        for name, ViewClass in nav_items.items():
            btn = ctk.CTkButton(
                self.sidebar,
                text=name,
                command=lambda c=ViewClass, n=name: self.navigate(n, c),
                fg_color="transparent",
                hover_color="#2E2E3E",
                anchor="w",
                width=180
            )
            btn.pack(pady=5, padx=10)
            self.nav_buttons[name] = btn

        # Main content area
        self.scrollable_main = ctk.CTkScrollableFrame(self, corner_radius=10)
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

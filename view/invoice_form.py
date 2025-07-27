import customtkinter as ctk

from controller.Invoice_controller import ItemController
from view.form_widgets.actions_button import create_actions_button
from view.form_widgets.item_list_table import create_item_list
from view.form_widgets.add_items_section import add_item_section
from view.form_widgets.customer_section import create_customer_section
from view.form_widgets.header import create_header


class InvoiceForm(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Configure grid weights for responsive layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.controller = ItemController(self)
        self.setup_ui()

    def setup_ui(self):
        create_header(self)
        create_customer_section(self)
        add_item_section(self)
        create_item_list(self)
        create_actions_button(self, self.controller)
        # ✅ Progress label
        self.progress_label = ctk.CTkLabel(
            self,
            text="Generating invoice...",
            font=ctk.CTkFont(size=13),
            text_color="green"
        )
        self.progress_label.grid(row=10, column=0, columnspan=4, pady=(10, 0))
        self.progress_label.grid_remove()  # Initially hidden

        # ✅ Progress bar
        self.popup_progress_bar = ctk.CTkProgressBar(self, width=400)
        self.popup_progress_bar.grid(row=11, column=0, columnspan=4, pady=(5, 10))
        self.popup_progress_bar.set(0)
        self.popup_progress_bar.grid_remove()


    def show_progress_bar(self):
        self.progress_label.grid()
        self.popup_progress_bar.set(0)
        self.popup_progress_bar.grid()

    def hide_progress_bar(self):
        self.progress_label.grid_remove()
        self.popup_progress_bar.grid_remove()




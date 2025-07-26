from tkinter import ttk

def create_styled_combobox(parent, values):
    style = ttk.Style()
    style.theme_use("default")

    style.configure("Custom.TCombobox",
        fieldbackground="#2b2b2b",  # dark mode input bg
        background="#1f6aa5",       # dropdown bg
        foreground="white",
        bordercolor="#1f6aa5",
        selectbackground="#1f6aa5",
        selectforeground="white",
        relief="flat",
        padding=5
    )

    combo = ttk.Combobox(parent, values=values, style="Custom.TCombobox", width=40)
    combo.set("Select Item")
    return combo

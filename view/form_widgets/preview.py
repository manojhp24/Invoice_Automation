import customtkinter as ctk

def preview_invoice(self):
    """Show invoice preview in a popup window"""

    # Create popup window
    preview_win = ctk.CTkToplevel(self)
    preview_win.title("Invoice Preview")
    preview_win.geometry("600x500")
    preview_win.grab_set()   # Make modal (focus stays until closed)

    # Header
    header = ctk.CTkLabel(
        preview_win,
        text="📄 Invoice Preview",
        font=ctk.CTkFont(size=18, weight="bold"),
        text_color=("#0D47A1", "#00C2CB")
    )
    header.pack(pady=(20, 10))

    ctk.CTkFrame(preview_win, height=2, fg_color=("#007bff", "#00C2CB")).pack(fill="x", padx=20, pady=(0, 20))

    # Content area
    content_frame = ctk.CTkScrollableFrame(preview_win, width=550, height=350)
    content_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Example: show customer info + items (replace with your real values)
    ctk.CTkLabel(content_frame, text=f"Customer: {self.customer_name.get()}", font=ctk.CTkFont(size=14)).pack(anchor="w", pady=5)
    ctk.CTkLabel(content_frame, text=f"Address: {self.address.get()}", font=ctk.CTkFont(size=14)).pack(anchor="w", pady=5)
    ctk.CTkLabel(content_frame, text=f"Mobile: {self.customer_mobile.get()}", font=ctk.CTkFont(size=14)).pack(anchor="w", pady=5)

    ctk.CTkLabel(content_frame, text="Items:", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", pady=(10, 5))
    ctk.CTkLabel(content_frame, text=f"{self.item_name.get()} | Qty: {self.item_quantity.get()} | Rate: {self.item_rate.get()}",
                 font=ctk.CTkFont(size=13)).pack(anchor="w", pady=2)

    # Close Button
    close_btn = ctk.CTkButton(
        preview_win,
        text="Close Preview",
        fg_color=("#6c757d", "#495057"),
        hover_color=("#5a6268", "#3d4043"),
        corner_radius=8,
        command=preview_win.destroy
    )
    close_btn.pack(pady=20)

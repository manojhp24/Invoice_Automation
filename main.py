import customtkinter as ctk
from view.main_window import MainWindow
from app_config import APP_NAME, WINDOW_WIDTH, WINDOW_HEIGHT
from db_connection.init_db import initialize_db


def main():
    initialize_db()

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = MainWindow()
    app.title(APP_NAME)
    app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    app.mainloop()


if __name__ == "__main__":
    main()

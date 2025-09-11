import sqlite3
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource (works for dev and PyInstaller exe) """
    if hasattr(sys, "_MEIPASS"):  # Running from the PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_connection():
    db_path = resource_path(os.path.join("data", "invoices.db"))
    os.makedirs(os.path.dirname(db_path), exist_ok=True)  # ensure folder exists
    return sqlite3.connect(db_path)

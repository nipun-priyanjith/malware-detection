import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from MalwareDetector import MalwareDetector
from lists import Lists
from prosess import Process
import result

class Settings:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Antivirus Settings")
        self.root.geometry("800x600")
        self.root.configure(bg="#F0F0F0")

        # Header Label
        self.header_label = tk.Label(self.root, text="Antivirus Settings", font=("Arial", 30, "bold"), fg="black", bg="#F0F0F0")
        self.header_label.place(relx=0.5, rely=0.1, anchor="center")

        # Style
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 14), background='#4CAF50', foreground='white')

        # Add More Signatures Button
        self.add_signatures_button = ttk.Button(self.root, text="Add More Signatures")
        self.add_signatures_button.place(relx=0.5, rely=0.3, anchor="center")

        # Contact Developers Button
        self.contact_developers_button = ttk.Button(self.root, text="Contact Developers")
        self.contact_developers_button.place(relx=0.5, rely=0.4, anchor="center")

        # Firewall & Network Protection Button
        self.firewall_button = ttk.Button(self.root, text="Firewall & Network Protection")
        self.firewall_button.place(relx=0.5, rely=0.5, anchor="center")

        # Device Security Button
        self.device_security_button = ttk.Button(self.root, text="Device Security")
        self.device_security_button.place(relx=0.5, rely=0.6, anchor="center")

        # Exit Button
        self.exit_button = ttk.Button(self.root, text="Exit")
        self.exit_button.place(relx=0.5, rely=0.9, anchor="center")

if __name__ == "__main__":
    frontend = Settings()
    frontend.root.mainloop()

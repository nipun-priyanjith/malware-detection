import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from MalwareDetector import MalwareDetector
from lists import Lists
from prosess import Process
import result

class FullScan:
     def __init__(self):
        self.root = tk.Tk()
        self.root.title("Malware Detection")
        self.root.geometry("1300x700")
        self.root.configure(bg="#F0F0F0")
        
        # Header Label
        self.header_label = tk.Label(self.root, text="Malware Detection Applycation", font=("Arial", 40, "bold"), fg="#fa0505", bg="#F0F0F0")
        self.header_label.place(relx=0.5, rely=0.1, anchor="center")
        
        # Left Label
        self.left_label = tk.Label(self.root, text="Select if you need to search full pc:", font=("Arial", 18),fg= "#2196F3", bg="#F0F0F0")
        self.left_label.place(relx=0.05, rely=0.2)
        
        # Enter Location Button
        self.enter_location_button = tk.Button(self.root, text="Full PC Scan", font=("Arial", 14),   bg="#2196F3", fg="#FFFFFF")
        self.enter_location_button.place(relx=0.37, rely=0.2)
        
        # Search Result Frame
        self.result_frame = tk.Frame(self.root, width=1200, height=400, bg="#FFFFFF")
        self.result_frame.place(relx=0.5, rely=0.6, anchor="center")
        
# Delete Malware Button
        self.delete_malware_button = tk.Button(self.root, text="Delete Malware", font=("Arial", 12), fg="#ffffff", bg="#ff5252", activebackground="#ff5252", activeforeground="#ffffff", padx=10, pady=5, borderwidth=0)
        self.delete_malware_button.place(relx=0.4, rely=0.9, anchor="center")

# More Info Malware Button
        self.more_info_button = tk.Button(self.root, text="More Info", font=("Arial", 12), fg="#ffffff", bg="#2196F3", activebackground="#388E3C", activeforeground="#ffffff", padx=10, pady=5, borderwidth=0)
        self.more_info_button.place(relx=0.5, rely=0.9, anchor="center")

# Clear All Data Button
        self.clear_button = tk.Button(self.root, text="Clear All Data", font=("Arial", 12), fg="#ffffff", bg="#2196F3", activebackground="#1976D2", activeforeground="#ffffff", padx=10, pady=5, borderwidth=0)
        self.clear_button.place(relx=0.6, rely=0.9, anchor="center")

        # Attach the frame to the bottom of the main frame
        self.result_frame.pack_propagate(False)

if __name__ == "__main__":
    frontend = FullScan()
    frontend.run()

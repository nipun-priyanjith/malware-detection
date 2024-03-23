import tkinter as tk
from PIL import Image, ImageTk

from antivirasFrontend import AntivirusFrontend
from fullScann import FullScan
from settings import Settings
from updates import Updates

def full_scan():
    fullscan=FullScan()
    fullscan.run()
    

def location_scan():
    frontend = AntivirusFrontend()
    frontend.run()

def updates():
    up=Updates()
    up.run()

def settings():
    st=Settings()
    st.run()
    

# Create Tkinter window
root = tk.Tk()
root.title("Malware Detection Menu")

# Load the image
image = Image.open("abc.jpg")  # Replace "abc.jpg" with your image file
photo = ImageTk.PhotoImage(image)

# Get the width and height of the image
width, height = image.size

# Create a frame with the same size as the image
frame = tk.Frame(root, width=width, height=height)

# Add a label to the frame to display the image
label = tk.Label(frame, image=photo)
label.pack(fill=tk.BOTH, expand=tk.YES)

# Place the frame
frame.pack(fill=tk.BOTH, expand=tk.YES)

# Create a label for "Malware"
malware_label = tk.Label(text="Malware Dtaction", font=("Arial", 50, "bold"), fg="red", bg='black')
malware_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Create buttons
def on_enter(e):
    e.widget.config(bg="#32a8a4", fg="black", font=("Arial", 21, "bold"),  borderwidth=5,  highlightbackground="#32a8a4")

def on_leave(e):
    e.widget.config(bg="black", fg="#32a8a4", font=("Arial", 20), borderwidth=5,  highlightbackground="#32a8a4")

full_scan_button = tk.Button(frame, text="Full Scan", bg="black", fg="#32a8a4", font=("Arial", 20), bd=0, command=full_scan, highlightthickness=0, borderwidth=0, highlightbackground="black")
full_scan_button.place(relx=0.1, rely=0.45)
full_scan_button.bind("<Enter>", on_enter)
full_scan_button.bind("<Leave>", on_leave)

location_scan_button = tk.Button(frame, text="Location Scan", bg="black", fg="#32a8a4", font=("Arial", 20), bd=0, command=location_scan, highlightthickness=0, borderwidth=0, highlightbackground="black")
location_scan_button.place(relx=0.1, rely=0.55)
location_scan_button.bind("<Enter>", on_enter)
location_scan_button.bind("<Leave>", on_leave)

updates_button = tk.Button(frame, text="Updates", bg="black", fg="#32a8a4", font=("Arial", 20), bd=0, command=updates, highlightthickness=0, borderwidth=0, highlightbackground="black")
updates_button.place(relx=0.85, rely=0.45)
updates_button.bind("<Enter>", on_enter)
updates_button.bind("<Leave>", on_leave)

settings_button = tk.Button(frame, text="Settings", bg="black", fg="#32a8a4", font=("Arial", 20), bd=0, command=settings, highlightthickness=0, borderwidth=0, highlightbackground="black")
settings_button.place(relx=0.85, rely=0.55)
settings_button.bind("<Enter>", on_enter)
settings_button.bind("<Leave>", on_leave)

# Run the Tkinter event loop
root.mainloop()

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from MalwareDetector import MalwareDetector
from lists import Lists
from prosess import Process
import result

class Updates:
    def __init__(self):
      self.root = tk.Tk()
      self.root.title("Malware Detection")
      self.root.geometry("1300x700")
      self.root.configure(bg="#F0F0F0")

            # Header Label
      self.header_label = tk.Label(self.root, text="Updates funtion is Devaloping", font=("Arial", 30, "bold"), fg="black", bg="#F0F0F0")
      self.header_label.place(relx=0.5, rely=0.1, anchor="center")  

if __name__ == "__main__":
    frontend = Updates()
    frontend.run()

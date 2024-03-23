import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from MalwareDetector import MalwareDetector
from lists import Lists
from prosess import Process
import result

class AntivirusFrontend:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Malware Detection")
        self.root.geometry("1300x700")
        self.root.configure(bg="#F0F0F0")
        
        # Header Label
        self.header_label = tk.Label(self.root, text="Malware Detection Applycation", font=("Arial", 40, "bold"), fg="#fa0505", bg="#F0F0F0")
        self.header_label.place(relx=0.5, rely=0.1, anchor="center")
        
        # Left Label
        self.left_label = tk.Label(self.root, text="Select if you need to search location:", font=("Arial", 18),fg= "#2196F3", bg="#F0F0F0")
        self.left_label.place(relx=0.05, rely=0.2)
        
        # Enter Location Button
        self.enter_location_button = tk.Button(self.root, text="Choose Location", font=("Arial", 14),   bg="#2196F3", fg="#FFFFFF", command=self.search_location)
        self.enter_location_button.place(relx=0.37, rely=0.2)
        
        # Search Result Frame
        self.result_frame = tk.Frame(self.root, width=1200, height=400, bg="#FFFFFF")
        self.result_frame.place(relx=0.5, rely=0.6, anchor="center")
        
# Delete Malware Button
        self.delete_malware_button = tk.Button(self.root, text="Delete Malware", font=("Arial", 12), fg="#ffffff", bg="#ff5252", activebackground="#ff5252", activeforeground="#ffffff", padx=10, pady=5, borderwidth=0, command=self.delete_malware)
        self.delete_malware_button.place(relx=0.4, rely=0.9, anchor="center")

# More Info Malware Button
        self.more_info_button = tk.Button(self.root, text="More Info", font=("Arial", 12), fg="#ffffff", bg="#2196F3", activebackground="#388E3C", activeforeground="#ffffff", padx=10, pady=5, borderwidth=0, command=self.more_info)
        self.more_info_button.place(relx=0.5, rely=0.9, anchor="center")

# Clear All Data Button
        self.clear_button = tk.Button(self.root, text="Clear All Data", font=("Arial", 12), fg="#ffffff", bg="#2196F3", activebackground="#1976D2", activeforeground="#ffffff", padx=10, pady=5, borderwidth=0, command=self.clear_all_data)
        self.clear_button.place(relx=0.6, rely=0.9, anchor="center")

        # Attach the frame to the bottom of the main frame
        self.result_frame.pack_propagate(False)
        
        # Call function to show search results
       

        # Creating instances of backend classes
        self.malware_detector = MalwareDetector()
        self.lists = Lists()
        self.processor = Process() 

    def clear_tree(self, node):
        if node is None:
            return
        node.children = {}
        for child in node.children.values():
            self.clear_tree(child)

    def clear_all_data(self):
        # Clear stored data
        self.processor.file_path = None
        self.processor.searchingLocation = []
        self.processor.searchResult = []
        self.processor.filePathtoDelete = []
        # Clear TreeNode data structure
        self.clear_tree(self.malware_detector.root)
        
        # Show success notification
        messagebox.showinfo("Success", "Successfully cleared data tree diagram and list.")
        
    def search_location(self):
        # Function to handle opening a directory selection dialog
        search_path = filedialog.askdirectory()
        if search_path:  # If a location is selected
            self.process_file(search_path)
    
    def process_file(self, search_path):
        # Function to process the selected file/location
        self.processor.setFilePath(search_path)
        self.processor.main()  # Call the main method in the Process class
        self.print_search_location()

    def print_search_location(self):
        # Print search results
        search_results = self.processor.searchResult
        if search_results:
            header_label = tk.Label(self.result_frame, text="Malware detected", font=("Arial", 15,"bold"), fg="blue", bg="#FFFFFF")
            header_label.pack(anchor='center')
            
            for lo in search_results:
                file_label = tk.Label(self.result_frame, text=lo, font=("Arial", 11 ,"bold"), fg="red", bg="#FFFFFF")
                file_label.pack(anchor='w')
        
                    
        else:
            header_label = tk.Label(self.result_frame, text="No malware detected. You are safe.", font=("Arial", 16,"bold"), fg="green",bg="#F0F0F0")
            header_label.pack(anchor='center')      


#___________________________________
    def more_info(self):
        serching_locations =self.processor.searchingLocation
        search_results = self.processor.searchResult

        
        if search_results :

            result.show_data(serching_locations,search_results)  # Show search results using result.py
        else:
               self.header_label = tk.Label(self.root, text="Not selected location ", font=("Arial", 15, "bold"), fg="green", bg="#F0F0F0")
               self.header_label.place(relx=0.5, rely=0.95, anchor="center")   





    def delete_malware(self):
        search_results = self.processor.filePathtoDelete
        if search_results:
           num=0
           for path in search_results:
               self.processor.delete_file(path)
               num+=1
           if num>0:
               self.header_label = tk.Label(self.root, text="Malware Deleted successfully, now you are safe", font=("Arial", 15, "bold"), fg="green", bg="#F0F0F0")
               self.header_label.place(relx=0.5, rely=0.95, anchor="center")
           else:
               self.header_label = tk.Label(self.root, text="Malware not Deleted , now not you  are safe", font=("Arial", 15, "bold"), fg="red", bg="#F0F0F0")
               self.header_label.place(relx=0.5, rely=0.95, anchor="center")           

        else:
               self.header_label = tk.Label(self.root, text="Not selected Malware ", font=("Arial", 15, "bold"), fg="green", bg="#F0F0F0")
               self.header_label.place(relx=0.5, rely=0.95, anchor="center")            
      
               

    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    frontend = AntivirusFrontend()
    frontend.run()

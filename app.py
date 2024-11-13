import tkinter as tk
from tkinter import filedialog


class GUI():
    def __init__(self, ppm):
        self.ppm = ppm
        self.window = tk.Tk()
        self.window.title("Pokemon Proxy Maker")
        self.window.geometry("700x700")
        self.title_label = tk.Label(self.window, text="Pokemon Proxy Maker")
        self.title_label.grid(row=0, columnspan=5)

        self.list_label = tk.Label(self.window, text="Deck List File:")
        self.list_label.grid(row=1, column=0)
        self.list_location_label = tk.Label(self.window, text="No file selected...")
        self.list_location_label.grid(row=1, column=1, columnspan=3)
        self.list_button = tk.Button(self.window, text="Load List", command=self.open_list)
        self.list_button.grid(row=1, column=4)

        self.image_label = tk.Label(self.window, text="Image Save Directory:")
        self.image_label.grid(row=2, column=0)
        self.image_directory_label = tk.Label(self.window, text="No directory chosen...")
        self.image_directory_label.grid(row=2, column=1, columnspan=3)
        self.directory_button = tk.Button(self.window, text="Select Directory", command=self.select_directory)
        self.directory_button.grid(row=2, column=4)

        self.download_button = tk.Button(self.window, text="Download and Make Proxies", command=self.ppm.make_proxies)
        self.download_button.grid(row=3, columnspan=5)

        self.status_title_label = tk.Label(self.window, text="Progress")
        self.status_title_label.grid(row=4, columnspan=5)
        self.status_text = tk.Text(self.window)
        self.status_text.grid(row=5, columnspan=5)

        self.status_scroll = tk.Scrollbar(self.window)
        self.status_scroll.grid(row=5, column=5, sticky='ns')
        self.status_scroll.config(command=self.status_text.yview)
        self.status_text.config(yscrollcommand=self.status_scroll.set)

        
    
    def run(self):
        self.window.mainloop()
    
    def open_list(self):
        temp_filename = filedialog.askopenfilename(title="Select Pokemon Proxy List")
        if len(temp_filename) > 0:
            self.ppm.filename = temp_filename
            self.list_location_label.config(text=temp_filename)

    def append_status_label(self, new_text):
        self.status_text.insert(tk.END, new_text)
        self.window.update()
        self.status_text.see(tk.END)

    def select_directory(self):
        temp_directory = filedialog.askdirectory(title="Select Image Download Directory")
        if len(temp_directory) > 0:
            self.ppm.directory = temp_directory
            self.image_directory_label.config(text=temp_directory)
        
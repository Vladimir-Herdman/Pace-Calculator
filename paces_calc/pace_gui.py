import re

import customtkinter as ctk

import paces_calc.pace_formatter as pf


class MyEntryFrame(ctk.CTkFrame):
    def __init__(self, master, title, placeholder, entry_width=140):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.placeholder = placeholder

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray70", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.entry = ctk.CTkEntry(self, width=entry_width, height=28, placeholder_text=self.placeholder)
        self.entry.grid(row=1, column=0, padx=(20, 10), pady=10, sticky='w')

    def get(self):
        return self.entry.get()

class ResultsFrame(ctk.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.label_var = ctk.StringVar(value="")
        
        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray70", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.label = ctk.CTkLabel(self, text="", fg_color="gray80", height=300, width=300, corner_radius=6, textvariable=self.label_var, font=("Courier", 12), anchor="n")
        self.label.grid(row=1, column=0, padx=10, pady=10, stick="esw")

    def set(self, text):
        self.label_var.set(text)

class Pace_Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Pace Calculator")
        self.geometry("800x380")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.from_distance = MyEntryFrame(self, "From Distance", "Insert a distance (400m, 2mi, 5k)", 320)
        self.from_distance.grid(row = 0, column=0, padx=10, pady=(10, 0), sticky = "sew")

        self.from_paces = MyEntryFrame(self, "From Paces (comma seperated for multiple)", "Insert Pace(s) (4:29.2, 2:54:11...)", 320)
        self.from_paces.grid(row = 1, column=0, padx=10, pady=10, sticky = "sew")

        self.to_distances = MyEntryFrame(self, "To Distances (comma seperated for multiple)", "Insert Distance(s) (400m, 2mi, 5k...)", 320)
        self.to_distances.grid(row = 2, column=0, padx=10, pady=10, sticky = "sew")

        self.results_table = ResultsFrame(self, "Results")
        self.results_table.grid(row=0, column=1, padx=10, pady=10, sticky="esw", rowspan=4)

        self.calculate_button = ctk.CTkButton(self, text="Calculate", command=self.calculate_paces_func, corner_radius=35, height=50, width=70)
        self.calculate_button.grid(row=3, column=0, padx=10, pady=10, sticky="sew")

        self.focus_force()
        self.bind("<q>", lambda event: self.destroy())

    def calculate_paces_func(self):
        from_distance = self.from_distance.get()
        from_paces = self.from_paces.get()
        to_distances = self.to_distances.get()

        if ("" in (from_distance, from_paces, to_distances)): return

        from_distance = from_distance + ","
        from_paces += ","
        to_distances += ","

        from_distance = list(map(str.strip, from_distance.split(",")))[0]
        from_paces = list(map(str.strip, from_paces.split(",")))[0:-1]
        to_distances = list(map(str.strip, to_distances.split(",")))[0:-1]
        
        table = pf.format_table(from_paces, from_distance, to_distances)
        table = re.sub(r"\033\[[0-9;]*m", "", table)

        self.results_table.set(table)

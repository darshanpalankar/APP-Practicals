import tkinter as tk
from tkinter import ttk

class FontColorDemo(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Font & Color Demo")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Font & Colors Options
        font_options = ["Cooper Black","Times New Roman", "Courier","Lexend","JetBrains Mono","Berlin Sans FB Demi","Arial"]
        color_options = ["Purple", "Blue", "Green", "Black","Yellow","Red"]

        # Frames for layout
        font_frame = ttk.Labelframe(self, text="Font & Color Settings")
        font_frame.grid(row=0, column=0, padx=30, pady=20)

        # Font Dropdown
        self.font_var = tk.StringVar(value=font_options[0])
        font_dropdown = ttk.Combobox(font_frame, textvariable=self.font_var, values=font_options)
        font_dropdown.pack()

        # Color Dropdown 
        self.color_var = tk.StringVar(value=color_options[0])
        color_dropdown = ttk.Combobox(font_frame, textvariable=self.color_var, values=color_options)
        color_dropdown.pack()

        # Event handling (Lambda function for concise code)
        font_dropdown.bind("<<ComboboxSelected>>", lambda event: self.update_label())
        color_dropdown.bind("<<ComboboxSelected>>", lambda event: self.update_label())

        #Label to Display changes
        self.label = ttk.Label(self, text="Hello, Darshan!!",
                               font=(self.font_var.get(), 32),
                               foreground=self.color_var.get())
        self.label.grid(row=1, column=0,padx= 50, pady=40)

    def update_label(self):
        self.label.config(font=(self.font_var.get(), 32),
                          foreground=self.color_var.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = FontColorDemo(master=root)
    root.mainloop()

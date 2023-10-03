import tkinter as tk
from pull_groups import get_user_data

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Pull Canvas Groups")
        self.geometry("275x75")

        container = tk.Frame(self)
        container.grid_rowconfigure(0, weight=1)
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)

        label = tk.Label(self, text="Enter the class number:")
        label.grid(row=0, column=0, columnspan=1, padx=5, pady=5, sticky='NSEW')

        self.class_number = tk.StringVar()
        class_number_entry = tk.Entry(self, textvariable=self.class_number)
        class_number_entry.grid(row=0, column=1, padx=5, pady=5, sticky='NSEW')

        self.submit_button = tk.Button(self, text='Submit', 
                                       command=lambda x='submit':
                                       self.action_performed(x))
        self.submit_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='NSEW')

    def action_performed(self, text: str):
        if text == "submit":
            get_user_data(self.class_number.get())
            self.submit_button.config(text="Completed!")
        else:
            raise Exception

if __name__ == "__main__":
    app = App()
    app.mainloop()
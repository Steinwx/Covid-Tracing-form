import tkinter as tk
from covid_form import CovidForm

class CovidTracingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("COVID Tracing App")
        self.geometry("400x500")
        
        self.form = CovidForm(self)
        self.form.pack(expand=True, fill='both')

if __name__ == "__main__":
    app = CovidTracingApp()
    app.mainloop()

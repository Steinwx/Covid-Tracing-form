import tkinter as tk

class CovidTracingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("COVID Tracing App")
        self.geometry("400x400")
        
        self.form = CovidForm(self)
        self.form.pack(expand=True, fill='both')


class CovidForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.symptoms = {
            "Fever": tk.IntVar(),
            "Cough": tk.IntVar(),
            "Shortness of Breath": tk.IntVar(),
            "Fatigue": tk.IntVar(),
            "Muscle or Body Aches": tk.IntVar(),
            "Sore Throat": tk.IntVar(),
            "Loss of Taste or Smell": tk.IntVar(),
            "Headache": tk.IntVar(),
            "Chills": tk.IntVar(),
            "Nausea or Vomiting": tk.IntVar(),
            "Diarrhea": tk.IntVar(),
        }

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="COVID Tracing App Form", font=("Helvetica", 16, "bold"))
        label.pack(pady=10)

        for symptom, var in self.symptoms.items():
            checkbox = tk.Checkbutton(self, text=symptom, variable=var, onvalue=1, offvalue=0)
            checkbox.pack(anchor="w", padx=10, pady=5)

        submit_button = tk.Button(self, text="Submit", command=self.submit_form)
        submit_button.pack(pady=20)

    def submit_form(self):
        selected_symptoms = [symptom for symptom, var in self.symptoms.items() if var.get() == 1]
        if selected_symptoms:
            symptoms_string = ", ".join(selected_symptoms)
            message = f"Thank you for submitting the form.\nYou have selected the following symptoms: {symptoms_string}"
        else:
            message = "Thank you for submitting the form.\nYou have not selected any symptoms."

        # Replace this print statement with your desired functionality, e.g., saving data to a file or sending it to a server.
        print(message)


if __name__ == "__main__":
    app = CovidTracingApp()
    app.mainloop()

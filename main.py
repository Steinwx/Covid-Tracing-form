import tkinter as tk
import csv

class CovidTracingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("COVID Tracing App")
        self.geometry("400x500")
        
        self.form = CovidForm(self)
        self.form.pack(expand=True, fill='both')


class CovidForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.address_var = tk.StringVar()

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
            "None of the above": tk.IntVar(),
        }

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="COVID Tracing App Form", font=("Helvetica", 16, "bold"))
        label.pack(pady=10)

        name_label = tk.Label(self, text="Name:")
        name_label.pack(anchor="w", padx=10)

        name_entry = tk.Entry(self, textvariable=self.name_var)
        name_entry.pack(fill='x', padx=10)

        phone_label = tk.Label(self, text="Phone Number:")
        phone_label.pack(anchor="w", padx=10)

        phone_entry = tk.Entry(self, textvariable=self.phone_var)
        phone_entry.pack(fill='x', padx=10)

        address_label = tk.Label(self, text="Address:")
        address_label.pack(anchor="w", padx=10)

        address_entry = tk.Entry(self, textvariable=self.address_var)
        address_entry.pack(fill='x', padx=10)

        for symptom, var in self.symptoms.items():
            checkbox = tk.Checkbutton(self, text=symptom, variable=var, onvalue=1, offvalue=0)
            checkbox.pack(anchor="w", padx=10, pady=5)

        submit_button = tk.Button(self, text="Submit", command=self.submit_form)
        submit_button.pack(pady=20)

    def submit_form(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        address = self.address_var.get()

        selected_symptoms = [symptom for symptom, var in self.symptoms.items() if var.get() == 1 and symptom != "None of the above"]

        if "None of the above" in selected_symptoms:
            selected_symptoms = ["None of the above"]

        if selected_symptoms:
            symptoms_string = ", ".join(selected_symptoms)
            message = f"Thank you, {name}, for submitting the form.\nPhone: {phone}\nAddress: {address}\nYou have selected the following symptoms: {symptoms_string}"
        else:
            message = f"Thank you, {name}, for submitting the form.\nPhone: {phone}\nAddress: {address}\nYou have not selected any symptoms."

        self.log_form_data(name, phone, address, selected_symptoms)
        # You can also call other functions to perform additional actions here.

    def log_form_data(self, name, phone, address, selected_symptoms):
        with open('form_logs.csv', mode='a', newline='') as file:
            fieldnames = ['Name', 'Phone', 'Address', 'Symptoms']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Check if the file is empty and add the header only if it is.
            if file.tell() == 0:
                writer.writeheader()

            writer.writerow({'Name': name, 'Phone': phone, 'Address': address, 'Symptoms': ', '.join(selected_symptoms)})


if __name__ == "__main__":
    app = CovidTracingApp()
    app.mainloop()

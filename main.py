import tkinter as tk
import csv

class CsvLogger:
    def __init__(self, file_path):
        self.file_path = file_path

    def log_form_data(self, name, phone, address, vaccine_taken, exposure, selected_symptoms):
        # Mask sensitive data before logging
        phone_masked = self.mask_phone_number(phone)
        address_masked = self.mask_address(address)
        vaccine_taken_masked = self.mask_vaccine_taken(vaccine_taken)

        with open(self.file_path, mode='a', newline='') as file:
            fieldnames = ['Name', 'Phone', 'Address', 'Covid Vaccine Taken', 'Exposure from Other Covid Patients', 'Symptoms']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if file.tell() == 0:
                writer.writeheader()

            writer.writerow({'Name': name, 'Phone': phone_masked, 'Address': address_masked, 'Covid Vaccine Taken': vaccine_taken_masked, 'Exposure from Other Covid Patients': exposure, 'Symptoms': ', '.join(selected_symptoms)})

    @staticmethod
    def mask_phone_number(phone):
        # Mask phone number except the last four digits
        masked_chars = '*' * (len(phone) - 4)
        return f"{masked_chars}{phone[-4:]}"
    
    @staticmethod
    def mask_address(address):
        # Mask address by showing only the first character and last character of each word
        address_parts = address.split()
        masked_address = ' '.join([f"{part[0]}{'*'*(len(part)-2)}{part[-1]}" for part in address_parts])
        return masked_address

    @staticmethod
    def mask_vaccine_taken(vaccine_taken):
        # Mask vaccine_taken by showing 'Yes' as 'Y**'
        if vaccine_taken.lower() == 'yes':
            return 'Y**'
        return vaccine_taken


class CovidTracingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("COVID Tracing App")
        self.geometry("400x550")
        
        self.form = CovidForm(self)
        self.form.pack(expand=True, fill='both')


class CovidForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.address_var = tk.StringVar()
        self.vaccine_taken_var = tk.StringVar()
        self.exposure_var = tk.StringVar()

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

        vaccine_taken_label = tk.Label(self, text="Covid Vaccine Taken:")
        vaccine_taken_label.pack(anchor="w", padx=10)

        vaccine_taken_entry = tk.Entry(self, textvariable=self.vaccine_taken_var)
        vaccine_taken_entry.pack(fill='x', padx=10)

        exposure_label = tk.Label(self, text="Exposure from Other Covid Patients:")
        exposure_label.pack(anchor="w", padx=10)

        exposure_entry = tk.Entry(self, textvariable=self.exposure_var)
        exposure_entry.pack(fill='x', padx=10)

        for symptom, var in self.symptoms.items():
            checkbox = tk.Checkbutton(self, text=symptom, variable=var, onvalue=1, offvalue=0)
            checkbox.pack(anchor="w", padx=10, pady=5)

        submit_button = tk.Button(self, text="Submit", command=self.submit_form)
        submit_button.pack(pady=20)

    def submit_form(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        address = self.address_var.get()
        vaccine_taken = self.vaccine_taken_var.get()
        exposure = self.exposure_var.get()

        selected_symptoms = [symptom for symptom, var in self.symptoms.items() if var.get() == 1 and symptom != "None of the above"]

        if "None of the above" in selected_symptoms:
            selected_symptoms = ["None of the above"]

        if selected_symptoms:
            symptoms_string = ", ".join(selected_symptoms)
            message = f"Thank you, {name}, for submitting the form.\nPhone: {phone}\nAddress: {address}\nCovid Vaccine Taken: {vaccine_taken}\nExposure from Other Covid Patients: {exposure}\nYou have selected the following symptoms: {symptoms_string}"
        else:
            message = f"Thank you, {name}, for submitting the form.\nPhone: {phone}\nAddress: {address}\nCovid Vaccine Taken: {vaccine_taken}\nExposure from Other Covid Patients: {exposure}\nYou have not selected any symptoms."

        logger = CsvLogger('form_logs.csv')
        logger.log_form_data(name, phone, address, vaccine_taken, exposure, selected_symptoms)
        # You can also call other functions to perform additional actions here.

if __name__ == "__main__":
    app = CovidTracingApp()
    app.mainloop()

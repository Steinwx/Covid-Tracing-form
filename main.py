import tkinter as tk
import csv
from datetime import datetime

class CovidTracingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("COVID Tracing App")
        self.responses = []  # List to store the recorded responses
        self.create_widgets()

    def create_widgets(self):
        self.label_name = tk.Label(self, text="Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(self)
        self.entry_name.pack()

        self.label_phone = tk.Label(self, text="Phone:")
        self.label_phone.pack()
        self.entry_phone = tk.Entry(self)
        self.entry_phone.pack()

        self.label_location = tk.Label(self, text="Location:")
        self.label_location.pack()
        self.entry_location = tk.Entry(self)
        self.entry_location.pack()

        self.label_symptoms = tk.Label(self, text="Symptoms:")
        self.label_symptoms.pack()
        self.entry_symptoms = tk.Text(self, height=5, width=30)
        self.entry_symptoms.pack()

        self.record_button = tk.Button(self, text="Record Response", command=self.record_response)
        self.record_button.pack()

        self.log_button = tk.Button(self, text="View Log", command=self.view_log)
        self.log_button.pack()

    def record_response(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        location = self.entry_location.get()
        symptoms = self.entry_symptoms.get("1.0", tk.END)

        # Get the current date and time
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Append the data to the responses list
        self.responses.append((timestamp, name, phone, location, symptoms))

        # Append the data to a CSV file
        with open('responses.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([timestamp, name, phone, location, symptoms])

        # Clear the input fields after recording the response
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_location.delete(0, tk.END)
        self.entry_symptoms.delete("1.0", tk.END)

    def view_log(self):
        log_window = tk.Toplevel(self)
        log_window.title("Recorded Entries")
        log_text = tk.Text(log_window, height=20, width=50)
        log_text.pack()

        # Display all the recorded responses in the log window
        for response in self.responses:
            log_text.insert(tk.END, f"Time: {response[0]}\nName: {response[1]}\nPhone: {response[2]}\nLocation: {response[3]}\nSymptoms: {response[4]}\n\n")

if __name__ == "__main__":
    app = CovidTracingApp()
    app.mainloop()

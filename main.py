import tkinter as tk
import csv
from datetime import datetime

def record_response():
    name = entry_name.get()
    phone = entry_phone.get()
    location = entry_location.get()
    symptoms = entry_symptoms.get("1.0", tk.END)

    # Get the current date and time
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Append the data to a CSV file
    with open('responses.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([timestamp, name, phone, location, symptoms])

    # Clear the input fields after recording the response
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_location.delete(0, tk.END)
    entry_symptoms.delete("1.0", tk.END)

# Create the main window
root = tk.Tk()
root.title("COVID Tracing App")

# Create and position labels and entry widgets
label_name = tk.Label(root, text="Name:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_phone = tk.Label(root, text="Phone:")
label_phone.pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

label_location = tk.Label(root, text="Location:")
label_location.pack()
entry_location = tk.Entry(root)
entry_location.pack()

label_symptoms = tk.Label(root, text="Symptoms:")
label_symptoms.pack()
entry_symptoms = tk.Text(root, height=5, width=30)
entry_symptoms.pack()

# Create the record button
record_button = tk.Button(root, text="Record Response", command=record_response)
record_button.pack()

# Start the Tkinter event loop
root.mainloop()

import tkinter as tk

# Replace the following with your secure credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.create_widgets()

    def create_widgets(self):
        self.label_username = tk.Label(self, text="Username:")
        self.label_username.pack()
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            self.destroy()
            from covid_tracing_app import CovidTracingApp
            tracing_app = CovidTracingApp()
        else:
            # Show an error message for invalid credentials
            error_label = tk.Label(self, text="Invalid credentials. Try again.", fg="red")
            error_label.pack()

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
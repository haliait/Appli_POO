import tkinter as tk
from tkinter import ttk

class LoginView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.pack(fill="both", expand=True)

        label = ttk.Label(self, text="Connexion Patient", font=("Helvetica", 18, "bold"))
        label.pack(pady=20)

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        ttk.Label(self, text="ID Patient:").pack(pady=5)
        self.username_entry = ttk.Entry(self, textvariable=self.username_var)
        self.username_entry.pack(pady=5)

        ttk.Label(self, text="Mot de passe:").pack(pady=5)
        self.password_entry = ttk.Entry(self, textvariable=self.password_var, show="*")
        self.password_entry.pack(pady=5)

        self.error_label = ttk.Label(self, text="", foreground="red")
        self.error_label.pack()

        login_btn = ttk.Button(self, text="Se connecter", command=self.try_login)
        login_btn.pack(pady=15)

        self.username_entry.focus()

    def try_login(self):
        patient_id = self.username_var.get().strip()
        password = self.password_var.get().strip()

        patient = self.controller.backend.get_patient_by_id(patient_id)
        if patient and password == "patient":  # mot de passe simple pour test
            self.error_label.config(text="")
            self.controller.login_success(patient)
        else:
            self.error_label.config(text="ID ou mot de passe incorrect")

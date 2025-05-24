import tkinter as tk
from tkinter import ttk

class MenuView(ttk.Frame):
    def __init__(self, parent, controller, patient):
        super().__init__(parent)
        self.controller = controller
        self.patient = patient
        self.pack(fill="both", expand=True)

        welcome_label = ttk.Label(self, text=f"Bienvenue {patient['prenom']} {patient['nom']} !", font=("Helvetica", 16, "bold"))
        welcome_label.pack(pady=20)

        ttk.Button(self, text="Voir mon dossier médical", command=self.goto_dossier).pack(pady=10, ipadx=20, ipady=10)
        ttk.Button(self, text="Messagerie interne", command=self.goto_chat).pack(pady=10, ipadx=20, ipady=10)
        ttk.Button(self, text="Déconnexion", command=self.controller.logout).pack(pady=40, ipadx=20, ipady=10)

    def goto_dossier(self):
        self.controller.show_dossier_view(self.patient)

    def goto_chat(self):
        self.controller.show_chat_view(self.patient)

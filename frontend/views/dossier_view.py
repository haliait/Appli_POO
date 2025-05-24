import tkinter as tk
from tkinter import ttk

class DossierView(ttk.Frame):
    def __init__(self, parent, controller, patient):
        super().__init__(parent)
        self.controller = controller
        self.patient = patient
        self.pack(fill="both", expand=True)

        label = ttk.Label(self, text=f"Dossier Médical de {patient['prenom']} {patient['nom']}", font=("Arial", 16))
        label.pack(pady=10)

        columns = ("ID", "Diagnostic", "Ordonnance", "Examens", "Médecin")
        self.table = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=150)
        self.table.pack(fill="both", expand=True, padx=20, pady=10)

        back_btn = ttk.Button(self, text="Retour au menu", command=self.controller.show_menu_view)
        back_btn.pack(pady=15)

        self.load_dossier()

    def load_dossier(self):
        dossiers = self.controller.backend.get_dossiers_by_patient_id(self.patient["id"])
        for d in dossiers:
            self.table.insert("", "end", values=(d["id"], d["diagnostic"], d["ordonnance"], d["examens"], d["docteur_nom"]))

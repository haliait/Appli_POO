import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import ospython -m frontend.main

# Import des vues
from frontend.views.login_view import LoginView
from frontend.views.chat_view import ChatView

from backend.backend import Backend  # Ta classe backend déjà fournie

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Système Hospitalière")
        self.geometry("1000x650")
        self.configure(bg="#f0f4f8")

        self.backend = Backend()  # connexion DB
        self.current_patient = None

        self.active_frame = None
        self.show_login_view()

    def show_login_view(self):
        if self.active_frame:
            self.active_frame.destroy()
        self.active_frame = LoginView(self, self)

    def login_success(self, patient):
        self.current_patient = patient
        self.show_main_view()

    def show_main_view(self):
        if self.active_frame:
            self.active_frame.destroy()

        frame = tk.Frame(self, bg="#f0f4f8")
        frame.pack(fill="both", expand=True)

        sidebar = tk.Frame(frame, bg="#2c3e50", width=200)
        sidebar.pack(side="left", fill="y")

        content = tk.Frame(frame, bg="#ecf0f1")
        content.pack(side="right", fill="both", expand=True)

        tk.Label(sidebar, text="Dashboard", bg="#2c3e50", fg="white", font=("Arial", 16)).pack(pady=20)

        buttons = [
            ("Dossier Médical", lambda: self.show_dossier(content)),
            ("Messagerie", lambda: self.show_chat()),
            ("Carte de l'hôpital", lambda: self.show_map(content)),
            ("Deconnexion", self.show_login_view)
        ]

        for text, cmd in buttons:
            tk.Button(sidebar, text=text, command=cmd, bg="#34495e", fg="white", relief="flat",
                      font=("Arial", 12), width=20).pack(pady=10)

        self.active_frame = frame

    def show_dossier(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()

        tk.Label(parent, text=f"Patient: {self.current_patient['nom']} {self.current_patient['prenom']}", font=("Arial", 18), bg="#ecf0f1").pack(pady=10)
        tk.Label(parent, text="Dossier Médical", font=("Arial", 16), bg="#ecf0f1").pack(pady=10)

        dossiers = self.backend.get_dossiers_by_patient_id(self.current_patient["id"])

        tree = ttk.Treeview(parent, columns=("Diagnostic", "Ordonnance", "Examens", "Docteur"), show='headings')
        tree.heading("Diagnostic", text="Diagnostic")
        tree.heading("Ordonnance", text="Ordonnance")
        tree.heading("Examens", text="Examens")
        tree.heading("Docteur", text="Docteur")
        tree.pack(pady=10, fill="both", expand=True)

        for d in dossiers:
            tree.insert("", "end", values=(d["diagnostic"], d["ordonnance"], d["examens"], d["docteur_nom"]))

    def show_chat(self):
        if self.active_frame:
            self.active_frame.destroy()
        self.active_frame = ChatView(self, self, self.current_patient)

    def show_map(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()

        tk.Label(parent, text="Hospital Map", font=("Arial", 18), bg="#ecf0f1").pack(pady=20)

        try:
            image_path = os.path.join(os.getcwd(), "hospital_map.jpg")
            image = Image.open(image_path)
            image = image.resize((700, 400), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(parent, image=photo, bg="#ecf0f1")
            label.image = photo
            label.pack(pady=10)
        except Exception as e:
            tk.Label(parent, text="Could not load map image.", bg="#ecf0f1", fg="red").pack(pady=10)
            print("Error loading map:", e)


if __name__ == "__main__":
    app = App()
    app.mainloop()

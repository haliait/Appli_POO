import ttkbootstrap as tb
from ttkbootstrap.constants import *
import tkinter as tk

from frontend.views.dossier_view import DossierView
from frontend.views.chat_view import ChatView
from frontend.views.map_view import MapView

class MainView(tb.Frame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Sidebar
        sidebar = tb.Frame(self, bootstyle="secondary", width=200)
        sidebar.grid(row=0, column=0, sticky="ns")
        sidebar.grid_propagate(False)

        # Header sidebar avec nom utilisateur
        user_label = tb.Label(sidebar, text=f"Bonjour, {user['username']} !", font=("Helvetica", 14, "bold"), bootstyle="light")
        user_label.pack(pady=20)

        # Boutons menu
        self.btn_dossier = tb.Button(sidebar, text="Dossiers Médicaux", bootstyle="info-outline", command=lambda: self.show_view("dossier"))
        self.btn_chat = tb.Button(sidebar, text="Messagerie Interne", bootstyle="info-outline", command=lambda: self.show_view("chat"))
        self.btn_map = tb.Button(sidebar, text="Carte de l'Hôpital", bootstyle="info-outline", command=lambda: self.show_view("map"))

        for btn in (self.btn_dossier, self.btn_chat, self.btn_map):
            btn.pack(fill="x", padx=15, pady=8)

        # Zone contenu
        self.container = tb.Frame(self, bootstyle="light")
        self.container.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # Instanciation des vues avec passage utilisateur
        self.views = {
            "dossier": DossierView(self.container, self.user),
            "chat": ChatView(self.container, self.user),
            "map": MapView(self.container, self.user)
        }
        for view in self.views.values():
            view.grid(row=0, column=0, sticky="nsew")

        self.current_view = None
        self.show_view("dossier")

    def show_view(self, name):
        if self.current_view:
            self.current_view.grid_remove()
        self.current_view = self.views[name]
        self.current_view.grid()

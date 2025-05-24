import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class ChatView(ttk.Frame):
    def __init__(self, parent, controller, patient):
        super().__init__(parent)
        self.controller = controller
        self.patient = patient
        self.pack(fill="both", expand=True)

        label = ttk.Label(self, text="Messagerie Interne", font=("Helvetica", 18, "bold"))
        label.pack(pady=10)

        self.chat_display = scrolledtext.ScrolledText(self, wrap=tk.WORD, height=20, state='disabled', font=("Helvetica", 11))
        self.chat_display.pack(padx=20, pady=10, fill="both", expand=True)

        input_frame = ttk.Frame(self)
        input_frame.pack(padx=20, pady=10, fill="x")

        self.message_var = tk.StringVar()
        self.message_entry = ttk.Entry(input_frame, textvariable=self.message_var, font=("Helvetica", 11))
        self.message_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.message_entry.bind("<Return>", self.send_message)

        self.send_button = ttk.Button(input_frame, text="Envoyer", command=self.send_message)
        self.send_button.pack(side="right")

        back_btn = ttk.Button(self, text="Retour au menu", command=self.controller.show_main_view)
        back_btn.pack(pady=10)

    def send_message(self, event=None):
        message = self.message_var.get().strip()
        if message:
            self.display_message("Vous", message)
            self.message_var.set("")

    def display_message(self, author, message):
        self.chat_display.configure(state='normal')
        self.chat_display.insert(tk.END, f"{author} : {message}\n")
        self.chat_display.configure(state='disabled')
        self.chat_display.yview(tk.END)

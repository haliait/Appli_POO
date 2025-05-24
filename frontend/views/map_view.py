import ttkbootstrap as tb
from PIL import Image, ImageTk
import os

class MapView(tb.Frame):
    def __init__(self, parent, user):
        super().__init__(parent, bootstyle="light")
        self.user = user

        label = tb.Label(self, text="Carte de l'Hôpital", font=("Helvetica", 18, "bold"))
        label.pack(pady=15)

        try:
            base_path = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(base_path, "hospital_map.jpg")  # Assure-toi que l'image est dans le même dossier
            image = Image.open(image_path)
            image = image.resize((700, 400), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(image)
        except Exception as e:
            self.photo = None
            print("Erreur chargement image carte:", e)

        if self.photo:
            canvas = tb.Canvas(self, width=700, height=400)
            canvas.pack(padx=20, pady=10)
            canvas.create_image(0, 0, anchor="nw", image=self.photo)
        else:
            tb.Label(self, text="Image de la carte non trouvée", bootstyle="danger").pack(pady=20)

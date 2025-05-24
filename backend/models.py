from backend.database import get_connection

class Personne:
    def __init__(self, nom, prenom, telephone):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone

class Patient(Personne):
    def __init__(self, id, nom, prenom, age, sexe, telephone):
        super().__init__(nom, prenom, telephone)
        self.id = id
        self.age = age
        self.sexe = sexe

    def to_dict(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'prenom': self.prenom,
            'age': self.age,
            'sexe': self.sexe,
            'telephone': self.telephone
        }

class Docteur(Personne):
    def __init__(self, id, nom, prenom, specialite, email, telephone):
        super().__init__(nom, prenom, telephone)
        self.id = id
        self.specialite = specialite
        self.email = email

class Dossier:
    def __init__(self, id, patient_id, docteur_id, diagnostic, ordonnance, examens):
        self.id = id
        self.patient_id = patient_id
        self.docteur_id = docteur_id
        self.diagnostic = diagnostic
        self.ordonnance = ordonnance
        self.examens = examens

    @classmethod
    def get_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM Dossier WHERE patient_id = %s', (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(
                id=row['id'],
                patient_id=row['patient_id'],
                docteur_id=row['docteur_id'],
                diagnostic=row['diagnostic'],
                ordonnance=row['ordonnance'],
                examens=row['examens']
            )
        return None

    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'docteur_id': self.docteur_id,
            'diagnostic': self.diagnostic,
            'ordonnance': self.ordonnance,
            'examens': self.examens
        }
import mysql.connector

class Backend:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="UM6SS", 
            database="hopital_bd"
        )

    def get_patient_by_id(self, patient_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Patient WHERE id=%s", (patient_id,))
        result = cursor.fetchone()
        if result:
            return {
                "id": result[0],
                "nom": result[1],
                "prenom": result[2],
                "age": result[3],
                "sexe": result[4],
                "telephone": result[5],
            }
        return None

    def get_dossiers_by_patient_id(self, patient_id):
        cursor = self.conn.cursor()
        query = """
            SELECT Dossier.id, Dossier.diagnostic, Dossier.ordonnance, Dossier.examens, Docteur.nom
            FROM Dossier
            JOIN Docteur ON Dossier.docteur_id = Docteur.id
            WHERE Dossier.patient_id = %s
        """
        cursor.execute(query, (patient_id,))
        results = cursor.fetchall()
        dossiers = []
        for row in results:
            dossiers.append({
                "id": row[0],
                "diagnostic": row[1],
                "ordonnance": row[2],
                "examens": row[3],
                "docteur_nom": row[4]
            })
        return dossiers

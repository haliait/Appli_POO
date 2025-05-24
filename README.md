
# Application Locale et Sécurisée pour Hôpitaux

Ce projet est une application de gestion hospitalière locale, conçue pour offrir un accès simplifié, sécurisé et hors-ligne à certaines fonctionnalités médicales essentielles telles que : la consultation de dossiers médicaux fictifs, une messagerie simulée entre patients et médecins, et une carte interactive de l’hôpital.

---

## Fonctionnalités

- Interface de connexion (identifiants fictifs)
- Consultation d’un dossier médical simulé
- Messagerie simulée entre patient et médecin
- Carte interactive statique de l’hôpital
- Application en mode local (pas besoin d'internet)

---

## Prérequis techniques

- Python 3.9 ou plus
- Systèmes compatibles : Windows, Linux, MacOS

### Dépendances Python

Assurez-vous d'installer les bibliothèques suivantes :

```
pip install flask
pip install tkintertable  # si utilisé
```

---

## Instructions d'installation

1. Clonez ou téléchargez ce dépôt.
2. Placez-vous dans le dossier racine du projet.
3. Lancez le backend Flask :

```
python app.py
```

4. Lancez ensuite l’interface Tkinter :

```
python main.py
```

(Vérifiez que le fichier `hopital_bd.db` est bien dans le même dossier ou accessible par les scripts.)

---

## Organisation du projet

- `app.py` : serveur Flask (gère les requêtes)
- `main.py` : interface utilisateur avec Tkinter
- `hopital_bd.db` : base de données SQLite fictive
- `README.md` : ce fichier

---

## Remarques

- le mot de passe de login est 'patient'
- le mot de passe de la base de données MySQL est 'UM6SS' 
- Ce prototype est uniquement destiné à un usage académique.
- Aucune donnée réelle n’est utilisée.
- Aucune couche de sécurité réelle n’est implémentée (authentification simplifiée).

---

## Auteurs

- Groupe de 2 étudiantes en ingénierie Génie Digital en Santé

---

## Perspectives

Ce prototype peut être étendu pour devenir une vraie application en réseau sécurisé, avec :
- Authentification réelle
- Base de données distante
- Chatbot intelligent
- Interface web moderne


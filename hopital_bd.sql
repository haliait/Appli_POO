create database hopital;

create table Patient (
	id int primary key,
	nom varchar(20),
    prenom varchar(20),
    age int,
    sexe varchar(10),
    telephone long
);

create table Docteur (
	id int primary key,
	nom varchar(20),
    prenom varchar(20),
    specialite varchar(50),
    email varchar(100),
    telephone long
);

create table Dossier (
	id int primary key,
    patient_id int,
    docteur_id int,
    diagnostic varchar(100),
    ordonnance varchar(100),
    examens varchar(100),
    foreign key(patient_id) references Patient(id),
    foreign key(docteur_id) references Docteur(id)
);

create table Historique (
	id int primary key,
    patient_id int,
    dateConsultation date,
    diagnostic varchar(100),
    traitment varchar(100),
    foreign key(patient_id) references Patient(id)
);

insert into Patient
Values(1, 'El Khayat', 'Amina',	34,	'Femme',	0611223344),
(2,	'Bouziane', 'Omar',	45,	'Homme',	0677889900),
(3,	'Belkadi', 'Sara',	29,	'Femme',	0622334455),
(4,	'Chafik', 'Mehdi', 51,	'Homme',	0655443322),
(5,	'Ouazzani', 'Laila', 38,	'Femme',	0633556677);

insert into Docteur
values(1, 'Dr. El Alaoui', 'Yassine',	'Cardiologue',	'y.elalaoui@hopital.ma',	0612345678),
(2,	'Dr. Rahmani', 'Sofia', 'Diabétologue',	's.rahmani@hopital.ma',	0687654321),
(3,	'Dr. Benjelloun', 'Karim', 'Orthopédiste',	'k.benjelloun@hopital.ma',	0622334455),
(4,	'Dr. Idrissi', 'Salma', 'Pneumologue',	's.idrissi@hopital.ma',	0644221100);

insert into Dossier
Values(1,	1,	1,	'Hypertension modérée',	'Ramipril 5mg/jour',	'ECG normal, tension 14/9'),
(2,	2,	2,	'Diabète de type 2',	'Metformine 850mg matin et soir',	'Glycémie à jeun : 1.45 g/L'),
(3,	3,	3,	'Douleurs lombaires chroniques',	'Paracétamol 1g + kinésithérapie',	'Radio lombaire : anomalies L4-L5'),
(4,	4,	1,	'Tachycardie sinusale légère',	'Surveillance + bêtabloquants légers',	'ECG rapide, échographie cardiaque normale'),
(5,	5,	4,	'Asthme modéré',	'Salbutamol spray + éviction allergènes',	'Spirométrie : VEMS réduit');

insert into Historique 
Values(1,	1,	'2024-04-12',	'Tension instable',	'Repos + surveillance'),
(2,	2,	'2023-11-20',	'Pré-diabète',	'Régime alimentaire + marche quotidienne'),
(3,	3,	'2024-01-10',	'Entorse lombaire légère',	'Anti-inflammatoires + repos'),
(4,	4,	'2022-09-15',	'Palpitations',	'Électrocardiogramme, pas de traitement'),
(5,	5,	'2023-05-03',	'Rhume allergique',	'Antihistaminiques'),
(6,	3,	'2023-08-28',	'Sciatique légère',	'Physiothérapie'),
(7,	2,	'2022-12-10',	'Surpoids',	'Suivi diététique mensuel');















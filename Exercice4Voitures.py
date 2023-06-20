# Exercice Créer une liste de 4 Voiture
# Trouver un moyen pour informer quelle personne conduit quelle voiture ???

###Création de la class Voiture:
class Voiture:
    def __init__(self, Vmarque, Vmodel, Vannee):
        self.marque = Vmarque
        self.model = Vmodel
        self.annee = Vannee

### Création de la class Conducteur:
class Conducteur:
    def __init__(self, nom, gender, age):
        self.nom = nom
        self.gender = gender
        self.age = age
        self.voiture = None

    def conduire_voiture(self, voiture):
        self.voiture = voiture


### création des voitures:
voitures = [Voiture("Nissan", "Sentra", "2009"), Voiture("Toyota", "Prius", "2023"),
            Voiture("Tesla", "Model 3", "2017"), Voiture("Hyundai", "Santa Fe", "2020")]

conducteur = [] ###liste conducteur pour class Conducteur

while True:
    nom = input("Saisir le nom du propiétaire: ")
    gender = input("Saisir le genre du conducteur: ") ###pour des mesures sécuritaires.
    age = int(input("Saisir l'âge:"))
    marque = input("Saisir la marque pour le trouver:")
    for voiture in voitures:
        if voiture.marque == marque:
            conducteur = Conducteur(nom, gender, age)


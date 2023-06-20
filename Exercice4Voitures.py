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
vtr_1 = Voiture("Nissan", "Sentra", "2009")
vtr_2 = Voiture("Toyota", "Prius", "2023")
vtr_3 = Voiture("Tesla", "Model 3", "2017")
vtr_4 = Voiture("Hyundai", "Santa Fe", "2020")
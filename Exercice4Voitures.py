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
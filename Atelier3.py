class Voiture:
    def _init_(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur

    def afficher_infos(self):
        print("Matricule :", self.matricule)
        print("Marque :", self.marque)
        print("Couleur :", self.couleur)

class Parc:
    def _init_(self,id,adresse,capacite marque,iste_voitures):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.liste_voitures = liste_voitures):
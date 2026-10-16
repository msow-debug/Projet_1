import json

#---- Lire le fichier json----

def read_json(lien_doc):
    file = open(lien_doc,"r")
    data = json.load(file)
    return data

data_2 = read_json("./mesures_capteurs_reseau.json")

#---- Création de la class capteur----

class capteur() : 

#---- Initialisation des paramètres pour chaque capteur----

    def __init__(self , nom_capteur,mesures_brutes) : 
        self.nom = nom_capteur
        self.mesures_brutes = mesures_brutes
        self.mesures_nettoyées = []

#---- Method pour nettoyer les fichiers des informations faussées ----
    
    def nettoyer(self, min, max) :
        for obj in self.mesures_brutes: 
            if type(obj) == int or type(obj) == float : 
                if min<=obj<=max:
                    self.mesures_nettoyées.append(obj)
        return (self.mesures_nettoyées)
        
     
#---- Ecritue dans le nouveau fichier json -----   

def write_json(nom_capteur, mesures_nettoyées: list):
        data_2[nom_capteur] = mesures_nettoyées
        file_out = open("./mesures_capteurs_nettoyées.json","w", encoding = "utf-8")
        json.dump(data_2, file_out, indent = 2)
        print(mesures_nettoyées)
        return 

#----Fonction trier-----------

def trier(self) : 
     capteurs_trier = []
     mesures = self.mesures_nettoyées

     if len(mesures) > 0 :
         moyenne = sum(mesures) / len(mesures)
         capteurs_trier.append(moyenne)

     return capteurs_trier 
               
#----Création des différents capteurs -----

temperature = capteur("temperature_bureau", data_2["temperature_bureau"] )
humidite = capteur ("humidite_serre" , data_2["humidite_serre"])
pression = capteur ("pression_capteur_ext" , data_2["pression_capteur_ext"])
luminosite = capteur ("luminosite_atelier" , data_2["luminosite_atelier"])

#----Appel des fonctions----

write_json("temperature_bureau", temperature.nettoyer(0,30))
write_json("humidite_serre" , humidite.nettoyer(60,70))
write_json("pression_capteur_ext" , pression.nettoyer(1000,1015))
write_json("luminosite_atelier" , luminosite.nettoyer(400,500))
write_json("temperature_bureau" , trier(temperature))
write_json("humidite_serre" , trier(humidite))
write_json("pression_capteur_ext" , trier(pression))
write_json("luminosite_moyen" , trier(luminosite))

# Script ingestion et nettoyage de donnes
import pandas as pd

# chemin du fichier csv
file_path = '../data/Student_Mental_health.csv'

# Lire le fichier CSV dans un DataFrame
df = pd.read_csv(file_path)

# Nettoyage : Exemple de suppression des valeurs manquantes
df = df.dropna()

# Renomer mes colonnes
df.columns = ['Timestamp','Sexe','Age','Profession','AnneeEtudeActuelle','CGPA','SituationMatrimonial','Depressif?','Anxieux?','CrisePanique?','SuivieParUnSpecialiste?']

# Sauvegarde du fichier transformé dans le dossier output
output_path= '../output/Student_Mental_health_nettoye.csv'
df.to_csv(output_path, index= False)

# Affiche les premières lignes pour vérifier l'ingestion
print("Données initiales")
print(df.head())
# Script ingestion et nettoyage de donnes
from operator import index

import pandas as pd
# chemin du fichier csv
file_path = '../data/Student_Mental_health.csv'

# Lire le fichier CSV dans un DataFrame
df = pd.read_csv(file_path)

# Nettoyage : Exemple de suppression des valeurs manquantes
df = df.dropna()

# Renomer mes colonnes
df.columns = ['Timestamp','Sexe','Age','Profession','AnneeEtudeActuelle','CGPA','SituationMatrimonial','Depressif?','Anxieux?','CrisePanique?','SuivieParUnSpecialiste?']


# nouvelle DataFrame
df_restreind = df[['Sexe', 'Age']]
# ajout de nouvelle colone

# regrouper pas sexe et age et compter le nombre d'occurence
df_restreind = df_restreind.groupby(['Sexe','Age']).size().reset_index(name='count')

# chemin de sortir
output_path= '../output/Student_Mental_health_nettoye.xlsx'
# Sauvegarder dans un fichier Excel avec plusieurs feuilles
# xls = pd.ExcelFile(output_path)
# df1 = df.read_excel(xls,'first_Date_Clear', index=False)
# df2 = df_restreind.read_excel(xls,'Count_By_Age_Sex', index=False)

with pd.ExcelWriter(output_path) as writer:
    df.to_excel(writer, sheet_name='first_Date_Clear', index=False)
    df_restreind.to_excel(writer, sheet_name='Count_By_Age_Sex', index=False)

# Affiche les premières lignes pour vérifier l'ingestion
print("Données initiales")
print(df.head())
print(df_restreind)
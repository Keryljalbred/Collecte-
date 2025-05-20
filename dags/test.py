from pymongo import MongoClient
import pandas as pd

def export_and_display_logs():
    # Connexion à MongoDB
    client = MongoClient("mongo_db", 27017)
    db = client["logs_db"]
    collection = db["logs"]

    # Lire tous les logs depuis MongoDB
    logs_cursor = collection.find()
    logs_list = list(logs_cursor)

    # Conversion en DataFrame
    df = pd.DataFrame(logs_list)

    # Supprimer la colonne _id générée par MongoDB
    if "_id" in df.columns:
        df.drop(columns=["_id"], inplace=True)

    # Affichage des 5 premières lignes
    print("✅ Voici les 5 premières lignes des logs en base :")
    print(df.head())

    # Sauvegarder en CSV si tu veux
    df.to_csv("logs_export.csv", index=False)

# Exécuter si ce fichier est lancé seul
if __name__ == "__main__":
    export_and_display_logs()

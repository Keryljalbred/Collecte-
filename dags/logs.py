import pandas as pd
from pymongo import MongoClient

def export_logs_to_csv(
    mongo_host="mongo_db", 
    mongo_port=27017, 
    db_name="logs_db", 
    collection_name="logs", 
    output_csv_path="/opt/airflow/dags/logs_export.csv"
):
    # Connexion à MongoDB
    client = MongoClient(mongo_host, mongo_port)
    db = client[db_name]
    collection = db[collection_name]

    # Récupération des documents
    documents = list(collection.find())
    
    if not documents:
        print("❌ Aucun log trouvé dans MongoDB.")
        return

    # Conversion en DataFrame
    df = pd.DataFrame(documents)

    # Suppression éventuelle de la colonne _id (non sérialisable en CSV)
    if "_id" in df.columns:
        df.drop(columns=["_id"], inplace=True)

    # Export en CSV
    df.to_csv(output_csv_path, index=False)

    print(f"✅ {len(df)} logs exportés vers {output_csv_path}")
    print(df.head())        # Aperçu des premières lignes
    print(df.columns)       # Affiche les colonnes

if __name__ == "__main__":
    export_logs_to_csv()

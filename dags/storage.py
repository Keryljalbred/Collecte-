from pymongo import MongoClient

def store_cleaned_logs(cleaned_logs):
    if not cleaned_logs:
        print("❌ Aucun log à insérer")
        return

    try:
        client = MongoClient("mongo_db", 27017)  # Assurez-vous que l'URL est correcte
        db = client["logdb"]
        collection = db["cleaned_logs"]

        # Insertion des logs
        result = collection.insert_many(cleaned_logs)
        print(f"✅ {len(result.inserted_ids)} logs insérés avec succès dans MongoDB")

    except Exception as e:
        print(f"🚨 Erreur lors de l'insertion dans MongoDB : {e}")
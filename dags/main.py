from ingest import read_logs
from clean import clean_and_transform_logs
from storage import store_cleaned_logs  # Importer la fonction pour interroger les logs
import json

def main():
    # Étape 2 : Lire les logs
    logs = read_logs("logs.txt")

    # Étape 3 : Nettoyer et transformer les logs
    cleaned_logs = clean_and_transform_logs(logs)

    # Afficher les 5 premières entrées nettoyées
    print("Entrées nettoyées :")
    for entry in cleaned_logs[:5]:
        print(json.dumps(entry, indent=4))
        print(cleaned_logs.head())      # Affiche les premières lignes
        print(cleaned_logs.columns) 

      # Appeler la fonction pour interroger les logs

if __name__ == "__main__":
    main()
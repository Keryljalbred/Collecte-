# 🧩 Projet : Pipeline de collecte et d’analyse de logs avec Apache Airflow & MongoDB

## 📘 Contexte

Une entreprise souhaite surveiller et analyser les activités de ses serveurs web afin de :
- Détecter les erreurs,
- Suivre les performances,
- Comprendre les tendances d’utilisation.

Les logs générés quotidiennement par les serveurs doivent être :
1. Collectés automatiquement,
2. Nettoyés et structurés,
3. Stockés efficacement pour être analysés.

---

## 🎯 Objectifs du projet

### 1. Collecte des logs
- Récupérer les logs depuis différentes sources (serveurs web, applications, etc.).
- Automatiser l’extraction des fichiers de log quotidiennement.

### 2. Nettoyage et transformation
- Filtrer les logs inutiles (fichiers CSS, images, etc.).
- Extraire les champs clés : **adresse IP, date/heure, URL, code HTTP, User-Agent**.
- Structurer les données en **JSON** pour MongoDB.

### 3. Stockage NoSQL
- Insérer les logs nettoyés dans **MongoDB**.
- Créer des index pour accélérer les recherches.

### 4. Orchestration avec Apache Airflow
- Automatiser les étapes de collecte, traitement et stockage.
- Superviser les exécutions et gérer les erreurs automatiquement.

---

## 🛠️ Stack technique

| Technologie     | Rôle                                                                 |
|----------------|----------------------------------------------------------------------|
| 🐍 Python       | Lecture, nettoyage, transformation des logs                          |
| 🗃️ MongoDB      | Stockage NoSQL des logs structurés                                    |
| 🪂 Apache Airflow | Orchestration du pipeline ETL                                        |
| 📊 Power BI     | Visualisation des données exportées                                   |
| 🐳 Docker        | Conteneurisation des services pour un déploiement reproductible      |

---


---

## 📥 Sources de logs utilisées

- [Apache HTTP Logs](https://httpd.apache.org/docs/2.4/logs.html)
- [Fake Apache Log Generator](https://github.com/kiritbasu/Fake-Apache-Log-Generator)
- [Common Crawl Logs](https://commoncrawl.org/)

---

## 🧪 Étapes du projet

1. **Définition de la source**
   - Configuration d’un générateur de logs ou import depuis un serveur réel.

2. **Ingestion**
   - Extraction automatique via Airflow (quotidiennement).

3. **Nettoyage & transformation**
   - Suppression des lignes non pertinentes.
   - Standardisation des données (JSON).
   - Enrichissement possible (géolocalisation IP, catégories HTTP).

4. **Stockage MongoDB**
   - Insertion dans `logs_db.cleaned_logs`.
   - Indexation sur les champs clés (ex: IP, date, code HTTP).

5. **Automatisation avec Airflow**
   - DAG avec 3 tâches : `ingest_logs`, `clean_logs`, `store_logs`.
   - Planning quotidien, logs d’exécution et alertes.

6. **Export des données**
   - Export automatique des logs depuis MongoDB vers un fichier `logs_export.csv` (via script Python).
   - Fichier utilisé comme **source de données Power BI**.

---

## 📊 Visualisation avec Power BI

- Le fichier `logs_export.csv` généré peut être importé dans Power BI Desktop.
- Exemples de visualisations :
  - 📈 Évolution du nombre de requêtes HTTP dans le temps
  - 🌐 Répartition des adresses IP (trafic par pays)
  - 🧾 Top des pages demandées
  - ❗ Analyse des erreurs (codes HTTP 4xx, 5xx)
  - 📱 Analyse des User-Agent (navigateurs / OS les plus utilisés)

### Étapes d’intégration Power BI :
1. Ouvrir Power BI Desktop
2. Importer `logs_export.csv`
3. Créer des visualisations avec les champs : `ip`, `date`, `request`, `status`, `user_agent`, etc.
4. Mettre en forme les graphiques et ajouter des filtres dynamiques.
5. Optionnel : programmer une **actualisation automatique** du fichier CSV.

---

lla/5.0 ..."
}

📫 Contact
Projet réalisé dans un cadre pédagogique.

Auteur : [BJEUKOUA KERYL]

Email : [keryljk@gmail.com]



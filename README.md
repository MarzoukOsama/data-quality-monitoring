&nbsp;🔍 Data Quality Monitoring System



Système automatisé de surveillance et validation de la qualité des données avec génération de rapports HTML professionnels.



&nbsp;📋 Description



Ce projet implémente un framework complet de Data Quality Management qui analyse automatiquement la qualité des datasets et génère des rapports détaillés. Il identifie les problèmes de données avant qu'ils n'impactent les analyses ou modèles.



&nbsp;🎯 Objectifs



\- Valider automatiquement la qualité des données

\- Détecter anomalies, outliers et incohérences

\- Générer des rapports HTML visuels et actionnables

\- Configurer des règles métier personnalisables

\- Fournir un score de qualité global



&nbsp;🛠️ Technologies utilisées



\- \*\*Python 3.x\*\*

\- \*\*Pandas\*\* : Analyse et validation de données

\- \*\*NumPy\*\* : Calculs statistiques et détection d'outliers

\- \*\*Jinja2\*\* : Génération de templates HTML

\- \*\*JSON\*\* : Configuration des règles de validation



&nbsp;✅ Contrôles de qualité implémentés



&nbsp;1. Freshness (Fraîcheur)

\- Vérifie l'âge des données

\- Alerte si dernière mise à jour > seuil défini



&nbsp;2. Completeness (Complétude)

\- Détecte colonnes manquantes

\- Identifie valeurs nulles/manquantes

\- Calcule le taux de complétude par colonne



&nbsp;3. Validity (Validité)

\- Valide les plages de valeurs (min/max)

\- Vérifie les contraintes métier

\- Détecte valeurs aberrantes



&nbsp;4. Consistency (Cohérence)

\- Détecte les doublons

\- Vérifie formats de dates

\- Valide relations entre colonnes



&nbsp;5. Outliers Detection

\- Méthode IQR (Interquartile Range)

\- Détection automatique sur colonnes numériques

\- Seuils configurables



&nbsp;📁 Structure du projet



data-quality-monitoring/

│

├── config/

│ └── quality\_rules.json  Règles de validation configurables

│

├── src/

│ ├── validators.py  Classes de validation

│ ├── reporter.py  Génération rapports HTML

│ └── init.py

│

├── data/

│ └── input/  Données à valider (non versionnées)

│

├── reports/  Rapports HTML générés (non versionnés)

│

├── logs/  Logs d'exécution

│

├── monitor.py  Script principal

├── requirements.txt

└── README.md







&nbsp;🚀 Installation



1\. \*\*Cloner le repository\*\*

git clone https://github.com/MarzoukOsama/data-quality-monitoring.git

cd data-quality-monitoring







2\. \*\*Créer un environnement virtuel\*\*

python -m venv venv

venv\\Scripts\\activate  Windows

source venv/bin/activate  Linux/Mac







3\. \*\*Installer les dépendances\*\*

pip install -r requirements.txt







&nbsp;▶️ Utilisation



&nbsp;1. Placer vos données



Copiez votre fichier CSV dans `data/input/` :

copy votre\_fichier.csv data/input/ecommerce\_transactions.csv







&nbsp;2. Configurer les règles (optionnel)



Modifiez `config/quality\_rules.json` pour adapter les seuils à vos besoins :



{

"freshness": {

"max\_age\_hours": 24

},

"completeness": {

"max\_null\_percentage": 5

},

"validity": {

"quantity": {"min": 1, "max": 100},

"unit\_price": {"min": 0, "max": 10000}

}

}







&nbsp;3. Exécuter le monitoring



python monitor.py







&nbsp;4. Consulter le rapport



Le système génère automatiquement un rapport HTML dans `reports/` avec :

\- 📊 Score de qualité global (0-100%)

\- 📈 Niveau de qualité (Excellent/Bon/Acceptable/Faible)

\- ✅ Détail de chaque contrôle avec statut PASS/FAIL/WARNING

\- 📋 Statistiques détaillées et recommandations



&nbsp;📊 Exemple de résultat



🔍 RÉSUMÉ DU CONTRÔLE QUALITÉ

📁 Dataset: E-commerce Transactions

🎯 Score global: 85.7%

📈 Niveau: 🟡 Bon



Contrôle Statut Score

Freshness ❌ FAIL 0.0%

Completeness - Nulls ✅ PASS 100.0%

Validity - quantity ✅ PASS 100.0%

Validity - unit\_price ✅ PASS 100.0%

Duplicates ✅ PASS 100.0%

Outliers - quantity ✅ PASS 100.0%

Outliers - unit\_price ✅ PASS 100.0%







&nbsp;🎨 Capture d'écran du rapport HTML



Le rapport HTML généré inclut :

\- Dashboard avec score visuel coloré

\- Graphiques de distribution des statuts

\- Tableau interactif des contrôles

\- Design professionnel responsive



&nbsp;🔧 Personnalisation



&nbsp;Ajouter un nouveau contrôle



Dans `src/validators.py`, ajoutez une nouvelle méthode :



def check\_custom\_rule(self, df):

"""Votre règle personnalisée"""

&nbsp;Votre logique de validation

self.results.append({

'check': 'Custom Rule',

'status': 'PASS',

'details': 'Description',

'score': 100

})







&nbsp;Modifier les seuils de scoring



Dans `config/quality\_rules.json`, section `thresholds` :



"thresholds": {

"excellent": 95,

"good": 80,

"acceptable": 60,

"poor": 0

}







&nbsp;🎯 Cas d'usage



\- \*\*Data Engineering\*\* : Validation avant chargement dans warehouse

\- \*\*ETL Pipelines\*\* : Contrôle qualité post-transformation

\- \*\*Machine Learning\*\* : Validation datasets avant entraînement

\- \*\*Reporting\*\* : Monitoring quotidien de la qualité

\- \*\*Data Governance\*\* : Audit et conformité



&nbsp;🚀 Évolutions futures



\- \[ ] Intégration alertes email automatiques

\- \[ ] Dashboard temps réel avec Streamlit

\- \[ ] Export métriques vers base de données

\- \[ ] API REST pour intégration CI/CD

\- \[ ] Détection de drift temporel

\- \[ ] Comparaison qualité entre datasets



&nbsp;👨‍💻 Auteur



\*\*Oussama Marzouk\*\*  

Data Analyst | Python Developer  

\[GitHub](https://github.com/MarzoukOsama)



&nbsp;📝 Licence



Ce projet est développé à des fins de portfolio et d'apprentissage.


import pandas as pd
import sys
import os
from datetime import datetime

# Ajouter le dossier src au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from validators import DataQualityValidator
from reporter import QualityReporter

def main():
    print("\n" + "="*70)
    print("🔍 DATA QUALITY MONITORING SYSTEM")
    print("="*70 + "\n")
    
    # Charger les données
    data_path = 'data/input/ecommerce_transactions.csv'
    
    if not os.path.exists(data_path):
        print(f"❌ Fichier non trouvé: {data_path}")
        print("\n💡 Conseil: Copie le fichier depuis ton projet ETL:")
        print("   copy ..\\etl-ecommerce-pipeline\\data\\raw\\ecommerce_transactions.csv data\\input\\")
        return
    
    print(f"📂 Chargement des données: {data_path}")
    df = pd.read_csv(data_path)
    print(f"✅ {len(df)} lignes chargées\n")
    
    # Exécuter les validations
    validator = DataQualityValidator()
    results, score = validator.run_all_checks(df)
    
    # Générer le rapport
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = f"reports/quality_report_{timestamp}.html"
    
    reporter = QualityReporter(results, score, "E-commerce Transactions")
    reporter.print_console_summary()
    reporter.generate_html_report(report_path)
    
    print(f"\n🌐 Ouvre le rapport dans ton navigateur:")
    print(f"   {os.path.abspath(report_path)}\n")

if __name__ == "__main__":
    main()

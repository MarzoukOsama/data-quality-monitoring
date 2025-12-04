import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

class DataQualityValidator:
    
    def __init__(self, config_path='config/quality_rules.json'):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        self.results = []
        self.score = 0
        
    def check_freshness(self, df):
        """Vérifie la fraîcheur des données"""
        date_col = self.config['freshness']['date_column']
        max_age = self.config['freshness']['max_age_hours']
        
        df[date_col] = pd.to_datetime(df[date_col])
        latest_date = df[date_col].max()
        age_hours = (datetime.now() - latest_date).total_seconds() / 3600
        
        status = "PASS" if age_hours <= max_age else "FAIL"
        
        self.results.append({
            'check': 'Freshness',
            'status': status,
            'details': f"Dernière mise à jour il y a {age_hours:.1f}h (limite: {max_age}h)",
            'score': 100 if status == "PASS" else 0
        })
        
    def check_completeness(self, df):
        """Vérifie la complétude des données"""
        required_cols = self.config['completeness']['required_columns']
        max_null_pct = self.config['completeness']['max_null_percentage']
        
        # Colonnes manquantes
        missing_cols = set(required_cols) - set(df.columns)
        if missing_cols:
            self.results.append({
                'check': 'Completeness - Columns',
                'status': 'FAIL',
                'details': f"Colonnes manquantes: {missing_cols}",
                'score': 0
            })
            return
        
        # Valeurs nulles
        null_counts = df[required_cols].isnull().sum()
        null_pcts = (null_counts / len(df)) * 100
        
        issues = null_pcts[null_pcts > max_null_pct]
        
        if len(issues) > 0:
            status = "FAIL"
            details = f"{len(issues)} colonnes avec >{max_null_pct}% nulls: {dict(issues.round(2))}"
            score = max(0, 100 - len(issues) * 20)
        else:
            status = "PASS"
            details = f"Toutes les colonnes ont <{max_null_pct}% de valeurs nulles"
            score = 100
            
        self.results.append({
            'check': 'Completeness - Nulls',
            'status': status,
            'details': details,
            'score': score
        })
        
    def check_validity(self, df):
        """Vérifie la validité des valeurs"""
        validity_rules = self.config['validity']
        
        for column, rules in validity_rules.items():
            if column not in df.columns:
                continue
                
            invalid_count = 0
            
            # Vérifier min
            if 'min' in rules:
                invalid_count += (df[column] < rules['min']).sum()
                
            # Vérifier max
            if 'max' in rules:
                invalid_count += (df[column] > rules['max']).sum()
            
            invalid_pct = (invalid_count / len(df)) * 100
            status = "PASS" if invalid_pct < 1 else "FAIL"
            
            self.results.append({
                'check': f'Validity - {column}',
                'status': status,
                'details': f"{invalid_count} valeurs invalides ({invalid_pct:.2f}%)",
                'score': max(0, 100 - invalid_pct * 10)
            })
            
    def check_duplicates(self, df):
        """Vérifie les doublons"""
        duplicate_count = df.duplicated().sum()
        duplicate_pct = (duplicate_count / len(df)) * 100
        threshold = self.config['consistency']['duplicate_threshold']
        
        status = "PASS" if duplicate_pct <= threshold else "WARNING"
        
        self.results.append({
            'check': 'Duplicates',
            'status': status,
            'details': f"{duplicate_count} doublons ({duplicate_pct:.2f}%)",
            'score': max(0, 100 - duplicate_pct * 20)
        })
        
    def check_outliers(self, df):
        """Détecte les outliers dans les colonnes numériques"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
            outlier_pct = (outliers / len(df)) * 100
            
            status = "PASS" if outlier_pct < 5 else "WARNING"
            
            self.results.append({
                'check': f'Outliers - {col}',
                'status': status,
                'details': f"{outliers} outliers ({outlier_pct:.2f}%)",
                'score': max(0, 100 - outlier_pct * 5)
            })
    
    def run_all_checks(self, df):
        """Exécute toutes les vérifications"""
        print("\n🔍 Démarrage des contrôles qualité...\n")
        
        self.check_freshness(df)
        self.check_completeness(df)
        self.check_validity(df)
        self.check_duplicates(df)
        self.check_outliers(df)
        
        # Calcul du score global
        self.score = sum(r['score'] for r in self.results) / len(self.results)
        
        return self.results, self.score
    
    def get_quality_level(self):
        """Retourne le niveau de qualité"""
        thresholds = self.config['thresholds']
        
        if self.score >= thresholds['excellent']:
            return 'Excellent', '🟢'
        elif self.score >= thresholds['good']:
            return 'Bon', '🟡'
        elif self.score >= thresholds['acceptable']:
            return 'Acceptable', '🟠'
        else:
            return 'Faible', '🔴'

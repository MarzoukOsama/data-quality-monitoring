from datetime import datetime
import json

class QualityReporter:
    
    def __init__(self, results, score, dataset_name):
        self.results = results
        self.score = score
        self.dataset_name = dataset_name
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    def generate_html_report(self, output_path):
        """Génère un rapport HTML professionnel"""
        
        # Déterminer le niveau de qualité
        if self.score >= 95:
            level, color, emoji = 'Excellent', '#22c55e', '🟢'
        elif self.score >= 80:
            level, color, emoji = 'Bon', '#eab308', '🟡'
        elif self.score >= 60:
            level, color, emoji = 'Acceptable', '#f97316', '🟠'
        else:
            level, color, emoji = 'Faible', '#ef4444', '🔴'
        
        # Compter les statuts
        pass_count = sum(1 for r in self.results if r['status'] == 'PASS')
        fail_count = sum(1 for r in self.results if r['status'] == 'FAIL')
        warning_count = sum(1 for r in self.results if r['status'] == 'WARNING')
        
        # Générer les lignes du tableau
        rows = ""
        for result in self.results:
            status_color = {
                'PASS': '#22c55e',
                'FAIL': '#ef4444',
                'WARNING': '#f97316'
            }.get(result['status'], '#gray')
            
            rows += f"""
            <tr>
                <td style="padding: 12px; border-bottom: 1px solid #e5e7eb;">{result['check']}</td>
                <td style="padding: 12px; border-bottom: 1px solid #e5e7eb;">
                    <span style="background: {status_color}; color: white; padding: 4px 12px; border-radius: 12px; font-weight: bold; font-size: 12px;">
                        {result['status']}
                    </span>
                </td>
                <td style="padding: 12px; border-bottom: 1px solid #e5e7eb;">{result['details']}</td>
                <td style="padding: 12px; border-bottom: 1px solid #e5e7eb; text-align: center; font-weight: bold;">
                    {result['score']:.1f}%
                </td>
            </tr>
            """
        
        html = f"""
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Rapport Qualité des Données - {self.dataset_name}</title>
            <style>
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: #f3f4f6;
                    padding: 20px;
                }}
                .container {{
                    max-width: 1200px;
                    margin: 0 auto;
                    background: white;
                    border-radius: 12px;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    overflow: hidden;
                }}
                .header {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 40px;
                    text-align: center;
                }}
                .header h1 {{
                    font-size: 32px;
                    margin-bottom: 10px;
                }}
                .header p {{
                    opacity: 0.9;
                }}
                .score-section {{
                    display: flex;
                    justify-content: space-around;
                    padding: 30px;
                    background: #fafafa;
                    border-bottom: 2px solid #e5e7eb;
                }}
                .score-card {{
                    text-align: center;
                    padding: 20px;
                    background: white;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                    flex: 1;
                    margin: 0 10px;
                }}
                .score-value {{
                    font-size: 48px;
                    font-weight: bold;
                    color: {color};
                    margin: 10px 0;
                }}
                .score-label {{
                    color: #6b7280;
                    font-size: 14px;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                }}
                .stats {{
                    display: flex;
                    justify-content: center;
                    gap: 30px;
                    margin-top: 15px;
                }}
                .stat-item {{
                    text-align: center;
                }}
                .stat-number {{
                    font-size: 24px;
                    font-weight: bold;
                }}
                .stat-number.pass {{ color: #22c55e; }}
                .stat-number.fail {{ color: #ef4444; }}
                .stat-number.warning {{ color: #f97316; }}
                .content {{
                    padding: 40px;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }}
                th {{
                    background: #f9fafb;
                    padding: 12px;
                    text-align: left;
                    font-weight: 600;
                    color: #374151;
                    border-bottom: 2px solid #e5e7eb;
                }}
                .footer {{
                    background: #f9fafb;
                    padding: 20px;
                    text-align: center;
                    color: #6b7280;
                    font-size: 14px;
                    border-top: 1px solid #e5e7eb;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>📊 Rapport Qualité des Données</h1>
                    <p>Dataset: <strong>{self.dataset_name}</strong></p>
                    <p>Généré le {self.timestamp}</p>
                </div>
                
                <div class="score-section">
                    <div class="score-card">
                        <div class="score-label">Score Global de Qualité</div>
                        <div class="score-value">{emoji} {self.score:.1f}%</div>
                        <div style="font-size: 18px; color: {color}; font-weight: bold; margin-top: 10px;">
                            {level}
                        </div>
                    </div>
                    
                    <div class="score-card">
                        <div class="score-label">Résumé des Contrôles</div>
                        <div class="stats">
                            <div class="stat-item">
                                <div class="stat-number pass">{pass_count}</div>
                                <div style="font-size: 12px; color: #6b7280;">PASS</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-number warning">{warning_count}</div>
                                <div style="font-size: 12px; color: #6b7280;">WARNING</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-number fail">{fail_count}</div>
                                <div style="font-size: 12px; color: #6b7280;">FAIL</div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="content">
                    <h2 style="margin-bottom: 20px; color: #1f2937;">Détails des Contrôles</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Contrôle</th>
                                <th>Statut</th>
                                <th>Détails</th>
                                <th style="text-align: center;">Score</th>
                            </tr>
                        </thead>
                        <tbody>
                            {rows}
                        </tbody>
                    </table>
                </div>
                
                <div class="footer">
                    <p>🔍 Data Quality Monitoring System | Développé par Oussama Marzouk</p>
                    <p style="margin-top: 5px;">Ce rapport a été généré automatiquement</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✅ Rapport HTML généré: {output_path}")
        
    def print_console_summary(self):
        """Affiche un résumé dans la console"""
        print("\n" + "="*70)
        print("📊 RÉSUMÉ DU CONTRÔLE QUALITÉ")
        print("="*70)
        print(f"\n📁 Dataset: {self.dataset_name}")
        print(f"🕐 Timestamp: {self.timestamp}")
        print(f"\n🎯 Score global: {self.score:.1f}%")
        
        # Déterminer le niveau
        if self.score >= 95:
            level, emoji = 'Excellent', '🟢'
        elif self.score >= 80:
            level, emoji = 'Bon', '🟡'
        elif self.score >= 60:
            level, emoji = 'Acceptable', '🟠'
        else:
            level, emoji = 'Faible', '🔴'
            
        print(f"📈 Niveau: {emoji} {level}\n")
        
        # Tableau des résultats
        print(f"{'Contrôle':<30} {'Statut':<10} {'Score':<10}")
        print("-" * 70)
        
        for result in self.results:
            status_emoji = {
                'PASS': '✅',
                'FAIL': '❌',
                'WARNING': '⚠️'
            }.get(result['status'], '❔')
            
            print(f"{result['check']:<30} {status_emoji} {result['status']:<8} {result['score']:>6.1f}%")
        
        print("\n" + "="*70 + "\n")

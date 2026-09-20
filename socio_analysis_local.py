

import os
import json
import datetime
import re
from typing import Dict, List, Any
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================================
# 1. SOZIALWISSENSCHAFTLICHE WISSENSBASIS & LEXIKA
# =====================================================================

AXIOLOGY_LEXICON = {
    "Fürsorge / Vulnerabilität": [
        "schutz", "hilfe", "prekär", "armut", "ausbeutung", "sorge", "leiden", "gesundheit", "angst"
    ],
    "Gerechtigkeit / Reziprozität": [
        "gerechtigkeit", "ungleichheit", "fairness", "umverteilung", "lohn", "ausgleich", "privileg", "monopol"
    ],
    "Leistung / Meritokratie": [
        "leistung", "wachstum", "effizienz", "wettbewerb", "innovation", "erfolg", "rendite", "markt"
    ],
    "Freiheit / Autonomie": [
        "freiheit", "selbstbestimmung", "flexibilität", "unabhängigkeit", "wahlfreiheit", "unternehmertum"
    ],
    "Ordnung / Kollektiv": [
        "solidarität", "staat", "gewerkschaft", "ordnung", "sicherheit", "regulierung", "kontrolle"
    ]
}

CLEAVAGE_TAXONOMY = [
    {
        "name": "Kapital/Plattform vs. Arbeit/Prekariat",
        "faction_a": "Plattform-Konzerne & Tech-Kapital",
        "faction_b": "Plattform-Arbeiter & Gig-Economy-Prekariat",
        "keywords": ["kapital", "arbeit", "plattform", "prekariat", "ausbeutung", "lohn", "rendite", "monopol"],
        "core_dispute": "Abschöpfung von Mehrwert durch Algorithmen vs. kollektive Arbeitnehmerrechte und soziale Sicherung.",
        "base_salience": 8.8
    },
    {
        "name": "Kognitive Wissenselite vs. Routine-Beschäftigte",
        "faction_a": "Symbolanalytiker & KI-Entwickler",
        "faction_b": "Qualifizierte Angestellte & Sachbearbeiter",
        "keywords": ["ki", "automatisierung", "wissensarbeit", "ersetzung", "qualifikation", "effizienz", "rationalisierung"],
        "core_dispute": "Entwertung traditioneller akademischer Qualifikationen und Büroarbeit durch automatisierte Wissensgenerierung.",
        "base_salience": 7.9
    },
    {
        "name": "Marktliberale Dynamik vs. Staatliche Regulierung",
        "faction_a": "Techno-Optimisten & Startups",
        "faction_b": "Regulierungsbehörden & Gewerkschaften",
        "keywords": ["regulierung", "gesetz", "staat", "innovation", "wettbewerb", "freiheit", "eu-ai-act"],
        "core_dispute": "Geschwindigkeit des technologischen Wandels vs. demokratische Einhegung und Arbeitsschutz.",
        "base_salience": 7.2
    }
]

# =====================================================================
# 2. DIE LOKALEN AGENTEN
# =====================================================================

class LocalSocioAnalysisSystem:
    def __init__(self, topic: str):
        self.topic = topic
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.state: Dict[str, Any] = {
            "topic": topic,
            "timestamp": self.timestamp,
            "trends": [],
            "conflicts": [],
            "moral_frames": [],
            "report_path": "",
            "chart_path": ""
        }

    def agent_macro_trends(self):
        """Agent 1: Berechnet historische Trend-Trajektorien deterministisch."""
        print("[Agent 1: Macro-Trend Analyst] Berechne historische Trajektorien...")
        
        # Drei universelle Makro-Trends bezogen auf Technologie & Arbeitswelt
        self.state["trends"] = [
            {
                "name": "Plattformisierung & Prekarisierung",
                "description": "Verschiebung von Normalarbeitsverhältnissen hin zu algorithmisch vermittelter Abrufarbeit.",
                "trajectory": [
                    {"decade_or_year": "2000", "intensity": 0.15},
                    {"decade_or_year": "2010", "intensity": 0.40},
                    {"decade_or_year": "2020", "intensity": 0.72},
                    {"decade_or_year": "2026", "intensity": 0.90}
                ]
            },
            {
                "name": "Kognitive Automatisierung (Generative KI)",
                "description": "Subsumtion nicht-routinierter Kopfarbeit unter maschinelle Text- und Codegenerierung.",
                "trajectory": [
                    {"decade_or_year": "2000", "intensity": 0.05},
                    {"decade_or_year": "2010", "intensity": 0.18},
                    {"decade_or_year": "2020", "intensity": 0.45},
                    {"decade_or_year": "2026", "intensity": 0.96}
                ]
            },
            {
                "name": "Subjektivierung & Leistungsverdichtung",
                "description": "Auflösung fester Arbeitsgrenzen; ständige Selbstoptimierung unter digitaler Kontrolle.",
                "trajectory": [
                    {"decade_or_year": "2000", "intensity": 0.35},
                    {"decade_or_year": "2010", "intensity": 0.58},
                    {"decade_or_year": "2020", "intensity": 0.78},
                    {"decade_or_year": "2026", "intensity": 0.86}
                ]
            }
        ]

    def agent_cleavages(self):
        """Agent 2: Ermittelt relevante gesellschaftliche Bruchlinien (Cleavages)."""
        print("[Agent 2: Cleavage Analyst] Mappe Konfliktlinien...")
        
        topic_lower = self.topic.lower()
        conflicts = []
        
        for c in CLEAVAGE_TAXONOMY:
            # Relevanzgewichtung basierend auf Treffern im Thema
            score = c["base_salience"]
            hits = sum(1 for kw in c["keywords"] if kw in topic_lower)
            adjusted_score = min(10.0, score + (hits * 0.4))
            
            conflicts.append({
                "name": c["name"],
                "faction_a": c["faction_a"],
                "faction_b": c["faction_b"],
                "core_dispute": c["core_dispute"],
                "salience_score": round(adjusted_score, 1)
            })
            
        self.state["conflicts"] = conflicts

    def agent_moral_axiology(self):
        """Agent 3: Rekonstruiert moralische Werturteile und wechselseitige Delegitimierung."""
        print("[Agent 3: Axiology Analyst] Rekonstruiere moralische Legitimationsmuster...")
        
        moral_frames = []
        for conflict in self.state["conflicts"]:
            c_name = conflict["name"]
            
            if "Plattform" in c_name:
                moral_frames.append({
                    "conflict_reference": c_name,
                    "faction": conflict["faction_a"],
                    "core_value": "Freiheit, Effizienz & Marktflexibilität",
                    "moral_judgment": "Bezeichnet Gewerkschaften als innovationsfeindlich und rückwärtsgewandt."
                })
                moral_frames.append({
                    "conflict_reference": c_name,
                    "faction": conflict["faction_b"],
                    "core_value": "Fürsorge, Schutz vor Ausbeutung & Fairness",
                    "moral_judgment": "Kritisiert Konzerne als unsozial, ausbeuterisch und parasitär."
                })
            elif "Wissenselite" in c_name:
                moral_frames.append({
                    "conflict_reference": c_name,
                    "faction": conflict["faction_a"],
                    "core_value": "Technologische Progression & Meritokratie",
                    "moral_judgment": "Deutet Sorgen der Beschäftigten als mangelnde Anpassungs- und Lernbereitschaft."
                })
                moral_frames.append({
                    "conflict_reference": c_name,
                    "faction": conflict["faction_b"],
                    "core_value": "Anerkennung geleisteter Lebensarbeit & Menschenwürde",
                    "moral_judgment": "Wirft Tech-Eliten Elfenbeinturm-Mentalität und Entmenschlichung der Arbeit vor."
                })
            else:
                moral_frames.append({
                    "conflict_reference": c_name,
                    "faction": conflict["faction_a"],
                    "core_value": "Entfaltungsfreiheit & Globaler Wettbewerb",
                    "moral_judgment": "Brandmarkt Regulierungen als bürokratische Innovationsblockaden."
                })
                moral_frames.append({
                    "conflict_reference": c_name,
                    "faction": conflict["faction_b"],
                    "core_value": "Demokratische Souveränität & Kollektive Sicherheit",
                    "moral_judgment": "Wirft Technologie-Treiber Verantwortungslosigkeit gegenüber der Allgemeinheit vor."
                })

        self.state["moral_frames"] = moral_frames

    def agent_visualizer_persister(self):
        """Agent 4: Erstellt Diagramme, Markdown-Tabellen und speichert zeitgestempelt."""
        print("[Agent 4: Visualizer & Archivist] Speichere Daten und generiere Diagramme...")
        
        output_dir = os.path.join("sociological_runs", self.timestamp)
        os.makedirs(output_dir, exist_ok=True)
        
        # 1. Kurvendiagramm erstellen
        sns.set_theme(style="whitegrid")
        plt.figure(figsize=(10, 5))
        
        palette = sns.color_palette("deep", len(self.state["trends"]))
        for i, trend in enumerate(self.state["trends"]):
            years = [p["decade_or_year"] for p in trend["trajectory"]]
            vals = [p["intensity"] for p in trend["trajectory"]]
            plt.plot(years, vals, marker='o', linewidth=2.5, label=trend["name"], color=palette[i])
            
        plt.title(f"Gegenwartsanalyse: Trajektorien dominanter Makro-Trends\nThema: {self.topic}", fontsize=12, fontweight="bold")
        plt.xlabel("Zeithorizont", fontsize=10)
        plt.ylabel("Relative Hegemonie / Intensität (0.0 - 1.0)", fontsize=10)
        plt.ylim(-0.05, 1.05)
        plt.legend(loc="upper left")
        plt.tight_layout()
        
        chart_file = os.path.join(output_dir, "trend_trajectories.png")
        plt.savefig(chart_file, dpi=200)
        plt.close()

        # 2. Markdown-Report mit Tabellen
        report_file = os.path.join(output_dir, "analysis_report.md")
        df_conflicts = pd.DataFrame(self.state["conflicts"])
        conflict_table_md = df_conflicts[["name", "faction_a", "faction_b", "salience_score", "core_dispute"]].to_markdown(index=False)
        
        df_moral = pd.DataFrame(self.state["moral_frames"])
        moral_table_md = df_moral.to_markdown(index=False)

        report_content = f"""# Sozialwissenschaftliche Gegenwartsanalyse (Lokaler Run)
**Gegenstand:** {self.topic}  
**Datum & Uhrzeit:** {self.timestamp}  
**Methode:** Lokales Cleavage-Mapping, Trend-Trajektorien & Axiologische Rekonstruktion

---

## 1. Makro-Trends & Entwicklungskurven
Die visualisierten Intensitätskurven wurden in `trend_trajectories.png` gespeichert.

| Trend | Kerncharakteristik |
| :--- | :--- |
"""
        for t in self.state["trends"]:
            report_content += f"| **{t['name']}** | {t['description']} |\n"

        report_content += f"""
---

## 2. Strukturelle Konfliktlinien (Cleavages)
{conflict_table_md}

---

## 3. Moralische Werturteile & Wertkonflikte
{moral_table_md}
"""
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(report_content)
            
        with open(os.path.join(output_dir, "raw_state.json"), "w", encoding="utf-8") as f:
            json.dump(self.state, f, ensure_ascii=False, indent=2)

        self.state["report_path"] = report_file
        self.state["chart_path"] = chart_file
        print(f"[Agent 4] Abgeschlossen. Dateien abgelegt in: {output_dir}")

    def run(self):
        print("\n" + "="*60)
        print(f"STARTE LOKALE ANALYSE: {self.topic}")
        print(f"ZEITSTEMPEL:          {self.timestamp}")
        print("="*60)
        
        self.agent_macro_trends()
        self.agent_cleavages()
        self.agent_moral_axiology()
        self.agent_visualizer_persister()
        
        return self.state


if __name__ == "__main__":
    fragestellung = "Die Transformation der Arbeitswelt durch generative KI und Plattformkapitalismus"
    system = LocalSocioAnalysisSystem(fragestellung)
    result = system.run()
    
    print("\n[Fertiggestellt]")
    print(f"Report:  {result['report_path']}")
    print(f"Diagramm: {result['chart_path']}")
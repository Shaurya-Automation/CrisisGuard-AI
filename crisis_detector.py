import pandas as pd
import numpy as np
from datetime import datetime
import random

class WatcherAgent:
    """Scans data sources for crisis keywords."""
    def __init__(self):
        self.keywords = ["flood", "earthquake", "heatwave", "storm", "fire", "cyclone"]
    
    def scan(self, data_source):
        # Simulates scanning social feeds or weather APIs
        potential_crisis = []
        for idx, row in data_source.iterrows():
            if any(kw in str(row['source_text']).lower() for kw in self.keywords):
                potential_crisis.append(row)
        return potential_crisis

class AnalystAgent:
    """Analyzes threats, calculates risk scores, and determines sentiment."""
    def __init__(self):
        self.risk_weights = {"flood": 0.9, "earthquake": 0.95, "heatwave": 0.7, "storm": 0.85, "fire": 0.8, "cyclone": 0.9}
    
    def analyze(self, data_points):
        analysis_results = []
        for point in data_points:
            risk_score = 0
            sentiment = "neutral"
            threat_level = "Low"
            
            # Simple logic to simulate AI reasoning
            if "heat" in str(point).lower() or "high temp" in str(point).lower():
                risk_score = 0.75
                sentiment = "negative"
                threat_level = "Medium"
            elif any(kw in str(point).lower() for kw in ["flood", "earthquake", "cyclone"]):
                risk_score = 0.95
                sentiment = "critical"
                threat_level = "Critical"
            else:
                risk_score = 0.4
                sentiment = "neutral"
                threat_level = "Low"
            
            analysis_results.append({
                "timestamp": datetime.now().isoformat(),
                "location": point.get('location', 'Unknown'),
                "threat_level": threat_level,
                "risk_score": risk_score,
                "sentiment": sentiment,
                "source": point.get('source', 'Simulated')
            })
        return analysis_results

class ReporterAgent:
    """Generates alerts and logs events."""
    def __init__(self):
        self.alert_log = []
    
    def report(self, analysis_data):
        for item in analysis_data:
            action = "MONITORING"
            if item['threat_level'] == "Critical":
                action = "ALERT_SENT"
            elif item['threat_level'] == "Medium":
                action = "WARNING_ISSUED"
            
            event_log = {
                **item,
                "action_taken": action,
                "response_time": f"{random.randint(1, 5)}s"
            }
            self.alert_log.append(event_log)
        return self.alert_log

def run_crisis_pipeline(data_df):
    watcher = WatcherAgent()
    analyst = AnalystAgent()
    reporter = ReporterAgent()
    
    # 1. Watcher scans
    flagged = watcher.scan(data_df)
    
    # 2. Analyst reasons
    analyzed = analyst.analyze(flagged)
    
    # 3. Reporter acts
    final_logs = reporter.report(analyzed)
    
    return pd.DataFrame(final_logs)
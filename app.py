import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==========================================
# CRISIS GUARD AI DASHBOARD
# ==========================================

st.set_page_config(page_title="CrisisGuard AI Dashboard", layout="wide")

st.title("🛡️ CrisisGuard AI: Multi-Agent Monitoring System")
st.markdown("""
**Real-time crisis detection powered by 3 autonomous agents:**  
- 📡 **Watcher:** Scans social feeds  
- 🧠 **Analyst:** Detects threats & reasons context  
- 📢 **Reporter:** Alerts & logs critical events  
""")

# Check if log file exists
log_file = "crisis_log.csv"

if not os.path.exists(log_file):
    st.warning("⚠️ No data found. Run `python main.py` first to generate the log.")
    st.stop()

# Load the data
try:
    df = pd.read_csv(log_file)
    # Convert timestamp to datetime for sorting
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df = df.sort_values(by='Timestamp', ascending=False)
except Exception as e:
    st.error(f"Error reading log file: {e}")
    st.stop()

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filters")
threat_filter = st.sidebar.multiselect(
    "Threat Level",
    options=df["ThreatLevel"].unique(),
    default=df["ThreatLevel"].unique()
)

source_filter = st.sidebar.multiselect(
    "Source",
    options=df["Source"].unique(),
    default=df["Source"].unique()
)

# Apply filters
df_selection = df.query(
    "ThreatLevel == @threat_filter and Source == @source_filter"
)

# --- MAIN DASHBOARD METRICS ---
st.header("📊 System Overview")
col1, col2, col3 = st.columns(3)

total_alerts = len(df_selection[df_selection["Action"] == "ALERT_SENT"])
total_monitored = len(df_selection[df_selection["Action"] == "MONITORING"])
avg_sentiment = df_selection["Sentiment"].mean() if not df_selection.empty else 0

col1.metric("🚨 Critical Alerts", total_alerts, delta="Active")
col2.metric("⚠️ Monitored Events", total_monitored, delta="Tracking")
col3.metric("📉 Avg. Sentiment Score", f"{avg_sentiment:.2f}", delta="Negative" if avg_sentiment < 0 else "Neutral")

# --- LIVE AGENT FEED ---
st.header("📡 Live Agent Activity Log")

# Style the dataframe for better readability
def highlight_threat(row):
    if row['ThreatLevel'] == 'HIGH':
        return ['background-color: #ff4444; color: white'] * len(row)
    elif row['ThreatLevel'] == 'MEDIUM':
        return ['background-color: #ffcc00; color: black'] * len(row)
    else:
        return [''] * len(row)

st.dataframe(
    df_selection.style.apply(highlight_threat, axis=1),
    use_container_width=True,
    hide_index=True
)

# --- AGENT EXPLANATION SECTION ---
with st.expander("🤖 How the Agents Work (Technical Details)"):
    st.markdown("""
    **1. Watcher Agent**: Fetches raw data from social feeds (simulated here).
    **2. Analyst Agent**: Runs sentiment analysis and keyword matching to determine `ThreatLevel`.
    **3. Reporter Agent**: Decides whether to `ALERT_SENT`, `MONITORING`, or `IGNORE` based on thresholds.
    
    *This multi-agent architecture ensures autonomous decision-making without human intervention.*
    """)

# --- FOOTER ---
st.markdown("---")
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | CrisisGuard AI Capstone Project")

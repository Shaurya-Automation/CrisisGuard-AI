# 🚨 CrisisGuard AI: Real-Time Crisis Detection

> **A Python-native, multi-agent system for detecting local crises in under 2 seconds.**  
> *Built for the Kaggle "Agents for Social Good" Capstone.*

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 🌍 The Problem
Mainstream news and enterprise tools (like Everbridge) are too slow or expensive for NGOs in developing regions. Critical information about floods, earthquakes, or conflicts often takes hours to reach first responders.

## ⚡ The Solution
**CrisisGuard AI** is a zero-cost, self-hosted system that monitors local news feeds and social signals using 3 autonomous Python agents:
1.  **Watcher:** Scans RSS feeds and social streams.
2.  **Analyst:** Validates and prioritizes threats using NLP.
3.  **Reporter:** Generates instant alerts for NGOs.

**No n8n. No Make.com. No Vendor Lock-in.**

## ✨ Key Features
- **⚡ Real-Time:** Detects crises in < 2 seconds.
- **🛡️ Zero Cost:** Runs on free-tier infrastructure (Hugging Face Spaces).
- **📊 Live Dashboard:** Interactive Streamlit UI for monitoring.
- **🌍 Social Good:** Designed for NGOs in resource-constrained areas.

## 🛠️ Tech Stack
- **Language:** Python 3.9+
- **Frontend:** Streamlit
- **Data:** Pandas, Requests
- **Agents:** Custom Python logic (No external workflow builders)

## 📦 Installation & Run

### Method: 💻 Local Development
1. Clone the repo:
   ```bash
   git clone https://github.com/Shaurya-Automation/CrisisGuard_AI.git
   cd CrisisGuard_AI
   pip install -r requirements.txt
   streamlit run app.py

📸 Screenshots
Dashboard Overview- (in the file named 'Live_Dashboard_Overview.png')

Crisis Check Table- (in the file named 'Agent Logic & Data Processing.png')

🎯 Use Cases
NGOs: Rapid response coordination during disasters.
Journalists: Real-time fact-checking and source verification.
Citizens: Early warning systems for local emergencies.

🤝 Contributing
This project is open source for social good. Feel free to fork, improve, and deploy!

📜 License
MIT License. See LICENSE (in files) for details.

## Credits
- **Developer**: [Shaurya Bisht] (AI Workflow Automation, Python/Streamlit)
- **Research Support**: [Rama Kruthi Sarvaraju] (Crisis data validation, testing)
- **Built for**: Kaggle "Agents for Social Good" Capstone

import streamlit as st
import feedparser
import csv
from datetime import datetime

# --- AGENT 1: WATCHER ---
@st.cache_data
def fetch_videos(channel_id):
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    try:
        feed = feedparser.parse(url)
        return [{"title": entry.title, "desc": entry.get("summary", "")} for entry in feed.entries[:5]]
    except:
        return []

# --- AGENT 2: ANALYST ---
def analyze_crisis(text):
    crisis_words = ["scam", "fraud", "fake", "stolen", "banned", "hacked", "cancelled"]
    score = sum(2 if word in text.lower() else 0 for word in crisis_words)
    return min(score, 10)

# --- AGENT 3: REPORTER ---
def log_crisis(video_id, title, score, keyword):
    with open("crisis_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        # Check if file exists to write header only once
        if f.tell() == 0:
            writer.writerow(["timestamp", "video_id", "keyword", "severity", "status"])
        status = "CRITICAL" if score >= 7 else "SAFE"
        writer.writerow([datetime.now(), video_id, keyword, score, status])

# --- UI ---
st.title("🚨 CrisisGuard AI: Multi-Agent Dashboard")
st.markdown("### Real-time YouTube Crisis Monitor")

channel_id = st.text_input("Enter YouTube Channel ID (e.g., UCkRfGmb...):")

if st.button("Scan for Crises"):
    if channel_id:
        with st.spinner("Agents scanning..."):
            videos = fetch_videos(channel_id)
            if not videos:
                st.error("No videos found or invalid Channel ID.")
            else:
                st.success(f"👀 Watcher: Found {len(videos)} videos.")
                
                for i, vid in enumerate(videos):
                    score = analyze_crisis(vid["title"] + " " + vid["desc"])
                    keyword = "None"
                    # Simple keyword extraction for demo
                    if score > 0:
                        for w in ["scam", "fraud", "fake", "stolen", "banned", "hacked", "cancelled"]:
                            if w in vid["title"].lower():
                                keyword = w
                                break
                    
                    st.subheader(f"Video {i+1}: {vid['title'] [:50]}...")
                    st.metric("Crisis Score", score)
                    
                    if score >= 7:
                        st.error("🚨 ALERT: High Crisis Score!")
                        log_crisis(f"vid_{i}", vid["title"], score, keyword)
                    else:
                        st.info("✅ Safe")
                
                st.warning("Check 'crisis_log.csv' for the full report.")
    else:
        st.warning("Please enter a Channel ID.")
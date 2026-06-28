import os
import feedparser
import streamlit as st

# Set page config
st.set_page_config(page_title="CrisisGuard AI", page_icon="⚠️")

st.title("⚠️ CrisisGuard AI: YouTube Crisis Detector")
st.markdown("Paste a **YouTube Channel ID** (e.g., `UCsXVk37bltHxD1rDPwtNM8Q`) below.")

# Input handling
channel_id = st.text_input("Channel ID", placeholder="UCsXVk37bltHxD1rDPwtNM8Q")

if st.button("Analyze for Crisis"):
    if not channel_id:
        st.error("Please enter a Channel ID.")
    else:
        # 1. CLEAN THE INPUT (Crucial for HF Spaces)
        clean_id = channel_id.strip().replace('"', '').replace("'", "")
        
        rss_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={clean_id}"
        
        with st.spinner(f"Fetching feed for {clean_id}..."):
            try:
                # 2. FETCH FEED
                feed = feedparser.parse(rss_url)
                
                # 3. DEBUGGING: Check for errors
                if feed.bozo:
                    st.error(f"Feed Error: {feed.bozo_exception}")
                    st.write(f"URL tried: {rss_url}")
                    st.stop()
                
                if not feed.entries:
                    st.error("No videos found.")
                    st.write("Possible reasons:")
                    st.write("- Invalid Channel ID.")
                    st.write("- The channel is private or has no videos.")
                    st.write("- The RSS feed is temporarily unavailable.")
                    st.stop()

                # 4. ANALYZE
                st.success(f"Found {len(feed.entries)} recent videos.")
                
                crisis_keywords = ["scam", "fraud", "ban", "controversy", "canceled", "lawsuit", "apology", "debt", "scandal"]
                crisis_detected = False
                crisis_videos = []

                for entry in feed.entries[:10]: # Check last 10 videos

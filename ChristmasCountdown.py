import streamlit as st
from datetime import datetime
import time

st.title("⏰ Countdown Timer")

# Let user pick a target date and time
col1, col2 = st.columns(2)
with col1:
    target_date = st.date_input("Target Date", value=datetime(2025, 12, 25))
with col2:
    target_time = st.time_input("Target Time", value=datetime.strptime("10:00", "%H:%M").time())

# Combine date and time
target_datetime = datetime.combine(target_date, target_time)

# Placeholder for the countdown display
countdown_placeholder = st.empty()
status_placeholder = st.empty()

# Start button
if st.button("Start Countdown"):
    now = datetime.now()
    
    if target_datetime <= now:
        st.error("⚠️ Target date/time must be in the future!")
    else:
        while target_datetime > datetime.now():
            now = datetime.now()
            diff = target_datetime - now
            
            days = diff.days
            hours, remainder = divmod(diff.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            
            countdown_placeholder.markdown(
                f"## 🕐 {days}d {hours}h {minutes}m {seconds}s"
            )
            status_placeholder.progress(
                min(1.0, 1 - (diff.total_seconds() / max((target_datetime - datetime.now()).total_seconds(), 1)))
            )
            time.sleep(1)
        
        countdown_placeholder.markdown("## 🎉 Done!")
        st.balloons()

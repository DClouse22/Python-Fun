import streamlit as st
from datetime import datetime
import time

st.title("🎄 Christmas Countdown")

# Get current year
current_year = datetime.now().year

# Let user select this year or next year
year_option = st.radio(
    "Select Christmas Year:",
    options=["This Year", "Next Year"],
    horizontal=True
)

# Determine the target year based on selection
if year_option == "This Year":
    target_year = current_year
else:
    target_year = current_year + 1

# Set target to Christmas Day at midnight
target_datetime = datetime(target_year, 12, 25, 0, 0, 0)

st.write(f"**Counting down to:** December 25, {target_year}")

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
        
        countdown_placeholder.markdown("## 🎄🎅 Merry Christmas! 🎁🎉")
        st.balloons()
        st.snow()

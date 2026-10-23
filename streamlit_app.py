# Import necessary packages (Make sure to also include in "requirements.txt" in this repository.)
import streamlit as st
import pandas as pd

# Print Title for the App
st.title("Microsoft Stock Data Dashboard by Coen He")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository) 
df = pd.read_csv("msft.csv")

# Set up the 4 tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart", "* Fun Tab"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for MSFT")
    st.dataframe(df, use_container_width=True)

# Tab 2: Closing Price Chart
with tabs[1]:
    st.subheader(f"Closing Price for MSFT")
    st.line_chart(df['Close'])

# Tab 3: Volume Chart
with tabs[2]:
    st.subheader(f"Volume for MSFT")
    st.bar_chart(df['Volume'])

# Tab 4: Volume Chart
with tabs[3]:
    st.subheader(f"Something New - Live Digital Clock EST")
    from datetime import datetime
    import time
    from zoneinfo import ZoneInfo  # Available in Python 3.9+
    import streamlit as st
    eastern_tz = ZoneInfo("America/New_York")
    clock_placeholder = st.empty()
    while True:
      now_eastern = datetime.now(eastern_tz)
        current_time = now_eastern.strftime("%H:%M:%S")
        current_date = now_eastern.strftime("%A, %B %d, %Y")
    clock_placeholder.markdown(
      f"""
        <div style="font-size: 40px; font-weight: bold; text-align: center; padding: 20px; border: 2px solid #4CAF50; border-radius: 10px;">
            {current_time}
            <div style="font-size: 16px; color: gray; font-weight: normal;">{current_date} (ET)</div>
        </div>
        """,
      unsafe_allow_html=True,
  )

  time.sleep(1)

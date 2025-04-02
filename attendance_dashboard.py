import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Attendance Dashboard", layout="wide")
st.title("📋 Face Recognition Attendance Dashboard")

CSV_FILE = "attendance.csv"

# Load the CSV
if not os.path.exists(CSV_FILE):
    st.warning(f"No attendance log found at `{CSV_FILE}`.")
    st.stop()

df = pd.read_csv(CSV_FILE)

# Filters
st.sidebar.header("🔍 Filters")
names = df["Name"].unique()
selected_name = st.sidebar.selectbox("Select Name", options=["All"] + sorted(names.tolist()))

dates = df["Date"].unique()
selected_date = st.sidebar.selectbox("Select Date", options=["All"] + sorted(dates.tolist()))

# Apply filters
filtered_df = df.copy()
if selected_name != "All":
    filtered_df = filtered_df[filtered_df["Name"] == selected_name]
if selected_date != "All":
    filtered_df = filtered_df[filtered_df["Date"] == selected_date]

st.subheader("📑 Attendance Records")
st.dataframe(filtered_df, use_container_width=True)

# Summary stats
st.subheader("📊 Summary")
st.markdown(f"- **Total Entries:** {len(filtered_df)}")
st.markdown(f"- **Unique People:** {filtered_df['Name'].nunique()}")
st.markdown(f"- **Dates Covered:** {filtered_df['Date'].nunique()}")

# Optional: plot attendance count per person
st.subheader("📈 Attendance Frequency")
count_plot = filtered_df["Name"].value_counts()
st.bar_chart(count_plot)

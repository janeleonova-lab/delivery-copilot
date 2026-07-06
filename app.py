import streamlit as st
import pandas as pd

st.set_page_config(page_title="Delivery Copilot", layout="wide")
st.title("🚦 Delivery Copilot")
st.caption("Predicts timelines, assigns owners, and simulates delivery scenarios")

# --- Load data ---
tasks = pd.read_csv("historical_tasks.csv")
team = pd.read_csv("team.csv")

st.subheader("📊 Historical delivery data")
st.write(f"{len(tasks)} past tasks · avg overrun: "
         f"{(tasks.actual_days / tasks.estimated_days).mean():.0%} of estimate")
st.dataframe(tasks, use_container_width=True)

st.subheader("👥 Team")
st.dataframe(team, use_container_width=True)

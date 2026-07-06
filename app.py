import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Delivery Copilot", layout="wide")
st.title("🚦 Delivery Copilot")
st.caption("Predicts timelines, assigns owners, and simulates delivery scenarios")

# --- Load data ---
tasks = pd.read_csv("historical_tasks.csv")
team = pd.read_csv("team.csv")
tasks["overrun_ratio"] = tasks.actual_days / tasks.estimated_days

# --- Learn overrun patterns ---
# ratio per task_type x complexity; fall back to complexity-only, then global
ratio_by_segment = tasks.groupby(["task_type", "complexity"]).overrun_ratio.mean()
ratio_by_complexity = tasks.groupby("complexity").overrun_ratio.mean()
global_ratio = tasks.overrun_ratio.mean()

def predict_days(task_type, complexity, estimate):
    if (task_type, complexity) in ratio_by_segment.index:
        ratio = ratio_by_segment[(task_type, complexity)]
    elif complexity in ratio_by_complexity.index:
        ratio = ratio_by_complexity[complexity]
    else:
        ratio = global_ratio
    return estimate * ratio, ratio

# --- Sidebar: what the model learned ---
with st.sidebar:
    st.header("🧠 What the model learned")
    st.write("Avg overrun by segment (actual ÷ estimate):")
    st.dataframe(ratio_by_segment.round(2).rename("ratio"))
    st.caption("Backend & Mobile high-complexity work slips the most — "
               "estimates are systematically optimistic.")

# --- Section 1: Timeline prediction ---
st.header("1️⃣ Predict a task timeline")

col1, col2, col3 = st.columns(3)
with col1:
    new_type = st.selectbox("Task type", sorted(tasks.task_type.unique()))
with col2:
    new_complexity = st.selectbox("Complexity", ["Low", "Medium", "High"])
with col3:
    new_estimate = st.number_input("Engineer's estimate (days)", 1, 60, 5)

predicted, ratio = predict_days(new_type, new_complexity, new_estimate)

c1, c2, c3 = st.columns(3)
c1.metric("Engineer's estimate", f"{new_estimate} days")
c2.metric("Learned overrun ratio", f"×{ratio:.2f}")
c3.metric("AI-predicted duration", f"{predicted:.1f} days",
          delta=f"+{predicted - new_estimate:.1f} days vs estimate",
          delta_color="inverse")

st.info("💡 The model learns each segment's estimate-vs-actual ratio from history. "
        "With real Jira data, this would retrain continuously as tasks complete.")

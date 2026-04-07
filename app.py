import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Customer Intelligence System", layout="wide")

# --- 1. Load Data ---
@st.cache_data
def load_data():
    return pd.read_csv("data/final_customer_segments.csv")

df = load_data()

# --- 2. Sidebar Controls ---
with st.sidebar:
    st.title("Settings")
    show_raw = st.checkbox("Show Raw Dataset")
    st.markdown("---")
    st.info("This system uses RFM analysis and K-Means clustering to segment customers into 4 behavioral groups.")

# --- 3. Title & Header ---
st.title("🎯 Customer Intelligence System")
st.subheader("Segmentation and Behavioral Insights")
st.markdown("---")

# --- 4. Top-Level Metrics ---
m1, m2, m3 = st.columns(3)
m1.metric("Total Customers", f"{len(df):,}")
m2.metric("Total Segments", df['Segment'].nunique())
m3.metric("Avg Recency (Log)", round(df['Recency_log'].mean(), 2))

st.markdown("---")

# --- 5. Visualizations ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Customer Segment Distribution")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x='Segment', data=df, palette='Set2', ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    st.subheader("Segmentation Visualization (R vs M)")
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='Recency_log', y='Monetary_log', hue='Segment', palette='Set2', data=df, ax=ax2)
    st.pyplot(fig2)

st.markdown("---")

# --- 6. Your Modified Strategic Marketing Roadmap ---
st.subheader("💡 Strategic Marketing Roadmap")

segment_insights = {
    "Champions 💎": {
        "Status": "Your most valuable assets.",
        "Goal": "Maximize lifetime value.",
        "Action": "Offer VIP treatment, early access to new arrivals, and appreciation-based rewards instead of generic discounts."
    },
    "Loyal Customers ⭐": {
        "Status": "The backbone of your revenue.",
        "Goal": "Increase purchase frequency.",
        "Action": "Introduce a point-based loyalty program and use cross-selling strategies to encourage repeat purchases."
    },
    "At Risk ⚠️": {
        "Status": "Losing interest rapidly.",
        "Goal": "Retention and re-activation.",
        "Action": "Launch a targeted win-back campaign with a limited-time discount or reminder email."
    },
    "Potential Customers 🌱": {
        "Status": "New or low-spend users.",
        "Goal": "Convert them into loyal customers.",
        "Action": "Use onboarding offers, product education, and follow-up incentives to build engagement."
    }
}

selected_insight = st.selectbox("Select a segment to view deep-dive strategy", list(segment_insights.keys()))

if selected_insight in segment_insights:
    data = segment_insights[selected_insight]
    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.markdown("#### 🏷️ Current Status")
        st.write(data["Status"])

    with col_b:
        st.markdown("#### 🎯 Primary Goal")
        st.write(data["Goal"])

    with col_c:
        st.markdown("#### 🛠️ Recommended Action")
        st.write(data["Action"])

st.markdown("---")

# --- 7. Final Raw Data Display ---
if show_raw:
    st.subheader("Full Dataset Overview")
    st.dataframe(df)
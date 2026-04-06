import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Customer Intelligence System", layout="wide")

#Load data
df = pd.read_csv("")

#Title
st.title("Customer Intelligence System")
st.subheader("Segmentation and Behaviotal Insights")

# Show Dataset
if st.checkbox("Show raw data"):
    st.write(df.head())

# Segment Distribution
st.subheader("Customer Segment Distribution")
fig, ax = plt.subplots()
df['Segment'].value_counts().plot(kind='bar',ax=ax)
st.pyplot(fig)

# Scatter Plot
st.subheader("Customer Segmentation Visualization")
fig, ax = plt.subplots(figsize=(8,6))
sns.scatterplot(
    x=df['Recency_log'],
    y=df['Monetary_log'],
    hue=df["Segment"],
    palette='Set2',
    ax=ax
)
st.pyplot(fig)

# Segment Insights
st.subheader("Business Insights")
segment = st.selectbox("Select Customer Segment", df['Segment'].unique())


if segment == "Champions 💎":
    st.write("High-value customers. Offer VIP rewards and exclusive deals.")
elif segment == "Loyal Customers ⭐":
    st.write("Frequent buyers. Focus on upselling and loyalty programs.")
elif segment == "At Risk ⚠️":
    st.write("Customers not active recently. Send re-engagement campaigns.")
else:
    st.write("Potential customers. Encourage more purchases with promotions.")
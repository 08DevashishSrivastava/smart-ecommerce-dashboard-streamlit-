import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Analytics Dashboard", layout="wide")

st.title("📊 Sales Analytics Dashboard")

# -------------------------------
# SAMPLE DATA
# -------------------------------
data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Sales": [200, 450, 300, 500, 700, 650, 800],
    "Profit": [50, 120, 80, 150, 200, 180, 250]
})

# -------------------------------
# KPIs (TOP CARDS)
# -------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Total Sales", "₹3,600", "+12%")

with col2:
    st.metric("📈 Profit", "₹1,030", "+8%")

with col3:
    st.metric("🛒 Orders", "120", "+5%")

# -------------------------------
# LINE CHART
# -------------------------------
st.write("### 📈 Sales Trend")

fig1 = px.line(
    data,
    x="Day",
    y="Sales",
    markers=True,
    color_discrete_sequence=["#00ffd5"]
)

st.plotly_chart(fig1, use_container_width=True)

# -------------------------------
# BAR CHART
# -------------------------------
st.write("### 📊 Sales vs Profit")

fig2 = px.bar(
    data,
    x="Day",
    y=["Sales", "Profit"],
    barmode="group",
    color_discrete_sequence=["#ff7e5f", "#00ffd5"]
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------------
# PIE CHART
# -------------------------------
st.write("### 🥧 Sales Distribution")

fig3 = px.pie(
    data,
    names="Day",
    values="Sales",
    color_discrete_sequence=px.colors.sequential.RdBu
)

st.plotly_chart(fig3, use_container_width=True)
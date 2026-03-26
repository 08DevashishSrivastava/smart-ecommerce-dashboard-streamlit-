import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Dev Store", layout="wide")

# -------------------------------
# CUSTOM CSS (DARK PREMIUM UI)
# -------------------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}

/* Card UI */
.card {
    padding: 20px;
    border-radius: 20px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    box-shadow: 0px 0px 20px rgba(0,255,213,0.2);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# TITLE
# -------------------------------
st.title("🛒 Dev E-Commerce Store")
st.write("### Buy Your Favorite Products")

# -------------------------------
# PRODUCT DATA
# -------------------------------
products = {
    "Laptop 💻": 50000,
    "Phone 📱": 20000,
    "Headphones 🎧": 2000,
    "Shoes 👟": 3000
}

if "cart" not in st.session_state:
    st.session_state.cart = []

# -------------------------------
# SHOP SECTION
# -------------------------------
product = st.selectbox("Select Product", list(products.keys()))
quantity = st.number_input("Quantity", min_value=1)

price = products[product]

if st.button("Add to Cart"):
    st.session_state.cart.append((product, price, quantity))
    st.success("Added to cart!")

# -------------------------------
# CART
# -------------------------------
st.write("## 🧾 Your Cart")

total = 0

for item, price, qty in st.session_state.cart:
    total += price * qty
    st.write(f"{item} x {qty} = ₹{price * qty}")

st.write(f"## 💰 Total Amount: ₹{total}")

# -------------------------------
# PREMIUM GRAPH SECTION 🔥
# -------------------------------
st.write("---")
st.write("## 📊 Visual Analytics (Devashish Dashboard)")

col1, col2 = st.columns(2)

# 📈 LINE CHART (LIKE TOP GRAPH)
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("### 📈 Workload Chart")

    df = pd.DataFrame({
        "Day": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        "Workload": [800, 650, 520, 760, 580, 700, 720]
    })

    fig = px.line(df, x="Day", y="Workload",
                  line_shape="spline",
                  color_discrete_sequence=["#a855f7"])

    fig.update_layout(
        plot_bgcolor="#111",
        paper_bgcolor="#111",
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 🥧 DONUT CHART (LIKE SECOND IMAGE)
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("### 🥧 Leads by Channel")

    df2 = pd.DataFrame({
        "Channel": ["Messenger", "Email", "Ads", "Search", "Social"],
        "Leads": [207, 390, 150, 500, 271]
    })

    fig2 = px.pie(
        df2,
        names="Channel",
        values="Leads",
        hole=0.6,
        color_discrete_sequence=px.colors.qualitative.Bold
    )

    fig2.update_layout(
        plot_bgcolor="#111",
        paper_bgcolor="#111",
        font_color="white"
    )

    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# CHECKOUT
# -------------------------------
if st.button("Checkout"):
    st.success("🎉 Order placed!")
    st.balloons()
    st.session_state.cart = []
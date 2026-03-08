import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Bowla's Garage", page_icon="🚗", layout="wide")

# --- CSS ---
st.markdown("""
<style>
    .stApp { background-color: #050505; color: white; }
    .m-stripe {
        height: 8px; width: 100%;
        background: linear-gradient(90deg, #0033ad 0%, #0033ad 33%, #000000 33%, #000000 66%, #ff0000 66%, #ff0000 100%);
        margin-bottom: 20px;
    }
    .custom-card {
        background-color: #111111;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #222;
        min-height: 450px;
    }
    .price-text { color: #4da3ff; font-size: 42px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- THE DATA PATTERN ---
# Prices exactly as you listed for Engine Oil and Filters
engines = {
    "N20": {"oil": 15000, "oil_filter": 2800, "air_filter": 5000, "cabin_filter": 6000, "labor": 14500},
    "N55": {"oil": 18000, "oil_filter": 2800, "air_filter": 5000, "cabin_filter": 6000, "labor": 14500},
    "B48": {"oil": 18000, "oil_filter": 3500, "air_filter": 8000, "cabin_filter": 8000, "labor": 15500},
    "B58": {"oil": 21000, "oil_filter": 5000, "air_filter": 8000, "cabin_filter": 8000, "labor": 15500}
}

st.markdown('<div class="m-stripe"></div>', unsafe_allow_html=True)
st.title("🔧 Bowla's Garage")
st.write("📍 90C Red Hills Road, Kingston")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.header("🛠️ SERVICE ESTIMATOR")
    
    selected_engine = st.selectbox("1. Select Engine Type", ["N20", "N55", "B48", "B58"])
    tier = st.radio("2. Select Service Tier", ["Basic F30", "Regular F30"])
    
    # Logic based on your pattern:
    data = engines[selected_engine]
    
    # BASIC = Oil + Oil Filter + Cabin Filter + Labor
    basic_total = data['oil'] + data['oil_filter'] + data['cabin_filter'] + data['labor']
    
    # REGULAR = Basic + Air Filter
    if tier == "Basic F30":
        final_price = basic_total
        items_included = ["Engine Oil", "Oil Filter", "Cabin Filter", "Labor"]
    else:
        final_price = basic_total + data['air_filter']
        items_included = ["Engine Oil", "Oil Filter", "Cabin Filter", "Air Filter", "Labor"]

    st.write(f"ESTIMATED {tier} TOTAL:")
    st.markdown(f'<p class="price-text">${final_price:,.0f} JMD</p>', unsafe_allow_html=True)
    
    st.write("**Includes:**")
    for item in items_included:
        st.write(f"✅ {item}")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.header("📅 BOOKING")
    name = st.text_input("Customer Name", value="Teroy")
    model = st.text_input("Vehicle Model", value="n55")
    
    if st.button("MESSAGE ON WHATSAPP ✅"):
        if name and model:
            msg = f"Hi Bowla! My name is {name}. I'd like to book a {tier} for my {model} ({selected_engine}). Total: ${final_price:,.0f} JMD.".replace(" ", "%20")
            st.markdown(f'<meta http-equiv="refresh" content="0;URL=https://wa.me/18764972031?text={msg}">', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
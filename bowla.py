import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Bowla's Garage", page_icon="🚗", layout="wide")

# --- CSS (Premium Dark Theme) ---
st.markdown("""
<style>
    .stApp { background-color: #050505; color: white; }
    .m-stripe {
        height: 10px; width: 100%;
        background: linear-gradient(90deg, #0033ad 0%, #0033ad 33%, #000000 33%, #000000 66%, #ff0000 66%, #ff0000 100%);
        margin-bottom: 30px;
    }
    .custom-card {
        background-color: #111111; padding: 30px; border-radius: 15px; border: 1px solid #222;
    }
    .price-text { color: #4da3ff; font-size: 42px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- THE DATA PATTERN ---
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
    st.header("🛠️ BUILD YOUR SERVICE")
    
    selected_engine = st.selectbox("1. Select Engine Type", ["N20", "N55", "B48", "B58"])
    st.write("2. Select Required Items:")
    
    data = engines[selected_engine]
    
    # Checkboxes for full control
    inc_oil = st.checkbox(f"Engine Oil (${data['oil']:,.0f})", value=True)
    inc_filter = st.checkbox(f"Oil Filter (${data['oil_filter']:,.0f})", value=True)
    inc_cabin = st.checkbox(f"Cabin Filter (${data['cabin_filter']:,.0f})", value=True)
    inc_air = st.checkbox(f"Air Filter (${data['air_filter']:,.0f})", value=False)
    inc_labor = st.checkbox(f"Labor (${data['labor']:,.0f})", value=True)
    
    # Calculate Total based on selections
    total = 0
    selected_items = []
    
    if inc_oil: total += data['oil']; selected_items.append("Oil")
    if inc_filter: total += data['oil_filter']; selected_items.append("Oil Filter")
    if inc_cabin: total += data['cabin_filter']; selected_items.append("Cabin Filter")
    if inc_air: total += data['air_filter']; selected_items.append("Air Filter")
    if inc_labor: total += data['labor']; selected_items.append("Labor")

    st.write("YOUR ESTIMATED TOTAL:")
    st.markdown(f'<p class="price-text">${total:,.0f} JMD</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.header("📅 BOOKING")
    name = st.text_input("Customer Name", value="Teroy")
    model = st.text_input("Vehicle Model", placeholder="e.g. 2015 335i")
    
    if st.button("SEND TO WHATSAPP ✅"):
        if name and model:
            items_str = ", ".join(selected_items)
            msg = f"Hi Bowla! My name is {name}. I'd like to book a service for my {model} ({selected_engine}). Items: {items_str}. Total: ${total:,.0f} JMD.".replace(" ", "%20")
            st.markdown(f'<meta http-equiv="refresh" content="0;URL=https://wa.me/18765551234?text={msg}">', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
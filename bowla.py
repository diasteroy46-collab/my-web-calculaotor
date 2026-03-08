import streamlit as st

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Bowla's Garage Ltd", page_icon="🚗", layout="wide")

# --- 2. PREMIUM CSS ---
st.markdown("""
<style>
    .stApp { background-color: #050505; color: white; }
    .m-stripe {
        height: 10px; width: 100%;
        background: linear-gradient(90deg, #0033ad 0%, #0033ad 33%, #000000 33%, #000000 66%, #ff0000 66%, #ff0000 100%);
        margin-bottom: 20px;
    }
    /* Logo and Header Styling */
    .header-box {
        background-color: #111111;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #222;
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }
    .custom-card {
        background-color: #111111;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #222;
        min-height: 520px;
    }
    .price-text { color: #4da3ff; font-size: 42px; font-weight: bold; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

# --- 3. THE DATA ---
engines = {
    "N20": {"oil": 15000, "oil_filter": 2800, "air_filter": 5000, "cabin_filter": 6000, "labor": 14500},
    "N55": {"oil": 18000, "oil_filter": 2800, "air_filter": 5000, "cabin_filter": 6000, "labor": 14500},
    "B48": {"oil": 18000, "oil_filter": 3500, "air_filter": 8000, "cabin_filter": 8000, "labor": 15500},
    "B58": {"oil": 21000, "oil_filter": 5000, "air_filter": 8000, "cabin_filter": 8000, "labor": 15500}
}

# --- 4. TOP BAR & LOGO HEADER ---
st.markdown('<div class="m-stripe"></div>', unsafe_allow_html=True)

# Header with Logo
head_col1, head_col2 = st.columns([1, 4])
with head_col1:
    # This uses a standard BMW logo link
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg", width=100)
with head_col2:
    st.markdown("## BOWLA'S GARAGE LTD")
    st.markdown("📍 **90C Red Hills Rd, Kingston 19**")

# --- 5. THE SIDE-BY-SIDE COLUMNS ---
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("🛠️ SERVICE ESTIMATOR")
    
    selected_engine = st.selectbox("1. Select Engine Type", list(engines.keys()))
    st.write("2. Select Required Items:")
    
    data = engines[selected_engine]
    
    # Checkboxes for full control
    inc_oil = st.checkbox(f"Engine Oil (${data['oil']:,.0f})", value=True)
    inc_filter = st.checkbox(f"Oil Filter (${data['oil_filter']:,.0f})", value=True)
    inc_cabin = st.checkbox(f"Cabin Filter (${data['cabin_filter']:,.0f})", value=True)
    inc_air = st.checkbox(f"Air Filter (${data['air_filter']:,.0f})", value=False)
    inc_labor = st.checkbox(f"Labor (${data['labor']:,.0f})", value=True)
    
    # Calculation
    total = 0
    items_selected = []
    if inc_oil: total += data['oil']; items_selected.append("Oil")
    if inc_filter: total += data['oil_filter']; items_selected.append("Oil Filter")
    if inc_cabin: total += data['cabin_filter']; items_selected.append("Cabin Filter")
    if inc_air: total += data['air_filter']; items_selected.append("Air Filter")
    if inc_labor: total += data['labor']; items_selected.append("Labor")

    st.markdown(f'<p class="price-text">${total:,.0f} JMD</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("📅 BOOK APPOINTMENT")
    
    u_name = st.text_input("Customer Name", value="Teroy")
    u_model = st.text_input("Vehicle Model (e.g. BMW M3)")
    
    st.write("") 
    
    if st.button("SEND TO WHATSAPP ✅"):
        if u_name and u_model:
            selected_str = ", ".join(items_selected)
            message = f"Hi Bowla! I'm {u_name}. I want to book {selected_str} for my {u_model} ({selected_engine}). Total: ${total:,.0f} JMD."
            # Business WhatsApp Link (Replace with real number)
            wa_link = f"https://wa.me/18765551234?text={message.replace(' ', '%20')}"
            st.markdown(f'<meta http-equiv="refresh" content="0;URL={wa_link}">', unsafe_allow_html=True)
        else:
            st.error("Please enter your name and vehicle model.")

    st.write("---")
    st.markdown('<a href="https://instagram.com/bowlasgarageltd" target="_blank"><button style="width:100%; padding:10px; border-radius:10px; background-color:#2d323e; color:white; border:none; cursor:pointer; font-weight:bold;">FOLLOW US ON INSTAGRAM 📸</button></a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
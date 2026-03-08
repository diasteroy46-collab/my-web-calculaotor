import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Bowla's Garage | BMW Specialist",
    page_icon="https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg",
    layout="wide"
)

# --- FIXED CSS FOR STRIPES & READABLE PRICE BOX ---
st.markdown("""
    <style>
    /* Fixed M-Stripes at the very top */
    .m-stripe-container {
        width: 100%;
        display: flex;
        height: 12px;
        margin-bottom: 30px;
        border-radius: 5px;
        overflow: hidden;
    }
    .m-blue { background-color: #0033AD; flex: 1; }
    .m-dark-blue { background-color: #001C57; flex: 1; }
    .m-red { background-color: #E7222E; flex: 1; }
    
    /* High-Contrast Price Box (Black text on white background) */
    .price-box {
        padding: 25px;
        border-radius: 12px;
        background-color: #ffffff;
        border-left: 8px solid #0033AD;
        color: #000000 !important; /* Forces black text */
        margin-top: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    .price-box h3, .price-box p, .price-box b {
        color: #000000 !important;
    }
    
    /* Button Styling */
    .stButton>button {
        width: 100%;
        background-color: #0033AD;
        color: white;
        border-radius: 5px;
        height: 3.5em;
        font-weight: bold;
        border: none;
    }
    </style>
    
    <div class="m-stripe-container">
        <div class="m-blue"></div>
        <div class="m-dark-blue"></div>
        <div class="m-red"></div>
    </div>
    """, unsafe_allow_html=True)

st.title("🛠️ Bowla's Garage Estimator")
st.write("### BMW Specialist | 90C Red Hills Road")

# --- PRICING DATA (Exact from secretary's list) ---
# Note: B58 Basic is $44,000 and Regular is $57,500
pricing_data = {
    "N20 (4-Cylinder Turbo)": {
        "oil": 15000, "oil_filter": 2800, "air_filter": 5000, "cabin_filter": 6000, "labour_basic": 10000, "labour_reg": 14500
    },
    "N55 (6-Cylinder Turbo)": {
        "oil": 18000, "oil_filter": 2800, "air_filter": 5000, "cabin_filter": 6000, "labour_basic": 10000, "labour_reg": 14500
    },
    "B48 (New 4-Cylinder)": {
        "oil": 18000, "oil_filter": 3500, "air_filter": 8000, "cabin_filter": 8000, "labour_basic": 10000, "labour_reg": 15500
    },
    "B58 (New 6-Cylinder)": {
        "oil": 21000, "oil_filter": 5000, "air_filter": 8000, "cabin_filter": 8000, "labour_basic": 10000, "labour_reg": 15500
    }
}

# --- USER INPUTS ---
col1, col2 = st.columns(2)
with col1:
    customer_name = st.text_input("Customer Name", placeholder="e.g. Teroy")
with col2:
    engine = st.selectbox("Engine Type", list(pricing_data.keys()))

st.markdown("---")

# --- SERVICE SELECTION ---
st.write("### Choose Your Service")
service_type = st.radio("Select Package", ["Basic Service (Oil & Filter Only)", "Full Service (All Filters)", "Custom Selection"])

selected = pricing_data[engine]
do_oil = True
do_air = False
do_cabin = False
labour = selected["labour_reg"] # Default to regular labour

if service_type == "Basic Service (Oil & Filter Only)":
    labour = selected["labour_basic"]
elif service_type == "Full Service (All Filters)":
    do_air = True
    do_cabin = True
elif service_type == "Custom Selection":
    c1, c2 = st.columns(2)
    with c1:
        do_oil = st.checkbox("Engine Oil & Filter", value=True)
    with c2:
        do_air = st.checkbox("Air Filter")
        do_cabin = st.checkbox("Cabin (A/C) Filter")

# --- CALCULATION ---
final_total = labour
details = ["Professional Labour"]

if do_oil:
    final_total += selected["oil"] + selected["oil_filter"]
    details.append("Oil Change & Filter")
if do_air:
    final_total += selected["air_filter"]
    details.append("Air Filter")
if do_cabin:
    final_total += selected["cabin_filter"]
    details.append("Cabin Filter")

# --- DISPLAY (FIXED VISIBILITY) ---
st.markdown(f"""
<div class="price-box">
    <h3>Estimated Total: ${final_total:,} JMD</h3>
    <p><b>Included Services:</b> {", ".join(details)}</p>
</div>
""", unsafe_allow_html=True)

st.caption("Prices are estimates and subject to parts availability.")

# --- WHATSAPP ---
garage_phone = "1876XXXXXXX" # Insert actual number

msg = f"Hi Bowla's Garage, I'm {customer_name}. Estimate for {engine}: ${final_total:,} JMD. Services: {', '.join(details)}."
wa_url = f"https://wa.me/{garage_phone}?text={msg.replace(' ', '%20')}"

if st.button("Confirm & Book via WhatsApp"):
    if customer_name:
        st.markdown(f'<meta http-equiv="refresh" content="0;URL={wa_url}">', unsafe_allow_html=True)
    else:
        st.warning("Please enter a name to book.")

st.markdown("---")
st.info("📍 90C Red Hills Road | BMW Specialists")
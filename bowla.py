import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Bowla's Garage | BMW Specialist",
    page_icon="https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg",
    layout="centered"
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .m-stripe { height: 10px; width: 100%; display: flex; margin-bottom: 20px; }
    .m-blue { background-color: #0033AD; flex: 1; }
    .m-dark-blue { background-color: #001C57; flex: 1; }
    .m-red { background-color: #E7222E; flex: 1; }
    .stButton>button {
        width: 100%;
        background-color: #0033AD;
        color: white;
        border-radius: 5px;
        height: 3em;
        font-weight: bold;
    }
    .price-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        border-left: 5px solid #0033AD;
    }
    </style>
    <div class="m-stripe">
        <div class="m-blue"></div>
        <div class="m-dark-blue"></div>
        <div class="m-red"></div>
    </div>
    """, unsafe_allow_html=True)

st.title("🛠️ Bowla's Garage Estimator")
st.subheader("BMW Specialist | 90C Red Hills Road")

# --- PRICING DATA (Official List) ---
pricing_data = {
    "N20 (4-Cylinder Turbo)": {
        "oil": 15000, "oil_filter": 2800, "air_filter": 5000, "cabin_filter": 6000, "labour": 14500
    },
    "N55 (6-Cylinder Turbo)": {
        "oil": 18000, "oil_filter": 2800, "air_filter": 5000, "cabin_filter": 6000, "labour": 14500
    },
    "B48 (New 4-Cylinder)": {
        "oil": 18000, "oil_filter": 3500, "air_filter": 8000, "cabin_filter": 8000, "labour": 15500
    },
    "B58 (New 6-Cylinder)": {
        "oil": 21000, "oil_filter": 5000, "air_filter": 8000, "cabin_filter": 8000, "labour": 15500
    }
}

# --- USER INPUTS ---
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Customer Name")
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

if service_type == "Full Service (All Filters)":
    do_air = True
    do_cabin = True
elif service_type == "Custom Selection":
    col_a, col_b = st.columns(2)
    with col_a:
        do_oil = st.checkbox("Engine Oil & Filter", value=True)
    with col_b:
        do_air = st.checkbox("Air Filter")
        do_cabin = st.checkbox("Cabin (A/C) Filter")

# --- CALCULATION ---
total = selected["labour"]
details = ["Professional Labour"]

if do_oil:
    total += selected["oil"] + selected["oil_filter"]
    details.append("Oil Change & Filter")
if do_air:
    total += selected["air_filter"]
    details.append("Air Filter")
if do_cabin:
    total += selected["cabin_filter"]
    details.append("Cabin Filter")

# --- DISPLAY ---
st.markdown(f"""
<div class="price-box">
    <h3>Estimated Total: ${total:,} JMD</h3>
    <p><b>Includes:</b> {", ".join(details)}</p>
</div>
""", unsafe_allow_html=True)

st.caption("Prices are estimates and subject to parts availability.")

# --- WHATSAPP ---
# UPDATING TO THE NEW GARAGE NUMBER
garage_phone = "18764972031" # Bowla's Garage WhatsApp Number

msg = f"Hi Bowla's Garage, I'm {name}. Estimate for {engine}: ${total:,} JMD. Services: {', '.join(details)}."
wa_url = f"https://wa.me/{garage_phone}?text={msg.replace(' ', '%20')}"

if st.button("Confirm & Book via WhatsApp"):
    if name:
        st.markdown(f'<meta http-equiv="refresh" content="0;URL={wa_url}">', unsafe_allow_html=True)
    else:
        st.warning("Please enter your name to complete the booking.")

st.markdown("---")
st.info("📍 90C Red Hills Road | BMW Specialists")
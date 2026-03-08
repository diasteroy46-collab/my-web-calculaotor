import streamlit as st

# --- PAGE CONFIG (Back to the original centered layout) ---
st.set_page_config(
    page_title="Bowla's Garage | BMW Specialist",
    page_icon="https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg",
    layout="centered"
)

# --- CLEAN CSS (No "Fixed" positions to avoid shifting the web layout) ---
st.markdown("""
    <style>
    .m-stripe {
        height: 10px;
        width: 100%;
        display: flex;
        margin-bottom: 20px;
    }
    .m-blue { background-color: #0033AD; flex: 1; }
    .m-dark-blue { background-color: #001C57; flex: 1; }
    .m-red { background-color: #E7222E; flex: 1; }
    
    /* Price Box that works in both Light and Dark mode */
    .price-box {
        padding: 20px;
        border-radius: 10px;
        background-color: rgba(0, 51, 173, 0.1);
        border-left: 5px solid #0033AD;
        margin: 20px 0;
    }
    
    .stButton>button {
        width: 100%;
        background-color: #0033AD;
        color: white;
        font-weight: bold;
        height: 3.5em;
    }
    </style>
    
    <div class="m-stripe">
        <div class="m-blue"></div>
        <div class="m-dark-blue"></div>
        <div class="m-red"></div>
    </div>
    """, unsafe_allow_html=True)

st.title("🛠️ Bowla's Garage Estimator")
st.info("90C Red Hills Road | BMW Specialist")

# --- PRICING DATA (Official B58 & B48 Included) ---
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

# --- INPUTS ---
name = st.text_input("Customer Name")
engine = st.selectbox("Select Engine", list(pricing_data.keys()))

st.write("### Services")
service_type = st.radio("Package", ["Basic (Oil & Filter)", "Full Service", "Custom"])

selected = pricing_data[engine]
do_oil, do_air, do_cabin = True, False, False

if service_type == "Full Service":
    do_air, do_cabin = True, True
elif service_type == "Custom":
    do_oil = st.checkbox("Oil & Filter", value=True)
    do_air = st.checkbox("Air Filter")
    do_cabin = st.checkbox("Cabin Filter")

# --- MATH ---
total = selected["labour"]
items = ["Labour"]

if do_oil:
    total += selected["oil"] + selected["oil_filter"]
    items.append("Oil/Filter")
if do_air:
    total += selected["air_filter"]
    items.append("Air Filter")
if do_cabin:
    total += selected["cabin_filter"]
    items.append("Cabin Filter")

# --- DISPLAY ---
st.markdown(f"""
<div class="price-box">
    <h2 style="margin:0;">Total: ${total:,} JMD</h2>
    <p style="margin:0; opacity: 0.8;">Includes: {', '.join(items)}</p>
</div>
""", unsafe_allow_html=True)

# --- WHATSAPP ---
garage_phone = "1876XXXXXXX" # Put the number here

message = f"Hello Bowla's Garage, my name is {name}. I'd like to book a service for my {engine}. Estimate: ${total:,} JMD."
whatsapp_url = f"https://wa.me/{garage_phone}?text={message.replace(' ', '%20')}"

if st.button("Book via WhatsApp"):
    if name:
        st.markdown(f'<meta http-equiv="refresh" content="0;URL={whatsapp_url}">', unsafe_allow_html=True)
    else:
        st.error("Please enter your name first.")
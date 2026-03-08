import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Bowla's Garage", page_icon="🚗", layout="wide")

# --- CSS FOR THE EXACT LOOK ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    .m-stripe {
        height: 6px;
        width: 100%;
        background: linear-gradient(90deg, #0033ad 0%, #0033ad 33%, #000000 33%, #000000 66%, #ff0000 66%, #ff0000 100%);
        margin-bottom: 20px;
    }
    .custom-card {
        background-color: #111111;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #222;
        margin-bottom: 15px;
    }
    .price-text {
        color: #4da3ff;
        font-size: 38px;
        font-weight: bold;
        margin: 0;
    }
    .part-list {
        font-size: 14px;
        color: #aaaaaa;
        line-height: 1.6;
    }
    </style>
    """, unsafe_content_safe=True)

# --- THE CORRECT DATA FROM YOUR SHEET ---
# Breaking it down so we can show the user what they are paying for
parts_prices = {
    "N20": {"oil": 12500, "filter": 2800, "cabin": 5000, "air": 7500, "labor": 12500},
    "N55": {"oil": 15500, "filter": 2800, "cabin": 5000, "air": 10500, "labor": 12500},
    "B48": {"oil": 12500, "filter": 4500, "cabin": 10000, "air": 5500, "labor": 12500},
    "B58": {"oil": 15500, "filter": 3500, "cabin": 12500, "air": 13500, "labor": 12500}
}

st.markdown('<div class="m-stripe"></div>', unsafe_content_safe=True)
st.title("🔧 Bowla's Garage")
st.subheader("Specializing in German Cars: BMW • Audi • Mercedes-Benz")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="custom-card">', unsafe_content_safe=True)
    st.header("🛠️ SERVICE ESTIMATOR")
    
    brand = st.selectbox("Vehicle Brand", ["BMW", "Audi", "Mercedes-Benz"])
    engine = st.selectbox("Engine Type", ["N20", "N55", "B48", "B58"])
    tier = st.radio("Service Tier", ["Basic F30", "Regular F30"], horizontal=True)
    
    # Calculation Logic
    data = parts_prices[engine]
    if tier == "Basic F30":
        # Oil + Filter + Cabin + Labor
        total = data['oil'] + data['filter'] + data['cabin'] + data['labor']
        items = ["Oil Change", "Oil Filter", "Cabin Filter", "Service Labor"]
    else:
        # Basic + Air Filter
        total = data['oil'] + data['filter'] + data['cabin'] + data['air'] + data['labor']
        items = ["Oil Change", "Oil Filter", "Cabin Filter", "Air Filter", "Service Labor"]

    st.write("STARTING AT")
    st.markdown(f'<p class="price-text">${total:,.0f} JMD</p>', unsafe_content_safe=True)
    
    st.markdown('<div class="part-list">', unsafe_content_safe=True)
    st.write("📦 **Package Includes:**")
    for item in items:
        st.write(f"• {item}")
    st.markdown('</div>', unsafe_content_safe=True)
    st.markdown('</div>', unsafe_content_safe=True)

with col2:
    st.markdown('<div class="custom-card">', unsafe_content_safe=True)
    st.header("📅 BOOK NOW")
    
    name = st.text_input("Your Name")
    model = st.text_input("Vehicle Model (e.g. 2014 328i)")
    
    if st.button("SEND TO WHATSAPP ✅"):
        if name and model:
            msg = f"Hi Bowla! My name is {name}. I'd like to book a {tier} for my {brand} {model} ({engine}). Estimate: ${total:,.0f} JMD."
            wa_link = f"https://wa.me/1876XXXXXXX?text={msg.replace(' ', '%20')}"
            st.markdown(f'<meta http-equiv="refresh" content="0;URL={wa_link}">', unsafe_content_safe=True)
        else:
            st.error("Please enter your name and vehicle model.")
            
    st.write("")
    st.markdown('<a href="https://instagram.com/bowlasgarageltd" target="_blank"><button style="width:100%; padding:12px; border-radius:8px; background-color:#2d323e; color:white; border:none; cursor:pointer;">FOLLOW @BOWLASGARAGELTD 📸</button></a>', unsafe_content_safe=True)
    st.markdown('</div>', unsafe_content_safe=True)
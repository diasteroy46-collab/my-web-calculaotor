import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Bowla's Garage", page_icon="🚗", layout="wide")

# --- FIXED CSS BLOCK ---
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
    }
</style>
""", unsafe_content_safe=True)

# --- EXACT DATA FROM YOUR SHEET ---
# Totals for N20, N55, B48, and handwritten B58 updates
pricing = {
    "N20": {"Basic F30": 32800, "Regular F30": 43300},
    "N55": {"Basic F30": 35800, "Regular F30": 46300},
    "B48": {"Basic F30": 39500, "Regular F30": 45000},
    "B58": {"Basic F30": 44000, "Regular F30": 57500}
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
    
    # Calculate Total
    total = pricing[engine][tier]
    
    st.write("STARTING AT")
    st.markdown(f'<p class="price-text">${total:,.0f} JMD</p>', unsafe_content_safe=True)
    st.markdown('</div>', unsafe_content_safe=True)

with col2:
    st.markdown('<div class="custom-card">', unsafe_content_safe=True)
    st.header("📅 BOOK APPOINTMENT")
    name = st.text_input("Customer Name", value="Teroy")
    model = st.text_input("Vehicle Model", placeholder="e.g. BMW M3")
    
    if st.button("SEND TO WHATSAPP ✅"):
        if name and model:
            msg = f"Hi Bowla! My name is {name}. I'd like to book a {tier} for my {brand} {model} ({engine}). Estimate: ${total:,.0f} JMD."
            # Replace with Bowla's actual number
            wa_link = f"https://wa.me/1876XXXXXXX?text={msg.replace(' ', '%20')}"
            st.markdown(f'<a href="{wa_link}" target="_blank">Click here to open WhatsApp</a>', unsafe_content_safe=True)
            
    st.write("")
    st.markdown('<a href="https://instagram.com/bowlasgarageltd" target="_blank"><button style="width:100%; padding:10px; border-radius:5px; background-color:#2d323e; color:white; border:none; cursor:pointer;">FOLLOW US ON INSTAGRAM 📸</button></a>', unsafe_content_safe=True)
    st.markdown('</div>', unsafe_content_safe=True)
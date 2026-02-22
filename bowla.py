import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Bowla's Garage Ltd", page_icon="🏎️", layout="wide")

# 2. High-Contrast Elite Styling
st.markdown("""
    <style>
    .stApp {
        background: #000000;
        color: #ffffff;
        border-top: 15px solid;
        border-image: linear-gradient(to right, #5da9e1 33%, #003399 33% 66%, #d5001c 66%) 1;
    }

    /* Making the cards actually visible with a lighter gray */
    [data-testid="stVerticalBlock"] > div > div > div > div.stVerticalBlock {
        background: #121212;
        padding: 35px;
        border-radius: 20px;
        border: 1px solid #222;
        box-shadow: 0 15px 35px rgba(0,0,0,0.8);
        margin-bottom: 20px;
    }

    /* Glow for the Price */
    [data-testid="stMetricValue"] {
        color: #5da9e1 !important;
        font-family: 'Arial Black', sans-serif;
        text-shadow: 0 0 10px rgba(93, 169, 225, 0.3);
    }

    /* WhatsApp & IG Button Glow */
    .stButton>button {
        border-radius: 12px !important;
        height: 3.5em !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Branding Section
logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/BMW.svg/600px-BMW.svg.png"
col_logo, col_text = st.columns([1, 5])
with col_logo:
    st.image(logo_url, width=110)
with col_text:
    st.markdown("# BOWLA'S GARAGE LTD")
    st.markdown("### 📍 90C Red Hills Rd, Kingston 19")

st.divider()

# 4. Main Showroom Floor
col_left, col_right = st.columns(2, gap="large")

with col_left:
    st.subheader("🛠️ SERVICE ESTIMATOR")
    service = st.selectbox(
        "Select your required service:",
        ["Full Synthetic Oil Change", "Brake System Overhaul", "Computer Diagnostics", "Suspension Tuning", "Engine Tune-up"]
    )
    
    prices = {
        "Full Synthetic Oil Change": 12500, "Brake System Overhaul": 18000,
        "Computer Diagnostics": 5500, "Suspension Tuning": 7500, "Engine Tune-up": 22000
    }
    
    st.metric("STARTING AT", f"${prices[service]:,} JMD")

with col_right:
    st.subheader("📅 BOOK APPOINTMENT")
    name = st.text_input("Customer Name")
    car = st.text_input("Vehicle Model (e.g. BMW M3)")
    
    phone = "18765555555" # CHANGE TO REAL NUMBER
    msg = f"Hi Bowla's Garage, my name is {name}. I'd like to book a {service} for my {car}."
    link = f"https://wa.me/{phone}?text={msg.replace(' ', '%20')}"
    
    if name and car:
        st.link_button("SEND TO WHATSAPP ✅", link)
        st.link_button("FOLLOW US ON INSTAGRAM 📸", "https://www.instagram.com/bowlasgarageltd")
    else:
        st.info("Enter details above to unlock booking.")

# 5. NEW VISIBLE OPENING HOURS SECTION
st.write("---")
h_col1, h_col2 = st.columns(2)

with h_col1:
    st.markdown("### 🕒 WORKSHOP HOURS")
    st.markdown("""
    * **Mon - Fri:** 8:00 AM - 5:00 PM
    * **Saturday:** 9:00 AM - 3:00 PM
    * **Sunday:** CLOSED
    """)

with h_col2:
    st.markdown("### 📞 DIRECT CONTACT")
    st.write("For emergency towing or parts inquiries:")
    st.write("Call: +1 (876) XXX-XXXX")
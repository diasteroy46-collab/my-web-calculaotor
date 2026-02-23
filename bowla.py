import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Bowla's Garage | BMW Specialist", page_icon="🏎️", layout="wide")

# 2. Elite M-Performance Styling (Original Flawless Look)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    
    /* The M-Stripe at the top */
    [data-testid="stAppViewContainer"] {
        border-top: 15px solid;
        border-image: linear-gradient(to right, #5da9e1 33%, #003399 33% 66%, #ff0000 66%) 1;
    }

    /* Centering the Header */
    .header-container { text-align: center; padding-bottom: 20px; }

    /* Dark Card styling for the two columns */
    [data-testid="stVerticalBlock"] > div > div > div > div.stVerticalBlock {
        background-color: #121212 !important;
        padding: 30px !important;
        border-radius: 20px !important;
        border: 1px solid #333 !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    h1, h2, h3, p, span, label { color: white !important; }
    .stSelectbox label, .stTextInput label { color: #888 !important; font-weight: bold; }
    
    .footer-text { text-align: center; color: #555 !important; margin-top: 30px; }
    </style>
""", unsafe_allow_html=True)

# 3. Centered Header: Logo + Name + Address
st.markdown("""
    <div class="header-container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg" width="80">
        <h1 style="margin-top: 10px; font-size: 3em;">BOWLA'S GARAGE LTD</h1>
        <p style="color: #888 !important; font-size: 1.2em;">🏁 BMW M-Performance Specialist</p>
        <p style="color: #5da9e1 !important;">📍 90C Red Hills Rd, Kingston 19</p>
    </div>
""", unsafe_allow_html=True)

st.divider()

# 4. Smart Pricing Database (Including Towing)
pricing_data = {
    "Engine Tuning": {"M2": 30000, "M3": 35000, "M4": 35000, "M5": 40000, "M6": 40000, "X5M": 45000},
    "Oil Change (Synthetic)": {"M2": 15000, "M3": 18000, "M4": 18000, "M5": 22000, "M6": 22000, "X5M": 25000},
    "Brake Overhaul": {"M2": 25000, "M3": 28000, "M4": 28000, "M5": 35000, "M6": 35000, "X5M": 38000},
    "Towing Service": {"M2": 12000, "M3": 12000, "M4": 12000, "M5": 15000, "M6": 15000, "X5M": 18000},
    "Computer Diagnostics": {"M2": 5500, "M3": 5500, "M4": 5500, "M5": 5500, "M6": 5500, "X5M": 5500}
}

# 5. The Estimator UI (Dropdown Logic)
col_left, col_right = st.columns(2, gap="large")

with col_left:
    st.subheader("🛠️ SERVICE ESTIMATOR")
    service_choice = st.selectbox("Select Service Required", list(pricing_data.keys()))
    
    # Logic to filter car list based on service
    available_models = list(pricing_data[service_choice].keys())
    model_choice = st.selectbox("Select Your BMW Model", available_models)
    
    price = pricing_data[service_choice][model_choice]

    # M-Bordered Price Box
    st.markdown(f"""
        <div style="background-color: #000; padding: 25px; border-radius: 15px; border-left: 5px solid #0066ff; border-right: 5px solid #ff0000; text-align: center; margin-top: 20px;">
            <p style="color: #888; margin: 0;">ESTIMATED COST</p>
            <h1 style="color: #0066ff; margin: 0; font-size: 45px;">${price:,} JMD</h1>
        </div>
    """, unsafe_allow_html=True)

with col_right:
    st.subheader("📅 BOOK APPOINTMENT")
    customer_name = st.text_input("Customer Name", placeholder="e.g. John Brown")
    st.write("Secure your slot by sending this estimate to Bowla via WhatsApp.")
    
    # WhatsApp URL Construction
    phone_number = "18765105118" 
    name_str = f"Hi Bowla, my name is {customer_name}." if customer_name else "Hi Bowla,"
    message = f"{name_str} I'd like to book a {service_choice} for my BMW {model_choice}. Estimate: ${price:,} JMD."
    whatsapp_url = f"https://wa.me/{phone_number}?text={message.replace(' ', '%20')}"
    
    # WhatsApp Button
    st.markdown(f'''
        <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
            <div style="background-color: #25D366; color: white; padding: 18px; border-radius: 12px; text-align: center; font-weight: bold; font-size: 18px; cursor: pointer; margin-top: 15px;">
                🚀 SEND TO WHATSAPP
            </div>
        </a>
    ''', unsafe_allow_html=True)
    
    # Instagram Button
    st.markdown('''
        <a href="https://instagram.com" target="_blank" style="text-decoration: none;">
            <div style="background-color: #1a1a1a; color: white; border: 1px solid #333; padding: 12px; border-radius: 10px; text-align: center; margin-top: 10px; font-size: 14px;">
                📸 FOLLOW US ON INSTAGRAM
            </div>
        </a>
    ''', unsafe_allow_html=True)

# 6. Opening Hours & Footer
st.divider()
col_f1, col_f2, col_f3 = st.columns(3)
with col_f2:
    st.markdown("""
        <div style="text-align: center; background-color: #111; padding: 20px; border-radius: 15px;">
            <h4 style="color: #5da9e1 !important; margin-bottom: 10px;">⏰ OPENING HOURS</h4>
            <p style="margin: 2px;">Mon - Fri: 8:30 AM - 5:30 PM</p>
            <p style="margin: 2px;">Sat: 9:00 AM - 3:00 PM</p>
            <p style="margin: 2px;">Sun: Closed</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<p class="footer-text">© 2026 Bowla\'s Garage Ltd | Kingston, Jamaica</p>', unsafe_allow_html=True)
import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Bowla's Garage | BMW Specialist", page_icon="🏎️", layout="wide")

# 2. Elite Styling (Stripe, Centered Text, and Cards)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    
    /* The M-Stripe */
    [data-testid="stAppViewContainer"] {
        border-top: 15px solid;
        border-image: linear-gradient(to right, #5da9e1 33%, #003399 33% 66%, #ff0000 66%) 1;
    }

    /* Centering the Header */
    .header-container {
        text-align: center;
        padding-bottom: 20px;
    }

    /* Dark Card styling for the two columns */
    [data-testid="stVerticalBlock"] > div > div > div > div.stVerticalBlock {
        background-color: #121212 !important;
        padding: 30px !important;
        border-radius: 20px !important;
        border: 1px solid #333 !important;
    }

    h1, h2, h3, p, span, label { color: white !important; }
    .stSelectbox label, .stTextInput label { color: #888 !important; }
    
    .footer-text {
        text-align: center;
        color: #555 !important;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header with BMW Logo and Centered Name
st.markdown("""
    <div class="header-container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg" width="80">
        <h1 style="margin-top: 10px;">BOWLA'S GARAGE LTD</h1>
        <p style="color: #888 !important;">🏁 BMW M-Performance Specialist | 📍 90C Red Hills Rd, Kingston 19</p>
    </div>
""", unsafe_allow_html=True)

st.divider()

# 4. Pricing Data
pricing_data = {
    "Engine Tuning": {"M2": 30000, "M3": 35000, "M4": 35000, "M5": 40000, "M6": 40000, "X5M": 45000},
    "Oil Change (Synthetic)": {"M2": 15000, "M3": 18000, "M4": 18000, "M5": 22000, "M6": 22000, "X5M": 25000},
    "Brake Overhaul": {"M2": 25000, "M3": 28000, "M4": 28000, "M5": 35000, "M6": 35000, "X5M": 38000},
    "Computer Diagnostics": {"M2": 5500, "M3": 5500, "M4": 5500, "M5": 5500, "M6": 5500, "X5M": 5500}
}

# 5. The Estimator UI
col_left, col_right = st.columns(2, gap="large")

with col_left:
    st.subheader("🛠️ SERVICE ESTIMATOR")
    service_choice = st.selectbox("What do you need done?", list(pricing_data.keys()))
    available_models = list(pricing_data[service_choice].keys())
    model_choice = st.selectbox("Which BMW do you drive?", available_models)
    price = pricing_data[service_choice][model_choice]

    st.markdown(f"""
        <div style="background-color: #000; padding: 20px; border-radius: 15px; border-left: 5px solid #0066ff; border-right: 5px solid #ff0000; text-align: center; margin-top: 20px;">
            <p style="color: #888; margin: 0;">Estimate for {model_choice}</p>
            <h1 style="color: #0066ff; margin: 0;">${price:,} JMD</h1>
        </div>
    """, unsafe_allow_html=True)

with col_right:
    st.subheader("📅 BOOK APPOINTMENT")
    # THE RESTORED FEATURE: Customer Name
    customer_name = st.text_input("Your Name", placeholder="e.g. John Doe")
    st.write("Send your estimate to Bowla's WhatsApp to secure your slot.")
    
    phone_number = "1875105118" 
    
    # Message logic that includes the name
    if customer_name:
        greeting = f"Hi Bowla, my name is {customer_name}."
    else:
        greeting = "Hi Bowla,"
        
    message = f"{greeting} I'd like to book a {service_choice} for my BMW {model_choice}. Estimate: ${price:,} JMD."
    whatsapp_url = f"https://wa.me/{phone_number}?text={message.replace(' ', '%20')}"
    
    st.markdown(f'''
        <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
            <div style="background-color: #25D366; color: white; padding: 18px; border-radius: 12px; text-align: center; font-weight: bold; font-size: 18px; cursor: pointer; margin-top: 20px;">
                🚀 Send to WhatsApp
            </div>
        </a>
    ''', unsafe_allow_html=True)

# 6. Opening Hours & Footer
st.divider()
col1, col2, col3 = st.columns(3)
with col2:
    st.markdown("""
        <div style="text-align: center;">
            <h4 style="color: #5da9e1 !important;">⏰ OPENING HOURS</h4>
            <p>Mon - Fri: 8:30 AM - 5:30 PM</p>
            <p>Sat: 9:00 AM - 3:00 PM</p>
            <p>Sun: Closed</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<p class="footer-text">© 2026 Bowla\'s Garage Ltd | Kingston, Jamaica</p>', unsafe_allow_html=True)
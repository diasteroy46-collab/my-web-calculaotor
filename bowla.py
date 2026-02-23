import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Bowla's Garage | BMW Specialist", page_icon="🏎️", layout="wide")

# 2. Elite M-Performance Styling (RESTORED ALL FEATURES)
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #000000; color: #ffffff; }
    
    /* The M-Stripe at the top */
    [data-testid="stAppViewContainer"] {
        border-top: 15px solid;
        border-image: linear-gradient(to right, #5da9e1 33%, #003399 33% 66%, #ff0000 66%) 1;
    }

    /* THE FIX: Specifically styling the two main containers (Cards) */
    [data-testid="stVerticalBlock"] > div > div > div > div.stVerticalBlock {
        background-color: #121212 !important;
        padding: 40px !important;
        border-radius: 20px !important;
        border: 1px solid #333 !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5) !important;
        margin-bottom: 20px !important;
    }

    /* Text Colors */
    h1, h2, h3, p, span, label { color: white !important; }
    .stSelectbox label { color: #888 !important; font-weight: bold; }
    
    /* Price Box Styling */
    .price-display {
        background-color: #000; 
        padding: 25px; 
        border-radius: 15px; 
        border-left: 5px solid #0066ff; 
        border-right: 5px solid #ff0000; 
        text-align: center; 
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. The Smart Pricing Database
pricing_data = {
    "Engine Tuning": {
        "M2": 30000, "M3": 35000, "M4": 35000, "M5": 40000, "M6": 40000, "X5M": 45000
    },
    "Oil Change (Full Synthetic)": {
        "M2": 15000, "M3": 18000, "M4": 18000, "M5": 22000, "M6": 22000, "X5M": 25000
    },
    "Brake System Overhaul": {
        "M2": 25000, "M3": 28000, "M4": 28000, "M5": 35000, "M6": 35000, "X5M": 38000
    },
    "Computer Diagnostics": {
        "M2": 5500, "M3": 5500, "M4": 5500, "M5": 5500, "M6": 5500, "X5M": 5500
    }
}

# 4. Header Section
st.markdown("# BOWLA'S GARAGE LTD")
st.markdown("### 🏁 BMW M-Performance Specialist")
st.markdown("📍 90C Red Hills Rd, Kingston 19")
st.divider()

# 5. The Estimator UI
col_left, col_right = st.columns(2, gap="large")

with col_left:
    st.subheader("🛠️ SERVICE ESTIMATOR")
    
    # Dropdown 1: Service
    service_choice = st.selectbox("What do you need done?", list(pricing_data.keys()))
    
    # Dropdown 2: Model (Updates based on selection)
    available_models = list(pricing_data[service_choice].keys())
    model_choice = st.selectbox("Which BMW do you drive?", available_models)
    
    price = pricing_data[service_choice][model_choice]

    # Price Display
    st.markdown(f"""
        <div class="price-display">
            <p style="color: #888; margin: 0;">Estimated Price for {model_choice}</p>
            <h1 style="color: #0066ff; margin: 0; font-size: 42px;">${price:,} JMD</h1>
        </div>
    """, unsafe_allow_html=True)

with col_right:
    st.subheader("📅 BOOK APPOINTMENT")
    st.write("Ready to bring your machine in? Send your estimate directly to Bowla's WhatsApp.")
    
    # WhatsApp Integration
    phone_number = "18766693455" 
    message = f"Hi Bowla, I'd like to book a {service_choice} for my BMW {model_choice}. My estimate was ${price:,} JMD."
    whatsapp_url = f"https://wa.me/{phone_number}?text={message.replace(' ', '%20')}"
    
    # Professional Button
    st.markdown(f'''
        <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
            <div style="background-color: #25D366; color: white; padding: 20px; border-radius: 12px; text-align: center; font-weight: bold; font-size: 20px; cursor: pointer; margin-top: 15px;">
                🚀 Send to WhatsApp
            </div>
        </a>
    ''', unsafe_allow_html=True)

st.divider()
st.caption("© 2026 Bowla's Garage Ltd | Kingston, Jamaica")
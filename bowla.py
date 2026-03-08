import streamlit as st

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Bowla's Garage", page_icon="🚗", layout="wide")

# --- 2. PREMIUM DARK THEME & M-STRIPE CSS ---
st.markdown("""
    <style>
    /* Global Background */
    .stApp {
        background-color: #050505;
        color: white;
    }
    
    /* M-Stripe Header */
    .m-stripe {
        height: 10px;
        width: 100%;
        background: linear-gradient(90deg, #0033ad 0%, #0033ad 33%, #000000 33%, #000000 66%, #ff0000 66%, #ff0000 100%);
        margin-bottom: 30px;
    }

    /* Centered Logo & Title Area */
    .header-container {
        text-align: center;
        margin-bottom: 40px;
    }
    
    /* Premium Cards */
    .custom-card {
        background-color: #111111;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #222;
        min-height: 480px;
    }

    /* Pricing Text */
    .price-display {
        color: #4da3ff;
        font-size: 42px;
        font-weight: bold;
        margin-top: 10px;
    }

    /* Footer Styling */
    .footer {
        text-align: center;
        color: #666;
        margin-top: 50px;
        font-size: 14px;
        border-top: 1px solid #222;
        padding-top: 20px;
    }
    
    /* WhatsApp Button */
    .stButton>button {
        width: 100%;
        background-color: #25D366;
        color: white;
        font-weight: bold;
        border: none;
        height: 50px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DATA FROM YOUR PHOTO ---
# Including your handwritten B58 updates
pricing_data = {
    "N20": {"Basic F30": 32800, "Regular F30": 43300},
    "N55": {"Basic F30": 35800, "Regular F30": 46300},
    "B48": {"Basic F30": 39500, "Regular F30": 45000},
    "B58": {"Basic F30": 44000, "Regular F30": 57500} # Handwritten updates
}

# --- 4. HEADER SECTION ---
st.markdown('<div class="m-stripe"></div>', unsafe_allow_html=True)

st.markdown("""
    <div class="header-container">
        <h1>⚪🔵🔴 BOWLA'S GARAGE</h1>
        <p style="font-size: 18px; color: #aaa;">MECHANICAL SERVICES ESTIMATOR</p>
    </div>
    """, unsafe_allow_html=True)

# --- 5. MAIN CONTENT (TWO COLUMNS) ---
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("🛠️ SERVICE ESTIMATOR")
    
    brand = st.selectbox("1. Select Vehicle Brand", ["BMW", "Audi", "Mercedes-Benz"])
    engine = st.selectbox("2. Select Engine Type", ["N20", "N55", "B48", "B58"])
    tier = st.selectbox("3. Select Service Tier", ["Basic F30", "Regular F30"])
    
    # Calculate Price
    total_price = pricing_data[engine][tier]
    
    st.write("ESTIMATED STARTING AT:")
    st.markdown(f'<p class="price-display">${total_price:,.0f} JMD</p>', unsafe_allow_html=True)
    
    # Package details display
    if tier == "Basic F30":
        st.info("Includes: 5-7qrts Oil, Oil Filter, Cabin Filter, Labor.")
    else:
        st.info("Includes: 5-7qrts Oil, Oil Filter, Air Filter, Cabin Filter, Labor.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("📅 BOOK APPOINTMENT")
    
    name = st.text_input("Customer Name", placeholder="Enter your name")
    v_model = st.text_input("Vehicle Model", placeholder="e.g. 2018 340i")
    phone = st.text_input("Your Phone Number")
    
    st.write("") # Spacer
    
    if st.button("SEND BOOKING TO WHATSAPP ✅"):
        if name and v_model:
            message = f"Hi Bowla's Garage, my name is {name}. I'd like to book a {tier} for my {v_model} ({engine}). Estimated price: ${total_price:,.0f} JMD."
            # Note: Replace the number below with Bowla's actual WhatsApp number
            whatsapp_url = f"https://wa.me/18765551234?text={message.replace(' ', '%20')}"
            st.markdown(f'<meta http-equiv="refresh" content="0;URL={whatsapp_url}">', unsafe_allow_html=True)
            st.success("Redirecting to WhatsApp...")
        else:
            st.error("Please fill in your Name and Model.")
            
    st.markdown("""
        <div style="margin-top: 20px;">
            <a href="https://instagram.com/bowlasgarageltd" target="_blank" style="text-decoration:none;">
                <button style="width:100%; background-color:#333; color:white; border:none; padding:10px; border-radius:10px; cursor:pointer;">
                    FOLLOW @BOWLASGARAGELTD 📸
                </button>
            </a>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 6. FOOTER SECTION ---
st.markdown(f"""
    <div class="footer">
        📍 Address: 90c Red Hills Road, Kingston<br>
        📞 Phone: +1 (876) 4972031 | 📸 Instagram: @bowlasgarageltd
    </div>
    """, unsafe_allow_html=True)
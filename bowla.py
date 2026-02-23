import streamlit as st

# 1. SETTINGS & STYLE
st.set_page_config(page_title="Bowla's Garage", page_icon="🏎️")
st.markdown("<style>main {background-color: #000; color: #fff;}</style>", unsafe_allow_html=True)

# 2. THE SMART DATABASE (The "Various Lists")
# This is where we link Services to specific Models and Prices
pricing_data = {
    "Engine Tuning": {
        "M2": 30000,
        "M3": 35000,
        "M4": 35000,
        "M5": 40000,
        "M6": 40000,
        "X5M": 45000
    },
    "Full Synthetic Oil Change": {
        "M2": 15000,
        "M3": 18000,
        "M4": 18000,
        "M5": 22000,
        "M6": 22000,
        "X5M": 25000
    },
    "Brake System Overhaul": {
        "M2": 25000,
        "M3": 28000,
        "M4": 28000,
        "M5": 35000,
        "M6": 35000,
        "X5M": 38000
    }
}

# 3. THE HEADER
st.title("BOWLA'S GARAGE LTD")
st.write("📍 90C Red Hills Rd, Kingston 19")
st.divider()

# 4. THE DYNAMIC DROPDOWNS (This is what you're looking for!)

# Step A: User picks the Service
service_choice = st.selectbox("Select Service", list(pricing_data.keys()))

# Step B: The app automatically finds the Models for THAT service
available_models = list(pricing_data[service_choice].keys())

# Step C: User picks the Model from the NEW list
model_choice = st.selectbox("Select BMW Model", available_models)

# Step D: The app pulls the final price
price = pricing_data[service_choice][model_choice]

# 5. THE RESULT BOX
st.info(f"Estimate for {model_choice}: **${price:,} JMD**")

# 6. WHATSAPP BOOKING
phone = "18765105118" # Update with Bowla's number
msg = f"Hi Bowla, I'd like to book a {service_choice} for my BMW {model_choice}. Estimate: ${price:,} JMD."
url = f"https://wa.me/{phone}?text={msg.replace(' ', '%20')}"

st.link_button("🚀 Send to WhatsApp", url)
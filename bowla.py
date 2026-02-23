import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Bowla's Garage", page_icon="🏎️")

# 2. Simple Pricing Data (The Brain)
pricing_data = {
    "Engine Tuning": {"M2": 30000, "M3": 35000, "M4": 35000, "M5": 40000, "M6": 40000},
    "Oil Change": {"M2": 15000, "M3": 18000, "M4": 18000, "M5": 22000, "M6": 22000},
    "Diagnostics": {"M2": 5500, "M3": 5500, "M4": 5500, "M5": 5500, "M6": 5500}
}

# 3. Header
st.title("BOWLA'S GARAGE LTD")
st.write("📍 90C Red Hills Rd, Kingston 19")
st.divider()

# 4. Selector UI
service = st.selectbox("Select Service", list(pricing_data.keys()))
model = st.selectbox("Select BMW Model", list(pricing_data[service].keys()))
price = pricing_data[service][model]

# 5. Price Box
st.info(f"Estimated Price for {model}: ${price:,} JMD")

# 6. WhatsApp Booking
phone = "18766693455"
msg = f"Hi Bowla, I'd like to book a {service} for my BMW {model}. Estimate: ${price:,} JMD."
url = f"https://wa.me/{phone}?text={msg.replace(' ', '%20')}"

st.link_button("🚀 Send to WhatsApp", url)
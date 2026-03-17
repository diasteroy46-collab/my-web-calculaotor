import streamlit as st
import pandas as pd

# --- PAGE CONFIG (Keep it centered for mobile) ---
st.set_page_config(
    page_title="Bowla's Garage | BMW Specialist",
    page_icon="🏎️",
    layout="centered"
)

# --- M-STRIPE CSS (Original Clean Layout) ---
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
    
    /* Table Styling for better mobile reading */
    .stTable {
        font-size: 16px;
    }
    </style>
    <div class="m-stripe">
        <div class="m-blue"></div>
        <div class="m-dark-blue"></div>
        <div class="m-red"></div>
    </div>
    """, unsafe_allow_html=True)

st.title("🛠️ Bowla's Garage")
st.write("### BMW Specialist | 90C Red Hills Road")

st.markdown("---")
st.write("## 📜 Official Service Pricing (JMD)")

# --- DATA FROM SECRETARY'S LIST ---
# Grouped by Basic vs Regular just like her sheet
pricing_data = {
    "Service Item": ["Oil filter", "Air filter", "Labour", "---", "TOTAL"],
    "N20": ["$2,800", "$5,000", "$14,500", "---", "$43,300"],
    "N55": ["$2,800", "$5,000", "$14,500", "---", "$46,300"],
    "B48": ["$3,500", "$8,000", "$15,500", "---", "$53,000"],
    "B58": ["$5,000", "$8,000", "$15,500", "---", "$57,500"]
}

df = pd.DataFrame(pricing_data)
st.table(df)

st.markdown("---")

# --- CLEAN BOOKING SECTION ---
st.write("### 📅 Book an Appointment")
name = st.text_input("Customer Name")
car = st.text_input("Car Model (e.g. 320i, M140i)")

# UPDATE THIS NUMBER TO THE OFFICIAL GARAGE LINE
garage_phone = "1876XXXXXXX" 

msg = f"Hi Bowla's Garage, I'm {name}. I saw the price list for my {car} and I'd like to book a service."
wa_url = f"https://wa.me/{garage_phone}?text={msg.replace(' ', '%20')}"

if st.button("Message on WhatsApp"):
    if name and car:
        st.markdown(f'<meta http-equiv="refresh" content="0;URL={wa_url}">', unsafe_allow_html=True)
    else:
        st.error("Please enter your name and car model.")

st.info("Note: Prices include oil and parts as per the official 2026 service menu.")
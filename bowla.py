import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Bowla's Garage | BMW Specialist",
    page_icon="https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg",
    layout="centered"
)

# --- THE G80 BACKGROUND & BMW M-STRIPES ---
st.markdown("""
    <style>
    /* THE G80 M3 BACKGROUND */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1617814076367-b759c7d7e738");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Dark overlay so the car looks mean but text is 100% readable */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.82); 
        z-index: -1;
    }

    /* Official M-Stripe logic */
    .m-stripe {
        height: 12px;
        width: 100%;
        display: flex;
        margin-bottom: 25px;
    }
    .m-blue { background-color: #0033AD; flex: 1; }
    .m-dark-blue { background-color: #001C57; flex: 1; }
    .m-red { background-color: #E7222E; flex: 1; }
    
    /* Ensuring all text and tables pop in White */
    h1, h2, h3, p, span, .stMarkdown, .stTable td, .stTable th {
        color: white !important;
    }
    </style>
    
    <div class="m-stripe">
        <div class="m-blue"></div>
        <div class="m-dark-blue"></div>
        <div class="m-red"></div>
    </div>
    """, unsafe_allow_html=True)

# --- HEADER WITH BMW LOGO ---
col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg", width=70)
with col_title:
    st.title("Bowla's Garage Service Menu")

st.write("### BMW Specialist | 90C Red Hills Road")
st.markdown("---")

# --- BASIC SERVICE TABLE ---
st.write("### 🔹 BASIC F30 (Oil & Filter Only)")
basic_data = {
    "Item": ["5-7qrts Oil", "Oil Filter", "Labour", "TOTAL"],
    "N20": ["$15,000", "$2,800", "$10,000", "**$32,800**"],
    "N55": ["$18,000", "$2,800", "$10,000", "**$35,800**"],
    "B48": ["$18,000", "$3,500", "$10,000", "**$39,500**"],
    "B58": ["$21,000", "$5,000", "$10,000", "**$44,000**"]
}
st.table(pd.DataFrame(basic_data))

# --- REGULAR SERVICE TABLE ---
st.write("### 🔸 REGULAR F30 (Full Service)")
reg_data = {
    "Item": ["Air Filter", "Cabin Filter", "Labour", "TOTAL"],
    "N20": ["$5,000", "$6,000", "$14,500", "**$43,300**"],
    "N55": ["$5,000", "$6,000", "$14,500", "**$46,300**"],
    "B48": ["$8,000", "$8,000", "$15,500", "**$53,000**"],
    "B58": ["$8,000", "$8,000", "$15,500", "**$57,500**"]
}
st.table(pd.DataFrame(reg_data))

st.markdown("---")

# --- WHATSAPP BOOKING SECTION ---
st.write("### 📅 Book an Appointment")
customer_name = st.text_input("Enter your name")
car_model = st.text_input("Car Model (e.g. M340i)")

# Replace with the official garage number (e.g. 18761234567)
garage_phone = "18764972031" 

msg = f"Hello Bowla's Garage, my name is {customer_name}. I'd like to book a service for my {car_model}."
wa_url = f"https://wa.me/{garage_phone}?text={msg.replace(' ', '%20')}"

if customer_name and car_model:
    st.link_button("🟢 Message on WhatsApp", wa_url, use_container_width=True)
else:
    st.button("Message on WhatsApp (Enter details first)", disabled=True, use_container_width=True)

st.markdown("---")
st.caption("Prices are estimates and subject to parts availability. © 2026 Bowla's Garage")
import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Bowla's Garage | BMW Specialist",
    page_icon="🏎️",
    layout="centered"
)

# --- BMW M-STRIPES & CLEAN STYLING ---
st.markdown("""
    <style>
    /* Professional Dark Theme */
    .stApp {
        background-color: #0E1117;
    }

    /* M-Stripe logic */
    .m-stripe {
        height: 12px;
        width: 100%;
        display: flex;
        margin-bottom: 25px;
    }
    .m-blue { background-color: #0033AD; flex: 1; }
    .m-dark-blue { background-color: #001C57; flex: 1; }
    .m-red { background-color: #E7222E; flex: 1; }
    
    /* Ensure all text is crisp and clear */
    h1, h2, h3, p, span, .stMarkdown {
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

st.info("📍 BMW Specialist | 90C Red Hills Road")
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

# --- CONTACT & SOCIALS ---
st.write("### 📍 Location & Socials")

# Official Garage Details
garage_phone = "18764972031" # Replace with Bowla's real number
ig_handle = "bowlas_garage" # Replace with real IG handle
# Official Google Maps link for 90C Red Hills Road
google_maps_url = "https://www.google.com/maps/search/?api=1&query=Bowlas+Garage+Ltd+90c+Red+Hills+Rd+Kingston"

# Three Clean Buttons (WhatsApp, Instagram, and Map)
col1, col2, col3 = st.columns(3)

with col1:
    if customer_name and car_model:
        msg = f"Hello Bowla's Garage, my name is {customer_name}. I'd like to book for my {car_model}."
        wa_url = f"https://wa.me/{garage_phone}?text={msg.replace(' ', '%20')}"
        st.link_button("🟢 WhatsApp", wa_url, use_container_width=True)
    else:
        st.button("🟢 WhatsApp", disabled=True, use_container_width=True)

with col2:
    st.link_button("📸 Instagram", f"https://instagram.com/{ig_handle}", use_container_width=True)

with col3:
    st.link_button("📍 View Map", google_maps_url, use_container_width=True)

st.markdown("---")

# --- THE ESTIMATE REMINDER ---
st.warning("""
**Please Note:** All prices listed are **estimates** based on current market rates for parts and fluids. 
Final pricing may vary depending on parts availability or additional work required.
""", icon="⚠️")

st.caption(f"© 2026 Bowla's Garage | 90C Red Hills Road | @{ig_handle}")
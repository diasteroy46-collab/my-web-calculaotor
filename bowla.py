import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Bowla's Garage | BMW Specialist",
    page_icon="🏎️",
    layout="wide" 
)

# --- STEALTH G80 BACKGROUND & TABLE STYLING ---
st.markdown("""
    <style>
    /* Pure black background for maximum readability */
    .stApp {
        background-color: #000000;
        background-image: 
            linear-gradient(90deg, #000000 0%, rgba(0,0,0,0.4) 50%, rgba(0,0,0,0) 100%),
            url("https://images.unsplash.com/photo-1627883584732-f2df2df555f3"); 
        background-size: auto, cover;
        background-position: left, right center;
        background-repeat: no-repeat;
        background-attachment: fixed;
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
    
    /* High-contrast white text */
    h1, h2, h3, p, span, .stMarkdown, .stTable td, .stTable th {
        color: white !important;
        font-family: 'Arial', sans-serif;
    }

    /* Table styling for dark mode */
    .stTable {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
    }
    </style>
    
    <div class="m-stripe">
        <div class="m-blue"></div>
        <div class="m-dark-blue"></div>
        <div class="m-red"></div>
    </div>
    """, unsafe_allow_html=True)

# --- HEADER ---
col_logo, col_title = st.columns([1, 6])
with col_logo:
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg", width=60)
with col_title:
    st.title("Bowla's Garage Service Menu")

st.write("### BMW Specialist | 90C Red Hills Road")
st.markdown("---")

# --- TABLES ---
col_content, col_spacer = st.columns([3, 2])
with col_content:
    st.write("## 🔹 BASIC F30 (Oil & Filter Only)")
    basic_data = {
        "Item": ["5-7qrts Oil", "Oil Filter", "Labour", "TOTAL"],
        "N20": ["$15,000", "$2,800", "$10,000", "$32,800"],
        "N55": ["$18,000", "$2,800", "$10,000", "$35,800"],
        "B48": ["$18,000", "$3,500", "$10,000", "$39,500"],
        "B58": ["$21,000", "$5,000", "$10,000", "$44,000"]
    }
    st.table(pd.DataFrame(basic_data))

    st.write("## 🔸 REGULAR F30 (Full Service)")
    reg_data = {
        "Item": ["Air Filter", "Cabin Filter", "Labour", "TOTAL"],
        "N20": ["$5,000", "$6,000", "$14,500", "$43,300"],
        "N55": ["$5,000", "$6,000", "$14,500", "$46,300"],
        "B48": ["$8,000", "$8,000", "$15,500", "$53,000"],
        "B58": ["$8,000", "$8,000", "$15,500", "$57,500"]
    }
    st.table(pd.DataFrame(reg_data))

st.markdown("---")

# --- WHATSAPP ---
st.write("### 📅 Book an Appointment")
c_name = st.text_input("Name")
c_car = st.text_input("Car Model")

# Use official number (e.g. 1876...)
garage_phone = "18764672031" 

if c_name and c_car:
    msg = f"Hello Bowla's Garage, my name is {c_name}. I'd like to book for my {c_car}."
    wa_url = f"https://wa.me/{garage_phone}?text={msg.replace(' ', '%20')}"
    st.link_button("🟢 Message on WhatsApp", wa_url, use_container_width=True)

st.caption("© 2026 Bowla's Garage")
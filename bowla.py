import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bowla's Garage", page_icon="🏎️", layout="centered")

# --- BMW M-STRIPES ---
st.markdown("""
    <style>
    .m-stripe { height: 10px; width: 100%; display: flex; margin-bottom: 20px; }
    .m-blue { background-color: #0033AD; flex: 1; }
    .m-dark-blue { background-color: #001C57; flex: 1; }
    .m-red { background-color: #E7222E; flex: 1; }
    </style>
    <div class="m-stripe">
        <div class="m-blue"></div><div class="m-dark-blue"></div><div class="m-red"></div>
    </div>
    """, unsafe_allow_html=True)

st.title("🛠️ Bowla's Garage Service Menu")
st.info("BMW Specialist | 90C Red Hills Road")

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
# Booking section remains the same...
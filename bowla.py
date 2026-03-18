import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_config(
    page_title="Bowla's Garage | BMW Specialist",
    page_icon="🏎️",
    layout="wide" # 'wide' allows us to position the headlights on the right
)

# --- STEALTH G80 BACKGROUND & TABLE STYLING ---
# Inspo: image_11.png (Stealthy, high-contrast, black G80 lights)
st.markdown("""
    <style>
    /* STEALTH BACKGROUND with Vignette to hide headlights under the text area */
    .stApp {
        background-color: #000000; /* Pure Black, matching image_11.png */
        background-image: 
            linear-gradient(90deg, #000000 0%, rgba(0,0,0,0.3) 60%, rgba(0,0,0,0) 100%),
            url("https://images.unsplash.com/photo-1627883584732-f2df2df555f3"); /* New Black G80 M3 Headlights shot */
        background-size: auto, cover;
        background-position: left, right center; /* Car is on the right, text on black left */
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* M-Stripe logic, keeping the official colours */
    .m-stripe {
        height: 12px;
        width: 100%;
        display: flex;
        margin-bottom: 25px;
        position: sticky;
        top: 0;
        z-index: 999;
    }
    .m-blue { background-color: #0033AD; flex: 1; }
    .m-dark-blue { background-color: #001C57; flex: 1; }
    .m-red { background-color: #E7222E; flex: 1; }
    
    /* Perfect Readability - All text is bright white and bold against pure black */
    h1, h2, h3, p, span, .stMarkdown, .stTable td, .stTable th, [data-testid="stDataFrame"] {
        color: white !important;
        font-family: 'Montserrat', sans-serif;
        font-weight: 500;
    }
    h1, h2, h3 { font-weight: 700; }

    /* Make the Table contrast pop */
    .stTable tbody tr:nth-child(even) { background-color: rgba(255, 255, 255, 0.05); }
    .stTable tbody tr:hover { background-color: rgba(255, 255, 255, 0.1); }
    </style>
    
    <div class="m-stripe">
        <div class="m-blue"></div>
        <div class="m-dark-blue"></div>
        <div class="m-red"></div>
    </div>
    """, unsafe_allow_html=True)

# --- LAYOUT FOR HEADERS ---
col_logo, col_title = st.columns([1, 6])
with col_logo:
    # Official BMW logo
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg", width=60)
with col_title:
    st.title("Bowla's Garage Service Menu")

st.write("### BMW Specialist | 90C Red Hills Road")
st.markdown("---")

# --- CONSTRAIN TABLES TO THE LEFT-SIDE PURE BLACK SPACE ---
col_content, col_spacer = st.columns([3, 2])
with col_content:
    # --- BASIC SERVICE TABLE ---
    st.write("## 🔹 BASIC F30 (Oil & Filter Only)")
    basic_data = {
        "Item": ["5-7qrts Oil", "Oil Filter", "Labour", "TOTAL"],
        "N20": ["$15,000", "$2,800", "$10,000", "$32,800"],
        "N55": ["$18,000", "$2,800", "$10,000", "$35,800"],
        "B48": ["$18,000", "$3,500", "$10,000", "$39,500"],
        "B58": ["$21,000", "$5,000", "$10,000", "$44,000"]
    }
    st.table(pd.DataFrame(basic_data).set_index("Item"))

    # --- REGULAR SERVICE TABLE ---
    st.write("## 🔸 REGULAR F30 (Full Service)")
    reg_data = {
        "Item": ["Air Filter", "Cabin Filter", "Labour", "TOTAL"],
        "N20": ["$5,000", "$6,000", "$14,500", "$43,300"],
        "N55": ["$5,000", "$6,000", "$14,500", "$46,300"],
        "B48": ["$8,000", "$8,000", "$15,500", "$53,000"],
        "B58": ["$8,000", "$8,000", "$15,500", "$57,500"]
    }
    st.table(pd.DataFrame(reg_data).set_index("Item"))

st.markdown("---")

# --- WHATSAPP BOOKING SECTION (Matching wide layout) ---
st.write("### 📅 Book an Appointment")
# Constrain input width
col_inputs, col_wa_spacer = st.columns([1, 1])
with col_inputs:
    customer_name = st.text_input("Enter your name", placeholder="e.g. Teroy")
    car_model = st.text_input("Car Model", placeholder="e.g. M3 Competition")

# Use official numbers (no XXXXXXX)
garage_phone = "18764972031" 

msg = f"Hello Bowla's Garage, my name is {customer_name}. I'd like to book a service for my {car_model} from your website."
wa_url = f"https://wa.me/{garage_phone}?text={msg.replace(' ', '%20')}"

st.markdown("<br>", unsafe_allow_html=True)

if customer_name and car_model:
    st.link_button("🟢 Message on WhatsApp", wa_url, use_container_width=True)
else:
    st.button("Message on WhatsApp (Enter details first)", disabled=True, use_container_width=True)

st.markdown("---")
st.caption("Prices are estimates and subject to parts availability. © 2026 Bowla's Garage")
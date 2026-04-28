import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime


# Sample Products
products = {
    "AMOXIL V": {"PC", "BOX"},
    "ELEC V": {"PC", "BOX"},
    "NOROVIT": {"10ML", "50ML", "100ML"},
    "PPG": {"SACHET", "BOX"},
    "FEATHERSHINE": {"SACHET", "BOX"},
    "WORM X": {"PAD", "BOX"},
    "WORM X MAXX": {"PAD", "BOX"},
    "-- OTHERS --" : {},
    "DOXA-V" : {"PC", "BOX", "BOTTLE", "PAD"},
    "PARA-V" : {"PC", "BOX", "BOTTLE", "PAD"},
    "TRIMAX" : {"PC", "BOX", "BOTTLE", "PAD"},
    "MULTIMAX" : {"PC", "BOX", "BOTTLE", "PAD"},
    "ELECTROMAX" : {"PC", "BOX", "BOTTLE", "PAD"},
    "MULTIMAX D5" : {"PC", "BOX", "BOTTLE", "PAD"},
    "DOX-C-LIN GOLD" : {"PC", "BOX", "BOTTLE", "PAD"},
    "DOX-C-TRIN GOLD" : {"PC", "BOX", "BOTTLE", "PAD"},
    "WORM-X MAXX" : {"PC", "BOX", "BOTTLE", "PAD"},
    "IRON-VET" : {"PC", "BOX", "BOTTLE", "PAD"},
    "BULATIGOK SD" : {"PC", "BOX", "BOTTLE", "PAD"},
    "TRIFAST" : {"PC", "BOX", "BOTTLE", "PAD"},
    "ALAMYCIN LA" : {"PC", "BOX", "BOTTLE", "PAD"}
}

stores = {
    "B AND E AGRIVET SUPPLY & VETERINARY SERVICES",
    "GWYN AGRIVET SUPPLIES & PET CARE SERVICES",
    "NIX ANIMAL CENTRE (AHPC)",
    "PACIFICA AGRIVET SUPPLIES, INC. - CARIGARA (AHPC)",
    "ROYAL EMPYREAN BREEDER",
    "3 KING'S AGRIVET SUPPLIES",
    "4J'S AGRIVET TRADING",
    "4M'S TUANG RICE STORE",
    "4R'S STORE",
    "5M AGRIVET",
    "5R'S STORE",
    "A & G BERCERO AGRIVET",
    "A & J AGRIVET SUPPLY",
    "A & N AGRIVET SUPPLY",
    "A.I.R. AGRIVET SUPPLY",
    "AB FARMERS AGRIVET SUPPLY",
    "ACF AGRIVET",
    "AGRIVET KO",
    "AILEEN'S STORE",
    "AJ BORNE AGRIVET SUPPLY",
    "AKIO'S AGRIVET SUPPLY",
    "ALARIC AGULLO",
    "ALICANDO VARIETY",
    "ALICE ARIAS",
    "ALMA DIPAD",
    "ALRENCE AGRIVET TRADING",
    "ANGELO VICENTE",
    "ANTONI'S AGRIVET SUPPLY",
    "ARA AGRICULTURAL PRODUCTS TRADING",
    "ARNEL BOSTILLO",
    "ARNOLD IMPRESO",
    "ARTURO BERINGUEL",
    "ATN AGRIVET SUPPLY",
    "BAKALA AGRIVET",
    "BELEN STORE",
    "BELINDA STORE",
    "BEN ANTHONY DADULA",
    "BENJIE SARI-SARI STORE",
    "BENSOI STORE",
    "BGT AGRIVET - ALANG ALANG",
    "BGT AGRIVET - PALO",
    "BLAYNE AGRIVET SUPPLY",
    "BLUEDOY LANANTI",
    "C AND J AGRIVET TRADING",
    "CABELLO AGRIVET SUPPLY",
    "CALIX YANSY VARIETY STORE",
    "CATHERINE P. GARRIDO",
    "CED VARIETY STORE",
    "CHELZ GEN. MERCHANDISE",
    "CHERRY'S STORE",
    "CHRISTIAN PHILIP ESQUADRA MIRALLES",
    "CIANYANA AGRIVET TRADING",
    "CLARIDAD AGRIVET SUPPLY",
    "CLAROS AGRIVET SUPPLY",
    "CONCEPTION RELEVO",
    "CULASIAN AGRIVET AND SUPPLIES",
    "CUTA FARMERS MULTI COOP",
    "D & E AGRIVET SUPPLY",
    "DEMAND CREATION - GEE RINOS",
    "DEMAND CREATION - JAYVEE BAGUNAS",
    "DEMAND CREATION - JEFFREY YBANEZ",
    "DEMAND CREATION - LEONEL LIBY APOR",
    "DEMAND CREATION - RECHIE APOR",
    "DEMAND CREATION ACTIVITY - LEYTE 1",
    "DENCIANG'S STORE",
    "DENSAN LIVESTOCK FARM",
    "DINA DANDAN",
    "DINA ROSENAS",
    "DJ RAISER",
    "DODONG TORENO",
    "DOFOX FLIERS AGRIVET - ABUYOG",
    "DOFOX FLIERS AGRIVET-TACLOBAN",
    "DOLORES B. VILLAFLOR",
    "DOMINGO SARI-SARI STORE",
    "DULAG AGRIVET",
    "E & R AGRIVET SUPPLIES",
    "E & V ARGUTA'S ENTERPRISES",
    "E&E LOPEZ AGRI SUPPLY",
    "EDEN'S FEEDS TRADING",
    "EDGAR DAGANASOL",
    "EDWIN ESTRALLA SABALLA",
    "EDWIN SABALLA",
    "EIVERJ LHANZ STORE",
    "ELEGIO R. BERSALES",
    "ELEVEN JAY FOX AGRICULTURAL SUPPLY",
    "ELIJAH",
    "ELISHA MINI STORE",
    "ELSIE CANMARATING",
    "FEB AGRI SUPPLY",
    "FELIMON BAGUE",
    "FRANCIS STORE",
    "FV AGRIVET SUPPLY",
    "G AND V AGRIVET",
    "GASPAR CUAYZON",
    "GCP ASTORGA GENERAL MERCHANDISE",
    "GEMINI AGRIVET",
    "GEMMA STORE",
    "GENISTO LARGO",
    "GIGIE AGRIVET - LEYTE",
    "GIL P. REBATO/ONJIE AGRIVET",
    "GIMA'S MKTG.",
    "GIRLEY TAN SANICO",
    "GLADYS VENEZUELA",
    "GLD TRUCKING",
    "GLEN ESQUIBEL",
    "GOLDEN J5 GAMEFARM",
    "GOLS AGRI TRADING",
    "GRACIE AGRIVET",
    "GREGORIO CABELTE JR.",
    "HAPPY TAILS AGRIVET SUPPLY",
    "HERMAN AYOSTE",
    "IDAY AGRIVET",
    "J & A AGRIVET",
    "J5 SOPHIA",
    "JAB'S AGRIFEEDS",
    "JAIME PACAYDE",
    "JAS SOFIA STORE",
    "JASON STORE",
    "JAZZ ENTERPRISE",
    "JEFFREY YBAÑEZ",
    "JENNY'S AGRIVET TRADING",
    "JERICO MALINDOG",
    "JERWEN B. DE PAZ",
    "JETH ALTON BERINO",
    "JIG AGRIVET SUPPLY",
    "JIMMY SEVILLA",
    "J'MARK AGRIVET",
    "JOHN JACOB SARI-SARI STORE",
    "JONATHAN ARIZA",
    "JOSEF YUCAMCO",
    "JOSEPH CLINT M. MALQUISTO",
    "JOY/JEFFREY STORE",
    "JP STORE-LEYTE",
    "JUNLICE STORE",
    "JVT AGRIVET",
    "KALANTAS ENTERPRISES",
    "KAREN'S AGRIVET SUPPLY",
    "KATRIZA STORE",
    "KAYZEIL L. BRITENIA",
    "KENNETH A. DELLORO",
    "KENNETH MORFE",
    "KER'S AGRIVET TRADING",
    "KIM JAID AGRIVET",
    "KING JUMONG AGRIVET SUPPLY",
    "KNJ AGRIVET SUPPLY",
    "KYRIC AGRIVET SUPPLY",
    "LAPAZ DIVERSIFIED FARMING AGRICULTURE COOPERATIVE",
    "LEO MAJABAGUE/JUNJIE RAMIREZ",
    "LERIO OBAOB",
    "LESTER LPG TRADING",
    "LEYSAMCO",
    "LGI",
    "LIEZEL STORE",
    "LINA BARRIENTOS",
    "LITONG AGRICULTURAL SUPPLY",
    "LJ KRIZEL STORE",
    "LLOYD NOVILLA",
    "LUCKY 3 STORE LIBERTAD",
    "MANOY AND CAYONG AGRIVET SUPPLY",
    "MARAY AGRI SUPPLY",
    "MARVIN VELARDE/MC PANIS STORE",
    "MATHEW AND JOHN ENTERPRISES",
    "MAXENE V. AGRIVET TRADING",
    "MC AGRIVET SUPPLY",
    "MDR",
    "MELANIE LUANGCO",
    "MH GENERAL MERCHANDISE",
    "MJ AGRIVET",
    "MOLABOLA STORE",
    "MRV2 AGRIVET TRADING",
    "NANCY'S RICE STORE",
    "NIEL AND DEM ENTERPRISES",
    "NL AGRIVET - TANAUAN",
    "NO WHELL AGRIVET SUPPLY",
    "NOEL PALANCA",
    "NOGAL STORE",
    "NOLERS STORE",
    "NSN AGRICULTURAL SUPPLY",
    "ORLY STORE",
    "OSCAR GALVEZ",
    "PACIFICA AGRIVET SUPPLIES INC. - CARIGARA",
    "PACIFICA AGRIVET SUPPLIES, INC. - ABUYOG",
    "PACIFICA AGRIVET SUPPLIES, INC. - BURGOS I",
    "PACIFICA AGRIVET SUPPLIES, INC. - BURGOS II",
    "PACIFICA AGRIVET SUPPLIES, INC. - PALO",
    "PACIFICA AGRIVET SUPPLIES, INC. - RIZAL TACLOBAN",
    "PACIFICA AGRIVET SUPPLIES, INC. - TACLOBAN PORT AREA",
    "PACIFICA AGRIVET SUPPLIES, INC. - TORRES",
    "PINKYS AGRIVET",
    "PIOBETH STORE",
    "PLACEMENT CAMPAIGN (FOR SAMPLING ) - LEYTE",
    "POSING AGRIVET/VILMA CABRERA",
    "POWER-FEEDS AGRIVET SUPPLIES",
    "PRINCESS STORE",
    "RAISER'S MARKETING",
    "RALH JADE POULTRY SUPPLIES",
    "RAZIEL GROCERY STORE",
    "RBD GAMEFARM",
    "RDA AGRIVET SUPPLY",
    "REAS",
    "RENE LAMPAYAN",
    "RENIK AGRIVET",
    "RETCHELIE MEDINO",
    "RICO C. MAGHINAY",
    "RJS AGRIVET",
    "ROGELIO COSTIN",
    "ROLENE ENTERPRISES",
    "ROSIES MINI MART",
    "ROWENA AGRI SUPPLY",
    "ROY GONHURAN",
    "RRD-6 AGRIVET SUPPLY",
    "SAN LORENZO STORE",
    "SETOSTA POULTRY FARM",
    "SIAPOL AGRIVET SUPPLY",
    "SOLAMO ENTERPRISES",
    "SP STORE",
    "SPARTANS GAMEFARM",
    "ST. AGUSTINE STORE",
    "ST. JUDE-CVE AGRICULTURAL MARKETING CORPORATION",
    "ST. MATTHEW AGRI TRADING",
    "SYLVIA'S VARIETY STORE",
    "TANASYO AGRIVET",
    "TARANTULA GAMEFARM",
    "TESS ARIZA",
    "THREE G ENTERPRISE",
    "THUNDER AGRIVET - LEYTE",
    "TICK-TOCK MINIMART",
    "TINDAHAN NI ANOK",
    "TINDAHAN NI MA'AM GRACE",
    "TUNGA KING'S STORE",
    "UMAHAN AGRIVET SUPPLY",
    "VERNON STORE",
    "VERSE STORE",
    "VILMA PAJO",
    "WENIE'S ENTERPRISE",
    "WHOZHAI TRADING",
    "WRH",
    "WVN AGRIVET SUPPLY",
    "YSAY'S AGRIVET",
    "ZENAIDA VERECIO",


}

# -----------SESSION-------------------
if "data" not in st.session_state:
    st.session_state.data = []

if "last_submission" not in st.session_state:
    st.session_state.last_submission = None

if "selected_product" not in st.session_state:
    st.session_state.selected_product = "-- Select Product --"
elif st.session_state.selected_product not in products:
    st.session_state.selected_product = "-- Select Product --"

if "user_role" not in st.session_state:
    st.session_state.user_role = None

if "stores" not in st.session_state:
    st.session_state.selected_store = "-- Select Store --"
elif st.session_state.selected_store not in stores:
    st.session_state.selected_store = "-- Select Store --"

if "admin_authenticated" not in st.session_state:
    st.session_state.admin_authenticated = False
# -------- END OF SESSION ------------

# -----------CONFIGURATION (Hardcoded for easy updates)--------------------
# Update these values to change credentials
ADMIN_CREDENTIALS = {
    "password": "password"  # Change this to update admin password
}
# -------- END OF CONFIGURATION ------------

st.set_page_config(layout="wide")

# -----------CSS FOR ALL CAPS INPUT & NAVY BLUE BUTTON & RESPONSIVE--------------------
st.markdown("""
<style>
    /* ===== RESPONSIVE LAYOUT ===== */
    /* Main container responsive padding */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }
    
    /* Tablet (768px - 1024px) */
    @media (max-width: 1024px) {
        .block-container {
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }
        div[data-testid="stColumn"] {
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
        }
    }
    
    /* Mobile (< 768px) */
    @media (max-width: 768px) {
        .block-container {
            padding-top: 0.5rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            padding-bottom: 0.5rem !important;
            max-width: 100% !important;
        }
        
        /* Stack columns vertically on mobile */
        div[data-testid="stHorizontalBlock"] {
            flex-direction: column !important;
        }
        
        /* Full width inputs on mobile */
        input[type="text"], input[type="number"], input[type="password"], select {
            font-size: 16px !important; /* Prevents iOS zoom on focus */
        }
        
        /* Responsive card containers */
        .responsive-card {
            padding: 15px !important;
            margin-bottom: 15px !important;
        }
        
        .responsive-card h2 {
            font-size: 1.2em !important;
        }
        
        .responsive-card p {
            font-size: 0.85em !important;
        }
        
        /* Adjust radio buttons to stack vertically on mobile */
        div[data-testid="stRadio"] > div {
            flex-direction: column !important;
        }
        
        /* Responsive metrics */
        div[data-testid="stMetric"] {
            margin-bottom: 1rem !important;
        }
        
        /* Hide expander arrow on mobile for cleaner look */
        div[data-testid="stExpander"] button {
            padding: 0.5rem !important;
        }
        
        /* Role indicator full width on mobile */
        div[data-testid="stAlertContainer"] {
            width: 100% !important;
        }
        
        /* Full width columns on mobile */
        div[data-testid="stColumn"] {
            flex: 1 1 100% !important;
            max-width: 100% !important;
        }
    }
    
    /* Small Mobile (< 480px) */
    @media (max-width: 480px) {
        .block-container {
            padding-top: 0.25rem !important;
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
            padding-bottom: 0.25rem !important;
        }
        
        .responsive-card {
            padding: 10px !important;
        }
        
        .responsive-card h2 {
            font-size: 1em !important;
        }
        
        /* Smaller buttons on mobile */
        div.stButton > button {
            padding: 0.4rem 0.8rem !important;
            font-size: 0.9em !important;
        }
        
        /* Reduce spacing between elements */
        div[data-testid="stVerticalBlock"] > div {
            margin-bottom: 0.5rem !important;
        }
    }
    
    /* Force all text inputs to display as uppercase */
    input[type="text"], input[type="number"]{
        text-transform: uppercase !important;
    }
    /* Also style Streamlit's specific input styling */
    .stTextInput input, .stNumberInput input {
        text-transform: uppercase !important;
    }
    /* Navy blue ALL buttons */
    div.stButton > button {
        background-color: #001F3F !important;
        color: white !important;
        border: 2px solid #003366 !important;
        font-weight: 600 !important;
    }
    div.stButton > button:hover {
        background-color: #003366 !important;
        border-color: #005599 !important;
        color: white !important;
    }
    div.stButton > button:active, div.stButton > button:focus {
        background-color: #003366 !important;
        border-color: #005599 !important;
        color: white !important;
    }
    
    /* Responsive card class */
    .responsive-card {
        background-color: #1e1e2f;
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #333;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)
# -------- END OF CSS ------------

st.markdown("""
<style>
    .centered-title {
        text-align: center;
        margin-bottom: 0.2rem;
    }
    .centered-subtitle {
        text-align: center;
        color: #888;
        margin-top: 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="centered-title">Sales Portal</h1>',
            unsafe_allow_html=True)
st.markdown('<p class="centered-subtitle">SMAHC Pullout Sales</p>',
            unsafe_allow_html=True)

# -----------GOOGLE SHEETS CONNECTION--------------------
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    # Read existing data to show (only for admin)
    try:
        existing_data = conn.read(
            worksheet="Data", usecols=list(range(7)), ttl=5)
        existing_data = existing_data.dropna(how="all")
    except Exception:
        existing_data = pd.DataFrame()
except Exception:
    st.error(
        "⚠️ Failed to connect to Google Sheets. Check your secrets.toml configuration.")
    existing_data = pd.DataFrame()

# -----------ROLE SELECTION--------------------
if st.session_state.user_role is None:
    st.markdown("<br>", unsafe_allow_html=True)

    # Responsive login form style container
    st.markdown("""
    <style>
    /* Base styles */
    .login-container {
        max-width: 500px;
        width: 90%;
        margin: 2rem auto;
        padding: 30px;
        background-color: #1e1e2f;
        border-radius: 12px;
        border: 1px solid #333;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }
    .login-container h2 {
        text-align: center;
        margin-bottom: 5px;
        font-size: 1.8rem;
    }
    .login-container p {
        text-align: center;
        color: #888;
        margin-top: 0;
        font-size: 0.95rem;
    }
    
    /* Radio button styling */
    .role-selector {
        width: 100%;
        margin: 20px 0;
    }
    
    /* Button styling */
    .login-container .stButton > button {
        width: 100%;
        margin-top: 10px;
    }

    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .login-container {
            width: 95%;
            padding: 20px 15px;
            margin: 1rem auto;
        }
        .login-container h2 {
            font-size: 1.4rem;
        }
        .login-container p {
            font-size: 0.85rem;
        }
    }

    @media (max-width: 480px) {
        .login-container {
            width: 95%;
            padding: 15px 10px;
            border-radius: 8px;
        }
        .login-container h2 {
            font-size: 1.2rem;
            margin-bottom: 10px;
        }
        .login-container p {
            font-size: 0.8rem;
        }
    }

    /* Tablet responsiveness */
    @media (min-width: 769px) and (max-width: 1024px) {
        .login-container {
            max-width: 450px;
            padding: 25px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='login-container'>
    <h2>🔐 Select Your Access Level</h2>
    <p style='color: #888;'>Please choose your role to continue</p>
    </div>
    """, unsafe_allow_html=True)

    # Role selection - responsive columns
    # On mobile: full width, on desktop: centered
    col1, col2, col3 = st.columns([1, 1, 1], vertical_alignment="center")
    with col2:
        # Use horizontal radio on desktop, vertical on mobile
        role = st.radio(
            "I am a:",
            ["👤 User (Add Transactions)", "👨‍ Admin (View All)"],
            index=0,
            horizontal=True,
            label_visibility="collapsed",
            key="role_selection",
        )

        if st.button("Continue", use_container_width=True, type="primary"):
            if "Admin" in role:
                st.session_state.user_role = "admin_pending"
            else:
                st.session_state.user_role = "user"
            st.rerun()
    st.stop()

# Admin password verification
if st.session_state.user_role == "admin_pending":
    if st.session_state.admin_authenticated:
        st.session_state.user_role = "admin"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Centered admin login form style
    st.markdown("""
    <div class='login-container'>
    <h2 style='margin-bottom: 5px;'>🔒 Admin Authentication Required</h2>
    <p style='color: #888; margin-top: 0;'>Enter your admin password to continue</p>
    </div>
    """, unsafe_allow_html=True, text_alignment="center")

    col_login1, col_login2, col_login3 = st.columns([1, 2, 1])
    with col_login2:
        admin_password = st.text_input(
            "Enter Admin Password", type="password", placeholder="Enter password")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔓 Verify & Continue", use_container_width=True, type="primary"):
                if admin_password == ADMIN_CREDENTIALS["password"]:
                    st.session_state.admin_authenticated = True
                    st.session_state.user_role = "admin"
                    st.success("✅ Access granted!")
                    st.rerun()
                else:
                    st.error(
                        "❌ Incorrect password. Please try again or select User mode.")
        with col2:
            if st.button("← Back", use_container_width=True):
                st.session_state.user_role = None
                st.rerun()
    st.stop()

# Show role indicator and logout button
col1, col2 = st.columns([3, 1])
with col1:
    if st.session_state.user_role == "admin":
        st.info("👨‍💼 **Admin Mode** - You can view all transactions")
    else:
        st.info("👤 **User Mode** - You can add transactions and view your session")

with col2:
    if st.button("🚪 Switch Role"):
        st.session_state.user_role = None
        st.session_state.admin_authenticated = False
        st.session_state.data = []
        st.session_state.selected_product = "-- Select Product --"
        st.session_state.selected_store = "-- Select Store --"
        st.rerun()

st.divider()

# -----------ADMIN VIEW: Summary Panels-------------------
if st.session_state.user_role == "admin":
    if not existing_data.empty:
        df = existing_data.copy()

        # Summary of Names (FAT's or GFS)
        st.markdown("""
        <div class='responsive-card'>
        <h2 style='margin-bottom: 2px; font-size: 1.5em;'>📊 Summary by Name</h2>
        <p style='color: #888; margin-top: 0; font-size: 0.9em;'>Total transactions per user</p>
        </div>
        """, unsafe_allow_html=True)

        if "Name" in df.columns:
            name_summary = df.groupby("Name").agg({
                "Timestamp": "count",
                "Qty": "sum"
            }).reset_index()
            name_summary.columns = ["Name", "Total Transactions", "Total Qty"]
            st.dataframe(name_summary, use_container_width=True)
        else:
            st.warning("Name column not found in data")

        st.divider()

        # Summary of Store Names
        st.markdown("""
        <div class='responsive-card'>
        <h2 style='margin-bottom: 2px; font-size: 1.5em;'>🏪 Summary by Store</h2>
        <p style='color: #888; margin-top: 0; font-size: 0.9em;'>Total transactions per store</p>
        </div>
        """, unsafe_allow_html=True)

        if "Store Name" in df.columns:
            store_summary = df.groupby("Store Name").agg({
                "Timestamp": "count",
                "Qty": "sum"
            }).reset_index()
            store_summary.columns = ["Store Name",
                                     "Total Transactions", "Total Qty"]
            st.dataframe(store_summary, use_container_width=True)
        else:
            st.warning("Store Name column not found in data")

        st.divider()

        # Product Summary
        st.markdown("""
        <div class='responsive-card'>
        <h2 style='margin-bottom: 2px; font-size: 1.5em;'>📦 Summary by Product</h2>
        <p style='color: #888; margin-top: 0; font-size: 0.9em;'>Total quantity per product and UOM</p>
        </div>
        """, unsafe_allow_html=True)

        if "Product" in df.columns and "Qty" in df.columns and "UOM" in df.columns:
            product_summary = df.groupby(["Product", "UOM"])[
                "Qty"].sum().reset_index()
            product_summary.columns = ["Product", "UOM", "Total Qty"]
            st.dataframe(product_summary, use_container_width=True)
        else:
            st.warning("Product/Qty/UOM columns not found in data")

        st.divider()

        # All Transactions
        st.markdown("""
        <div class='responsive-card'>
        <h2 style='margin-bottom: 2px; font-size: 1.5em;'>📋 All Transactions</h2>
        <p style='color: #888; margin-top: 0; font-size: 0.9em;'>Complete transaction history</p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("🔍 View All Transactions"):
            st.dataframe(df, use_container_width=True)
    else:
        st.info("No transactions yet.")

# -----------USER VIEW: Transaction Entry Forms-------------------
else:
    # -----------USER & STORE INFO-------------------
    st.markdown("""
    <div class='responsive-card'>
    <h2 style='margin-bottom: 5px;'>👤 User & Store Info</h2>
    <p style='color: #888; margin-top: 0;'>Enter your details below</p>
    </div>
    """, unsafe_allow_html=True)

    # Radio buttons for user type - placed beside the text input
    col_type, col_empty = st.columns([2, 3])
    with col_type:
        user_type = st.radio(
            "User Type *",
            ["FAT's", "GFS", "DCAT"],
            horizontal=True,
            label_visibility="collapsed"
        )

    col1, col2 = st.columns([2, 2])
    with col1:
        user_name = st.text_input(
            "Name *", placeholder="Enter Full Name").upper()
    with col2:
        selected_store = st.selectbox(
            "SUKING TINDAHAN *", ["-- Select Store --"] + list(stores),
            index=0 if st.session_state.selected_store == "-- Select Store --"
            else list(stores).index(st.session_state.selected_store) + 1
            )
        if selected_store != st.session_state.selected_store:
            st.session_state.selected_store = selected_store

        
    st.divider()

    # -----------PRODUCT SELECTION (Outside Form)-------------------
    st.markdown("""
    <div class='responsive-card'>
    <h2 style='margin-bottom: 5px;'>📦 Select Product</h2>
    <p style='color: #888; margin-top: 0;'>Choose a product to add</p>
    </div>
    """, unsafe_allow_html=True)

    selected_product = st.selectbox(
        "Product *", ["-- Select Product --"] + list(products.keys()),
        index=0 if st.session_state.selected_product == "-- Select Product --" or "-- OTHERS --"
        else list(products.keys()).index(st.session_state.selected_product) + 1
    )

    # Update session state when product changes
    if selected_product != st.session_state.selected_product:
        st.session_state.selected_product = selected_product
        st.rerun()

    # -----------ENTER TRANSACTION FORM-------------------
    st.markdown("""
    <div class='responsive-card'>
    <h2 style='margin-bottom: 5px;'>🛒 Enter Quantity & Unit</h2>
    <p style='color: #888; margin-top: 0;'>Fill in the quantity & unit details</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("transaction_form", clear_on_submit=True):
        # Display selected product (read-only)
        st.markdown(f"**Product:** {st.session_state.selected_product}")
        quantity = st.number_input("Quantity *", min_value=1, step=1)

        # Filter units based on selected product
        if st.session_state.selected_product != "-- Select Product --":
            valid_units = sorted(products[st.session_state.selected_product])
            unit_options = ["-- Select Unit --"] + valid_units
        else:
            unit_options = ["-- Select Unit --"]

        selected_uom = st.selectbox("Unit *", unit_options)

        submitted = st.form_submit_button(
            "Submit Sales", use_container_width=True, type="primary")

    # -----------FORM SUBMISSION-------------------
    if submitted:
        errors = []

        # Validation
        if not user_name.strip():
            errors.append("Name is required")
        if not user_type:
            errors.append("User type is required")
        if not selected_store.strip():
            errors.append("Store name is required")
        if selected_product == "-- Select Product --":
            errors.append("Please select a product")
        if selected_uom == "-- Select Unit --":
            errors.append("Please select a unit")
        if quantity <= 0:
            errors.append("Quantity must be greater than 0")
        if selected_product != "-- Select Product --" and selected_uom != "-- Select Unit --" and selected_uom not in products.get(selected_product, set()):
            errors.append(
                f"Invalid UOM '{selected_uom}' for product '{selected_product}'")

        if errors:
            for e in errors:
                st.error(f"⚠️ {e}")
        else:
            # Create transaction record
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction = {
                "Timestamp": timestamp,
                "User Type": user_type,
                "Name": user_name.strip().upper(),
                "Store Name": selected_store.strip().upper(),
                "Product": selected_product.upper(),
                "Qty": quantity,
                "UOM": selected_uom.upper()
            }

            # Add to session state
            st.session_state.data.append(transaction)

            # Push to Google Sheets
            try:
                # Read current data
                current_data = conn.read(
                    worksheet="Data", usecols=list(range(7)), ttl=5)
                current_data = current_data.dropna(how="all")

                # Create new row
                new_row = pd.DataFrame([transaction])

                # Append and update
                if current_data.empty:
                    updated_data = new_row
                else:
                    updated_data = pd.concat(
                        [current_data, new_row], ignore_index=True)

                conn.update(worksheet="Data", data=updated_data)
                st.success(f"✅ Transaction added and synced to Google Sheets!")
            except Exception as e:
                st.warning(
                    f"✅ Transaction added locally, but failed to sync to Google Sheets: {str(e)}")

            # Update last submission timestamp to trigger rerun
            st.session_state.last_submission = timestamp

    # -----------USER TRANSACTION LIST-------------------
    st.divider()
    st.subheader("📋 Your Session Transactions")

    if st.session_state.data:
        df = pd.DataFrame(st.session_state.data)
        st.dataframe(df, use_container_width=True)

        # Show summary
        st.subheader("📊 Your Session Summary")
        if "Product" in df.columns and "Qty" in df.columns and "UOM" in df.columns:
            summary = df.groupby(["Product", "UOM"])["Qty"].sum().reset_index()
            summary.columns = ["Product", "UOM", "Total Qty"]
            st.dataframe(summary, use_container_width=True)

        # End Session button after summary
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔒 End Session", use_container_width=True, type="secondary"):
            st.session_state.data = []
            st.session_state.selected_product = "-- Select Product --"
            st.success("✅ Session ended. All session data has been cleared.")
            st.rerun()
    else:
        st.info(
            "No transactions in this session yet. Add your first transaction above!")

# -----------GOOGLE FORM DATA VIEWER (Admin Only)-------------------
if st.session_state.user_role == "admin":
    st.divider()
    st.subheader("📝 Google Form Submissions")
    st.caption("Live data from Google Form submissions")

    if not existing_data.empty:
        # Add expand/collapse toggle
        with st.expander("🔍 View All Form Submissions"):
            st.dataframe(existing_data, use_container_width=True)

        # Show quick stats
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Submissions", len(existing_data))
        with col2:
            if "Product" in existing_data.columns:
                unique_products = existing_data["Product"].nunique()
                st.metric("Unique Products", unique_products)
            else:
                st.metric("Unique Products", "N/A")
        with col3:
            if "Timestamp" in existing_data.columns:
                latest = pd.to_datetime(existing_data["Timestamp"]).max()
                st.metric("Latest Submission", latest.strftime("%m/%d %H:%M"))
            else:
                st.metric("Latest Submission", "N/A")

        # Add responsive spacing for mobile
        st.markdown("""
        <style>
        @media (max-width: 768px) {
            div[data-testid="stMetric"] {
                margin-bottom: 1rem !important;
            }
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.info("No Google Form submissions yet.")

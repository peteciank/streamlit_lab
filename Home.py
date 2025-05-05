import streamlit as st

st.cache_data.clear()

# ---------- Home ------------------------
home = st.Page("pages/home/home_style.py", title="Streamlit Lab", icon=":material/home:")



# ---------- Columns and organizers ----------
col_size = st.Page("pages/orgs/col_size.py", title="Columns Sizing", icon=":material/toggle_on:")

# ---------- DB -------------------
db_start = st.Page("pages/db/bi/src/app.py", title="DB", icon=":material/database:")



# ---------- NAVIGATION ----------
pg = st.navigation(
    {
        "Home": [home],
        "Organizers": [col_size],
        "DB": [db_start],
    }, position="sidebar"
)

pg.run()
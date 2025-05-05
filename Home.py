import streamlit as st

st.cache_data.clear()

# ---------- Home ------------------------
home = st.Page("pages/home/home_style.py", title="Streamlit Lab", icon=":material/home:")



# ---------- Columns and organizers ----------
col_size = st.Page("pages/orgs/col_size.py", title="Columns Sizing", icon=":material/toggle_on:")

# ---------- DB -------------------
db_start = st.Page("pages/db/bi/src/app.py", title="DB", icon=":material/database:")
db_api = st.Page("pages/db/bi/src/api.py", title="API", icon=":material/database:")
db_call_api = st.Page("pages/db/bi/src/call_api.py", title="Call API", icon=":material/database:")
db_upload = st.Page("pages/db/bi/src/upload_data.py", title="Upload Data", icon=":material/database:")


# ----------- Styling -------------------------
data_app = st.Page("pages/styling/superapp.py", title="Data Management", icon=":material/database:")
counter = st.Page("pages/styling/counter.py", title="DB", icon=":material/database:")



# ---------- NAVIGATION ----------
pg = st.navigation(
    {
        "Home": [home],
        "Organizers": [col_size],
        "DB": [db_start, db_api, db_call_api, db_upload],
        #"Styling": [data_app, counter],
    }, position="sidebar"
)

pg.run()
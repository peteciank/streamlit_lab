import streamlit as st

st.cache_data.clear()

# ---------- Home ------------------------
home = st.Page("pages/home/home_style.py", title="Streamlit Lab", icon=":material/home:")



# ---------- Columns and organizers ----------
col_size = st.Page("pages/orgs/col_size.py", title="Columns Sizing", icon=":material/toggle_on:")

# ---------- DB -------------------
db_start = st.Page("pages/db/bi/src/app.py", title="DB", icon=":material/database:")
db_api = st.Page("pages/db/bi/src/api.py", title="API", icon=":material/database:")
db_call_api = st.Page("pages/db/bi/src/pages/call_api.py", title="Call API", icon=":material/database:")
db_upload = st.Page("pages/db/bi/src/pages/upload_data.py", title="Upload Data", icon=":material/database:")
db_delete_query = st.Page("pages/db/bi/src/pages/delete_query.py", title="Delete Query", icon=":material/database:")
db_delete_table = st.Page("pages/db/bi/src/pages/delete_table.py", title="Delete Table", icon=":material/database:")
db_plot = st.Page("pages/db/bi/src/pages/plot_results.py", title="Plot Results", icon=":material/database:")
db_save = st.Page("pages/db/bi/src/pages/save_query.py", title="Save Query", icon=":material/database:")


# ----------- Styling -------------------------
data_app = st.Page("pages/styling/superapp.py", title="Data Management", icon=":material/database:")
counter = st.Page("pages/styling/counter.py", title="DB", icon=":material/database:")

# ----------- Links CRUD ----------------------
link_manager = st.Page("pages/links_app.py", title="Link Manager", icon=":material/link:")

# ----------- Research -------------------------
st_context = st.Page("pages/research/Context.py", title="Context", icon=":material/chat_add_on:")
st_playsound = st.Page("pages/research/play_sound.py", title="Play Sound", icon=":material/volume_up:")
st_camera = st.Page("pages/research/camera.py", title="Camera", icon=":material/video_camera_front:")
st_sensors = st.Page("pages/research/sensors.py", title="Sensors", icon=":material/sensors:")



# ---------- NAVIGATION ----------
pg = st.navigation(
    {
        "Home": [home],
        "Organizers": [col_size],
        "Links": [link_manager],
        #"DB": [db_start, db_api, db_call_api, db_upload, db_delete_query, db_delete_table, db_plot, db_save],
        "Research": [st_context, st_playsound, st_camera, st_sensors],
    }, position="sidebar"
)

pg.run()

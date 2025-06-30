import streamlit as st
from supabase import create_client, Client
import pandas as pd

# Initialize Supabase client using secrets
supabase_url = st.secrets.get("supabase_url")
supabase_key = st.secrets.get("supabase_key")


st.page_link("pages/home/home_style.py", label="Home", icon=":material/home:")


st.page_link("https://pedrociancaglini.streamlit.app/", label="Portfolio", icon=":material/business_chip:")



if not supabase_url or not supabase_key:
    st.error("Supabase credentials not found in secrets!")
    st.stop()

supabase: Client = create_client(supabase_url, supabase_key)

table_name = "link_manager"

st.title("Link Manager")

phrasecode_filter = st.text_input("Phrasecode")

# Function definitions
@st.cache_data(show_spinner=False)
def fetch_links(code: str):
    response = supabase.table(table_name).select("*").eq("phrasecode", code).execute()
    return response.data

def create_link(code: str, title: str, notes: str, url: str):
    supabase.table(table_name).insert({
        "phrasecode": code,
        "title": title,
        "notes": notes,
        "url": url,
    }).execute()

def update_link(link_id: int, title: str, notes: str, url: str):
    supabase.table(table_name).update({
        "title": title,
        "notes": notes,
        "url": url,
    }).eq("id", link_id).execute()

def delete_link(link_id: int):
    supabase.table(table_name).delete().eq("id", link_id).execute()

# Display records when phrasecode is provided
if phrasecode_filter:
    links = fetch_links(phrasecode_filter) or []
    if links:
        df = pd.DataFrame(links)
        st.dataframe(df)

        ids = [link["id"] for link in links]
        selected_id = st.selectbox("Select record", ids, format_func=lambda x: f"ID {x}")
        selected = next((l for l in links if l["id"] == selected_id), None)
        if selected:
            st.subheader("Update / Delete")
            title_u = st.text_input("Title", value=selected.get("title", ""), key="upd_title")
            notes_u = st.text_area("Notes", value=selected.get("notes", ""), key="upd_notes")
            url_u = st.text_input("URL", value=selected.get("url", ""), key="upd_url")
            col1, col2 = st.columns(2)
            if col1.button("Update", key="update_btn"):
                update_link(selected_id, title_u, notes_u, url_u)
                st.success("Record updated")
                st.rerun()
            if col2.button("Delete", key="delete_btn"):
                delete_link(selected_id)
                st.success("Record deleted")
                st.rerun()
    else:
        st.info("No records found")

st.subheader("Create New Record")
with st.form("create_form"):
    new_code = st.text_input("Phrasecode", value=phrasecode_filter)
    new_title = st.text_input("Title")
    new_notes = st.text_area("Notes")
    new_url = st.text_input("URL")
    submitted = st.form_submit_button("Create")
    if submitted:
        create_link(new_code, new_title, new_notes, new_url)
        st.success("Record created")
        st.rerun()

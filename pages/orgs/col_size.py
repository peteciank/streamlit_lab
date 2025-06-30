import streamlit as st



st.set_page_config(layout="wide")  # For better column distribution


with open('static/css/style_back.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

col1, col2, col3 = st.columns((1, 2, 3))  # Create columns with different widths

with col1:
    st.write("First column (1/6 width)")
    st.text("This is smaller.")

with col2:
    st.write("Second column (2/6 width)")
    st.text("This is larger.")

with col3:
    st.write("Third column (3/6 width)")
    st.text("This is largest.")


st.page_link("pages/home/home_style.py", label="Home", icon=":material/home:")


st.page_link("https://pedrociancaglini.streamlit.app/", label="Portfolio", icon=":material/business_chip:")






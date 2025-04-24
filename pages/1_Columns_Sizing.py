import streamlit as st

st.set_page_config(layout="wide")  # For better column distribution

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
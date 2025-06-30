import streamlit as st
from libs.myside import MySidebar

# Define CSS with increased specificity for hero-title

with open('static/css/style_home.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Main banner content with button to toggle sidebar
st.markdown("""
<div class="main-banner">
    <h2 class="hero-title">This is my Streamlit Lab, This is my kingdom come!</h2>
    <p class="hero-subtitle">I will test all new features in this streamlit lab before moving them to other environments</p>
    <button id="browse-button" class="action-button">Browse Other Pages for More!</button>
</div>
<script>
    document.getElementById('browse-button').addEventListener('click', function() {
        console.log('Button clicked');
        const burgerMenu = window.parent.document.querySelector('[data-testid="stSidebarToggle"]');
        if (burgerMenu) {
            console.log('Burger menu found');
            burgerMenu.click();
        } else {
            console.log('Burger menu not found');
        }
    });
</script>
""", unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.title("Sidebar")
st.sidebar.write("This is the sidebar content.")
MySidebar()



with open('static/css/style_metrics.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
import streamlit as st

# Define CSS with increased specificity for hero-title

with open('static/css/style_home.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Main banner content with button to toggle sidebar
st.markdown("""
<div class="main-banner">
    <h2 class="hero-title">Reclaim your rhythm. Track every stroke. Measure your speed!</h2>
    <p class="hero-subtitle">Remand your training. Own your progress. Command your journey.</p>
    <button 
        onclick="
            console.log('Button clicked');
            const burgerMenu = document.querySelector('[data-testid=\"BurgerMenu\"]');
            if (burgerMenu) {
                console.log('Burger menu found');
                burgerMenu.click();
            } else {
                console.log('Burger menu not found');
            }
        "
        class="action-button">
        Start Training Now
    </button>
</div>
""", unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.title("Sidebar")
st.sidebar.write("This is the sidebar content.")


with open('static/css/style_metrics.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
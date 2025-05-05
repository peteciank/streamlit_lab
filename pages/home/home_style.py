import streamlit as st

# Define CSS with increased specificity for hero-title
st.markdown("""
<style>
* {
    font-family: 'Helvetica', 'Arial', sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
.main-banner .hero-title {
    color: white;
    font-size: 2.5rem;
    font-weight: bold;
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    margin-bottom: 1rem;
}
.hero-subtitle {
    color: rgba(255,255,255,0.95);
    font-size: 1.25rem;
    margin-bottom: 2rem;
}
.action-button {
    background-color: #f28c38;
    color: white;
    padding: 1rem 2rem;
    border: none;
    border-radius: 50px;
    font-size: 1.2rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
}
.action-button:hover {
    background-color: #e07b30;
}
.main-banner {
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    padding: 4rem 2rem;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

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
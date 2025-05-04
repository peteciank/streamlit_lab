import streamlit as st
import os
from pathlib import Path
import base64

# Function to get relative path to the logo
def get_logo_path():
    """Get the path to the logo file"""
    # Starting from the current file's directory
    current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    # Go up one level to the parent directory (from 'home' to the project root)
    parent_dir = current_dir.parent
    # Path to logo
    logo_path = parent_dir / 'static' / 'images' / 'logo.png'
    
    if logo_path.exists():
        return str(logo_path)
    else:
        return None

# Function to convert image to base64 for inline display
def get_image_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def show_home():
    # Streamlit config
    st.set_page_config(
        page_title="RemandIn - Take Training into Your Hands",
        page_icon="🚣",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    logo_path = get_logo_path()

    # CSS styles
    st.markdown("""
        <style>
            body {
                font-family: 'Helvetica', sans-serif;
                background-color: #f5f7fa;
            }

            .header-container {
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
                background-color: white;
                border-radius: 10px;
                margin-bottom: 30px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }

            .header-logo {
                max-height: 70px;
                margin-right: 20px;
            }

            .main-banner {
                background: linear-gradient(90deg, #1e3d59 0%, #0f2a3f 100%);
                padding: 50px 30px;
                border-radius: 20px;
                text-align: center;
                color: white;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            }

            .hero-title {
                font-size: 2.5rem;
                font-weight: 700;
                margin-bottom: 1rem;
            }

            .hero-subtitle {
                font-size: 1.3rem;
                margin-bottom: 2rem;
                opacity: 0.95;
            }

            .cta-button {
                background-color: #ff6e40;
                padding: 14px 32px;
                border: none;
                border-radius: 30px;
                color: white;
                font-size: 1.2rem;
                font-weight: 600;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                transition: all 0.3s ease;
                cursor: pointer;
            }

            .cta-button:hover {
                background-color: #ff8a65;
                transform: translateY(-2px);
                box-shadow: 0 6px 18px rgba(0,0,0,0.3);
            }
        </style>
    """, unsafe_allow_html=True)

    # Header with logo and title
    st.markdown('<div class="header-container">', unsafe_allow_html=True)

    if logo_path:
        logo_base64 = get_image_as_base64(logo_path)
        st.markdown(
            f'<img class="header-logo" src="data:image/png;base64,{logo_base64}"/>',
            unsafe_allow_html=True
        )

    st.markdown(
        '<h1 style="margin: 0; color: #1e3d59; font-weight: 700;">Take Training into Your Hands</h1>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # Main banner
    st.markdown("""
        <div class="main-banner">
            <h2 class="hero-title">Reclaim your rhythm. Track every stroke. Measure your speed.</h2>
            <p class="hero-subtitle"><span style="color: #ff6e40; font-weight: bold;">Remand</span> your training. Own your progress. Command your journey.</p>
            <button class="cta-button" onclick="window.location.href = '/SomeOtherPage'">Start Training Now</button>
        </div>
    """, unsafe_allow_html=True)
if __name__ == "__main__":
    show_home()
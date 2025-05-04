import streamlit as st
import os
from pathlib import Path
import base64

# Function to get relative path to the logo
def get_logo_path():
    """Get the path to the logo file"""
    current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    parent_dir = current_dir.parent
    logo_path = parent_dir / 'static' / 'images' / 'logo.png'
    if logo_path.exists():
        return str(logo_path)
    return None

# Function to convert image to base64 for inline display
def get_image_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def show_home():
    # Set Streamlit page configuration
    st.set_page_config(
        page_title="RemandIn - Take Training into Your Hands",
        page_icon="🚣",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Try to load logo path
    logo_path = get_logo_path()
    
    # Define CSS styles
    st.markdown("""
        <style>
            * {
                font-family: 'Helvetica', 'Arial', sans-serif;
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            .main-banner {
                background: linear-gradient(90deg, #1e3d59 0%, #0f2a3f 100%);
                border-radius: 15px;
                padding: 30px 20px;
                margin-bottom: 20px;
                width: 100%;
                text-align: center;
                position: relative;
                overflow: hidden;
            }
            .hero-title {
                font-size: 2.3rem;
                font-weight: 700;
                color: white;
                margin-bottom: 1rem;
                text-shadow: 0 2px 4px rgba(0,0,0,0.3);
            }
            .hero-subtitle {
                font-size: 1.4rem;
                color: rgba(255,255,255,0.95);
                margin-bottom: 2rem;
                text-shadow: 0 1px 3px rgba(0,0,0,0.2);
            }
            .action-button {
                background: #ff6e40;
                color: white;
                border: none;
                padding: 12px 30px;
                border-radius: 30px;
                font-size: 1.2rem;
                font-weight: 600;
                cursor: pointer;
                box-shadow: 0 4px 10px rgba(0,0,0,0.2);
                transition: all 0.3s ease;
            }
            .action-button:hover {
                background: #ff8a65;
                transform: translateY(-2px);
                box-shadow: 0 6px 15px rgba(0,0,0,0.3);
            }
            .highlight {
                color: #ff6e40;
                font-weight: 700;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Header with logo and title
    if logo_path:
        st.markdown(f"""
            <div style="display: flex; align-items: center; padding: 20px; background: white; margin-bottom: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                <div style="flex: 0 0 auto; margin-right: 20px;">
                    <img src="data:image/png;base64,{get_image_as_base64(logo_path)}" style="max-height: 70px; width: auto;">
                </div>
                <div style="flex: 1; text-align: center;">
                    <h1 style="font-size: 2rem; color: #1e3d59; margin: 0; font-weight: 700;">Take Training into Your Hands</h1>
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="display: flex; align-items: center; padding: 20px; background: white; margin-bottom: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                <div style="flex: 0 0 auto; margin-right: 20px; font-size: 2.5rem; color: #1e3d59; font-weight: 700;">R</div>
                <div style="flex: 1; text-align: center;">
                    <h1 style="font-size: 2rem; color: #1e3d59; margin: 0; font-weight: 700;">Take Training into Your Hands</h1>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Main banner with hero text and button
    st.markdown("""
        <div class="main-banner">
            <h2 class="hero-title">Reclaim your rhythm. Track every stroke. Measure your speed!</h2>
            <p class="hero-subtitle"><span class="highlight">Remand</span> your training. Own your progress. Command your journey.</p>
            <button 
                onclick="
                    const burgerMenu = document.querySelector('[data-testid=\"BurgerMenu\"]');
                    if (burgerMenu) {
                        burgerMenu.click();
                    }
                "
                class="action-button">
                Start Training Now
            </button>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_home()
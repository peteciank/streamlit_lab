import streamlit as st
import streamlit.components.v1 as components
import os
from pathlib import Path

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

# Custom CSS for styling
st.markdown("""
<style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container styling */
    .main-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
        padding: 0;
        margin: 0;
    }
    
    /* Hero section */
    .hero-section {
        text-align: center;
        padding: 2rem 1rem;
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        margin-bottom: 2rem;
    }
    
    /* Logo and title styling */
    .logo-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        margin-bottom: 1rem;
        flex-wrap: nowrap;
    }
    
    .logo {
        font-size: 4rem;
        animation: float 3s ease-in-out infinite;
        flex-shrink: 0;
    }
    
    .logo img {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        object-fit: cover;
        animation: float 3s ease-in-out infinite;
        flex-shrink: 0;
    }
    
    .app-title {
        font-size: 3.5rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin: 0;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .app-title {
        font-size: 3.5rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin: 0;
    }
    
    .alpha-badge {
        background: #ff6b6b;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: bold;
        display: inline-block;
        margin-top: 0.5rem;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    /* Video container */
    .video-container {
        max-width: 800px;
        width: 100%;
        margin: 2rem auto;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    /* Mobile video styling */
    @media (max-width: 768px) {
        .video-container {
            max-width: 95%;
            margin: 1rem auto;
            height: 400px;
        }
    }
    
    /* Video iframe styling */
    .video-container iframe {
        width: 100% !important;
        min-height: 350px !important;
    }
    
    @media (max-width: 768px) {
        .video-container iframe {
            height: 400px !important;
            min-height: 400px !important;
        }
    }
    
    /* Content sections */
    .content-section {
        background: white;
        margin: 2rem auto;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        max-width: 800px;
    }
    
    .section-title {
        color: #2a5298 !important;
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    /* Dark mode support for section titles */
    @media (prefers-color-scheme: dark) {
        .section-title {
            color: #74b9ff !important;
        }
    }
    
    .section-text {
        font-size: 1.1rem;
        line-height: 1.6;
        color: #333;
        text-align: center;
    }
    
    /* Call-to-action buttons */
    .cta-container {
        text-align: center;
        margin: 2rem 0;
    }
    
    .cta-button {
        display: inline-block;
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 1rem 2rem;
        text-decoration: none;
        border-radius: 30px;
        font-weight: bold;
        margin: 0.5rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .cta-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        text-decoration: none;
        color: white;
    }
    
    /* Animated hand pointer */
    .hand-pointer {
        position: fixed;
        top: 20px;
        left: 70px;
        font-size: 2.5rem;
        z-index: 9999 !important;
        animation: bounce 2s infinite;
        cursor: pointer;
        pointer-events: none;
        color: #ff6b6b;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0) rotate(-15deg); }
        40% { transform: translateY(-10px) rotate(-10deg); }
        60% { transform: translateY(-5px) rotate(-20deg); }
    }
    
    /* Floating contact menu */
    .floating-contact {
        position: fixed !important;
        bottom: 130px !important;
        right: 20px !important;
        z-index: 9999 !important;
    }
    
    .contact-button {
        background: #25d366 !important;
        color: white !important;
        border: none !important;
        border-radius: 50% !important;
        width: 60px !important;
        height: 60px !important;
        font-size: 1.5rem !important;
        cursor: pointer !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
        transition: all 0.3s ease !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    .contact-button:hover {
        transform: scale(1.1) !important;
        background: #20ba5a !important;
    }
    
    .contact-popup {
        position: absolute !important;
        bottom: 70px !important;
        right: 0 !important;
        background: white !important;
        border-radius: 15px !important;
        padding: 1rem !important;
        box-shadow: 0 5px 20px rgba(0,0,0,0.2) !important;
        width: 250px !important;
        display: none !important;
        z-index: 10000 !important;
    }
    
    .contact-popup.show {
        display: block !important;
        animation: slideUp 0.3s ease !important;
    }
    
    @keyframes slideUp {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    .contact-item {
        padding: 0.5rem 0 !important;
        border-bottom: 1px solid #eee !important;
        color: #333 !important;
    }
    
    .contact-item:last-child {
        border-bottom: none !important;
    }
    
    .contact-item a {
        color: #2a5298 !important;
        text-decoration: none !important;
    }
    
    .contact-item a:hover {
        text-decoration: underline !important;
    }
    
    /* Features grid */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .feature-card {
        background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .app-title {
            font-size: 2.5rem;
        }
        
        .logo {
            font-size: 3rem;
        }
        
        .logo img {
            width: 60px;
            height: 60px;
        }
        
        .logo-container {
            gap: 15px;
            flex-direction: row;
            flex-wrap: nowrap;
        }
        
        .content-section {
            margin: 1rem;
            padding: 1.5rem;
        }
        
        .features-grid {
            grid-template-columns: 1fr;
        }
        
        .hand-pointer {
            left: 65px;
            top: 15px;
            font-size: 2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Animated hand pointer
st.markdown("""
<div class="hand-pointer" onclick="document.querySelector('[data-testid=\"collapsedControl\"]').click()">
    👈
</div>
""", unsafe_allow_html=True)

# Hero Section with Logo
logo_path = get_logo_path()
if logo_path and os.path.exists(logo_path):
    # Read and encode the logo
    import base64
    with open(logo_path, "rb") as img_file:
        img_data = base64.b64encode(img_file.read()).decode()
    
    st.markdown(f"""
    <div class="hero-section">
        <div class="logo-container">
            <img src="data:image/png;base64,{img_data}" class="logo" alt="RowTok Logo">
            <h1 class="app-title">RowTok</h1>
        </div>
        <div class="alpha-badge">ALPHA VERSION</div>
        <p style="font-size: 1.3rem; margin-top: 1rem; opacity: 0.9;">
            The Future of Water Sports Training is Here
        </p>
    </div>
    """, unsafe_allow_html=True)
else:
    # Fallback to emoji if logo not found
    st.markdown("""
    <div class="hero-section">
        <div class="logo-container">
            <div class="logo">🚣‍♂️</div>
            <h1 class="app-title">RowTok</h1>
        </div>
        <div class="alpha-badge">ALPHA VERSION</div>
        <p style="font-size: 1.3rem; margin-top: 1rem; opacity: 0.9;">
            The Future of Water Sports Training is Here
        </p>
    </div>
    """, unsafe_allow_html=True)

# Video Section
st.markdown("""
<div class="video-container">
""", unsafe_allow_html=True)

# Embed YouTube video with better sizing
video_url = "https://youtu.be/GYgs9DkWTjo"
st.video(video_url)

st.markdown("</div>", unsafe_allow_html=True)

# Main content
st.markdown("""
<div class="content-section">
    <h2 class="section-title">🌊 Join the Revolution</h2>
    <p class="section-text">
        We're building the world's most advanced coach and training assistant for water sports, 
        and we need <strong>YOU</strong> to make it extraordinary! As an alpha tester, your feedback 
        will shape the future of rowing training technology.
    </p>
</div>
""", unsafe_allow_html=True)

# Features grid
st.markdown("""
<div class="content-section">
    <h2 class="section-title">✨ What Makes RowTok Special</h2>
    <div class="features-grid">
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <h3>AI-Powered Coaching</h3>
            <p>Get personalized training recommendations based on your performance data</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3>Advanced Analytics</h3>
            <p>Track your progress with detailed metrics and performance insights</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🤝</div>
            <h3>Community Driven</h3>
            <p>Connect with rowers worldwide and learn from the best</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🏆</div>
            <h3>Competition Ready</h3>
            <p>Prepare for races with targeted training programs</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Call to action section
st.markdown("""
<div class="content-section">
    <h2 class="section-title">🚀 Get Started Now</h2>
    <p class="section-text">
        Ready to revolutionize your water sports training? Click the arrow (👉) in the top-left corner 
        to access the RowTok app and start your journey to becoming a better rower!
    </p>
    <div class="cta-container">
        <a href="https://youtube.com/playlist?list=YOUR_PLAYLIST_ID" target="_blank" class="cta-button">
            📺 Watch More Tutorials
        </a>
        <a href="https://www.kickstarter.com" target="_blank" class="cta-button">
            💰 Support Our Mission
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# Support section with crowdfunding recommendation
st.markdown("""
<div class="content-section">
    <h2 class="section-title">💡 Help Us Grow</h2>
    <p class="section-text">
        Love what we're building? Support RowTok's development and help us create the ultimate 
        water sports training platform. We recommend <strong>Kickstarter</strong> for tech products 
        like ours, as it has the best reach for international audiences and sports enthusiasts.
    </p>
    <div style="text-align: center; margin-top: 1.5rem;">
        <p style="font-style: italic; color: #666;">
            "Every great journey starts with a single stroke. Join us in making waves in water sports training!"
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Floating contact menu
contact_script = """
<div class="floating-contact">
    <button class="contact-button" onclick="toggleContactPopup()" id="contactButton">💬</button>
    <div class="contact-popup" id="contactPopup">
        <div class="contact-item">
            <strong>📧 Email:</strong><br>
            <a href="mailto:contact@rowtok.app">contact@rowtok.app</a>
        </div>
        <div class="contact-item">
            <strong>💼 LinkedIn:</strong><br>
            <a href="https://linkedin.com/in/yourprofile" target="_blank">Connect with us</a>
        </div>
        <div class="contact-item">
            <strong>🐦 Twitter:</strong><br>
            <a href="https://twitter.com/rowtok" target="_blank">@RowTok</a>
        </div>
        <div class="contact-item">
            <strong>📱 WhatsApp:</strong><br>
            <a href="https://wa.me/1234567890" target="_blank">Chat with us</a>
        </div>
    </div>
</div>

<script>
function toggleContactPopup() {
    console.log('Contact button clicked');
    var popup = document.getElementById('contactPopup');
    if (popup) {
        popup.classList.toggle('show');
    }
}

// Ensure the script runs after DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Close popup when clicking outside
    document.addEventListener('click', function(event) {
        var popup = document.getElementById('contactPopup');
        var button = document.getElementById('contactButton');
        
        if (popup && button && !popup.contains(event.target) && !button.contains(event.target)) {
            popup.classList.remove('show');
        }
    });
});

// Alternative method if DOMContentLoaded doesn't work
setTimeout(function() {
    var button = document.getElementById('contactButton');
    if (button) {
        button.addEventListener('click', function() {
            console.log('Button clicked via event listener');
            var popup = document.getElementById('contactPopup');
            if (popup) {
                popup.classList.toggle('show');
            }
        });
    }
}, 1000);
</script>
"""

components.html(contact_script, height=0)

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; color: white; background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); margin-top: 2rem;">
    <p style="margin: 0; font-size: 1.1rem;">
        🚣‍♂️ <strong>RowTok</strong> - Revolutionizing Water Sports Training
    </p>
    <p style="margin: 0.5rem 0 0 0; opacity: 0.8;">
        Alpha Version • Built with ❤️ for the Rowing Community
    </p>
</div>
""", unsafe_allow_html=True)
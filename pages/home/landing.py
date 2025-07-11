import streamlit as st
import streamlit.components.v1 as components
import os
from pathlib import Path
import base64

# Page configuration: wide layout & ensure sidebar toggle is available
st.set_page_config(
    page_title="RowTok",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to locate the logo file
def get_logo_path():
    current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    logo_path = current_dir.parent / 'static' / 'images' / 'logo.png'
    return logo_path if logo_path.exists() else None

# Inject custom CSS (including making sidebar toggle visible)
st.markdown("""
<style>
    /* Hide Streamlit default menu/footer */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    /* Hide header contents but keep toggle */
    header > div:first-child { visibility: hidden; }
    /* Always show sidebar toggle button */
    [data-testid="stSidebarToggleButton"] {
        visibility: visible !important;
        pointer-events: all !important;
    }
    /* Your existing CSS below */
    .main-container { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 0; margin: 0; }
    .hero-section { text-align: center; padding: 2rem 1rem; background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); color: white; margin-bottom: 2rem; }
    .header-container { display: flex; align-items: center; justify-content: center; gap: 25px; margin-bottom: 1rem; min-height: 100px; }
    .rowtok-logo { width: 80px; height: 80px; border-radius: 50%; object-fit: cover; animation: logoFloat 3s ease-in-out infinite; flex-shrink: 0; }
    .rowtok-title { font-size: 4rem; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); margin: 0; display: inline-block; flex-shrink: 0; }
    @keyframes logoFloat { 0%,100% { transform: translateY(0px); } 50% { transform: translateY(-10px); } }
    .alpha-badge { background: #ff6b6b; color: white; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.9rem; font-weight: bold; display: inline-block; margin-top: 0.5rem; animation: pulse 2s infinite; }
    @keyframes pulse { 0%,100% { opacity:1; } 50% { opacity:0.7; } }
    .finger-pointer { position: fixed !important; top: 25px !important; left: 35px !important; z-index: 999998 !important; font-size: 2rem !important; color: #ff4444 !important; text-shadow: 2px 2px 4px rgba(0,0,0,0.8) !important; animation: fingerBounce 2s infinite !important; pointer-events: none !important; user-select: none !important; }
    @keyframes fingerBounce { 0%,20%,50%,80%,100% { transform: translateY(0px) rotate(-15deg); } 40% { transform: translateY(-8px) rotate(-10deg); } 60% { transform: translateY(-4px) rotate(-20deg); } }
    .contact-bubble { position: fixed !important; bottom: 140px !important; right: 25px !important; z-index: 999999 !important; font-family: Arial, sans-serif !important; }
    .contact-button { width: 65px !important; height: 65px !important; border-radius: 50% !important; background: #25D366 !important; border: none !important; font-size: 24px !important; cursor: pointer !important; box-shadow: 0 4px 12px rgba(0,0,0,0.3) !important; transition: all 0.3s ease !important; display: flex !important; align-items: center !important; justify-content: center !important; color: white !important; }
    .contact-button:hover { transform: scale(1.05) !important; box-shadow: 0 6px 20px rgba(0,0,0,0.4) !important; background: #20ba5a !important; }
    .contact-menu { position: absolute !important; bottom: 75px !important; right: 0 !important; width: 260px !important; background: white !important; border-radius: 15px !important; box-shadow: 0 8px 25px rgba(0,0,0,0.15) !important; display: none !important; padding: 0 !important; overflow: hidden !important; border: 1px solid #e0e0e0 !important; }
    .contact-menu.show { display: block !important; animation: contactSlideIn 0.3s ease-out !important; }
    @keyframes contactSlideIn { from { opacity:0; transform: translateY(20px) scale(0.8); } to { opacity:1; transform: translateY(0) scale(1); } }
    .content-section { background: white; margin: 2rem auto; padding: 2rem; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); max-width:800px; }
    .section-title { color:#2a5298 !important; font-size:2rem; font-weight:bold; text-align:center; margin-bottom:1rem; }
    .section-text { font-size:1.1rem; line-height:1.6; color:#333; text-align:center; }
    .cta-container { text-align:center; margin:2rem 0; }
    .cta-button { display:inline-block; background:linear-gradient(45deg,#667eea,#764ba2); color:white; padding:1rem 2rem; text-decoration:none; border-radius:30px; font-weight:bold; margin:0.5rem; transition:all 0.3s ease; box-shadow:0 4px 15px rgba(0,0,0,0.2); }
    .cta-button:hover { transform:translateY(-2px); box-shadow:0 6px 20px rgba(0,0,0,0.3); }
    .features-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:2rem; margin:2rem 0; }
    .feature-card { background:linear-gradient(135deg,#74b9ff 0%,#0984e3 100%); color:white; padding:1.5rem; border-radius:15px; text-align:center; box-shadow:0 5px 15px rgba(0,0,0,0.1); transition:transform 0.3s ease; }
    .feature-card:hover { transform:translateY(-5px); }
    .feature-icon { font-size:3rem; margin-bottom:1rem; }
</style>
""", unsafe_allow_html=True)

# Prepare image HTML separately to avoid nested f-strings
logo_path = get_logo_path()
img_data = None
if logo_path:
    with open(str(logo_path), "rb") as f:
        img_data = base64.b64encode(f.read()).decode()

if img_data:
    img_html = f'<img src="data:image/png;base64,{img_data}" class="rowtok-logo" alt="RowTok Logo">'
else:
    img_html = '<div style="font-size:4rem;animation:logoFloat 3s ease-in-out infinite;">🚣‍♂️</div>'

# Build hero HTML and JS
hero_html = f"""
<div class="finger-pointer">👈</div>
<div class="contact-bubble">
  <button class="contact-button" id="rowtokContactBtn">💬</button>
  <div class="contact-menu" id="rowtokContactMenu">
    <div class="contact-header">📞 Contact RowTok</div>
    <div class="contact-item"><strong>📧 Email:</strong><br><a href="mailto:contact@rowtok.app">contact@rowtok.app</a></div>
    <div class="contact-item"><strong>💼 LinkedIn:</strong><br><a href="https://linkedin.com/in/yourprofile" target="_blank">Connect with us</a></div>
    <div class="contact-item"><strong>🐦 Twitter:</strong><br><a href="https://twitter.com/rowtok" target="_blank">@RowTok</a></div>
    <div class="contact-item"><strong>📱 WhatsApp:</strong><br><a href="https://wa.me/1234567890" target="_blank">Chat with us</a></div>
  </div>
</div>
<div class="hero-section">
  <div class="header-container">
    {img_html}
    <h1 class="rowtok-title">RowTok</h1>
  </div>
  <div class="alpha-badge">ALPHA VERSION</div>
  <p style="font-size:1.3rem; margin-top:1rem; opacity:0.9;">The Future of Water Sports Training is Here</p>
</div>
<script>
;(function() {{
    let open = false;
    function init() {{
        const btn = document.getElementById("rowtokContactBtn");
        const menu = document.getElementById("rowtokContactMenu");
        if (!btn || !menu) return setTimeout(init, 500);
        btn.onclick = (e) => {{ e.stopPropagation(); open = !open; menu.classList.toggle("show", open); btn.style.transform = open ? "scale(1.1)" : "scale(1)"; }};
        document.addEventListener("click", (e) => {{
            if (open && !document.querySelector(".contact-bubble").contains(e.target)) {{
                menu.classList.remove("show");
                btn.style.transform = "scale(1)";
                open = false;
            }}
        }});
    }}
    init();
}})();
</script>
"""
components.html(hero_html, height=700, scrolling=True)

# Video Embed
st.video("https://youtu.be/GYgs9DkWTjo")

# Main content sections
st.markdown("""
<div class="content-section">
  <h2 class="section-title">🌊 Join the Revolution</h2>
  <p class="section-text">
    We're building the world's most advanced coach and training assistant for water sports, and we need <strong>YOU</strong> to make it extraordinary! As an alpha tester, your feedback will shape the future of rowing training technology.
  </p>
</div>
<div class="content-section">
  <h2 class="section-title">✨ What Makes RowTok Special</h2>
  <div class="features-grid">
    <div class="feature-card"><div class="feature-icon">🎯</div><h3>AI-Powered Coaching</h3><p>Get personalized training recommendations based on your performance data</p></div>
    <div class="feature-card"><div class="feature-icon">📊</div><h3>Advanced Analytics</h3><p>Track your progress with detailed metrics and performance insights</p></div>
    <div class="feature-card"><div class="feature-icon">🤝</div><h3>Community Driven</h3><p>Connect with rowers worldwide and learn from the best</p></div>
    <div class="feature-card"><div class="feature-icon">🏆</div><h3>Competition Ready</h3><p>Prepare for races with targeted training programs</p></div>
  </div>
</div>
<div class="content-section">
  <h2 class="section-title">🚀 Get Started Now</h2>
  <p class="section-text">
    Ready to revolutionize your water sports training? Click the arrow (👉) in the top-left corner to access the RowTok app and start your journey to becoming a better rower!
  </p>
  <div class="cta-container">
    <a href="https://youtube.com/playlist?list=YOUR_PLAYLIST_ID" target="_blank" class="cta-button">📺 Watch More Tutorials</a>
    <a href="https://www.kickstarter.com" target="_blank" class="cta-button">💰 Support Our Mission</a>
  </div>
</div>
<div class="content-section">
  <h2 class="section-title">💡 Help Us Grow</h2>
  <p class="section-text">
    Love what we're building? Support RowTok's development and help us create the ultimate water sports training platform. We recommend <strong>Kickstarter</strong> for tech products like ours, as it has the best reach for international audiences and sports enthusiasts.
  </p>
  <div style="text-align:center; margin-top:1.5rem;"><p style="font-style:italic; color:#666;">"Every great journey starts with a single stroke. Join us in making waves in water sports training!"</p></div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align:center; padding:2rem; color:white; background:linear-gradient(135deg,#1e3c72 0%,#2a5298 100%); margin-top:2rem;">
  <p style="margin:0; font-size:1.1rem;">🚣‍♂️ <strong>RowTok</strong> - Revolutionizing Water Sports Training</p>
  <p style="margin:0.5rem 0 0 0; opacity:0.8;">Alpha Version • Built with ❤️ for the Rowing Community.</p>
</div>
""", unsafe_allow_html=True)

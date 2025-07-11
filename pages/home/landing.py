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
    
    /* COMPLETELY NEW Logo and title styling */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 25px;
        margin-bottom: 1rem;
        min-height: 100px;
    }
    
    .rowtok-logo {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        object-fit: cover;
        animation: logoFloat 3s ease-in-out infinite;
        flex-shrink: 0;
    }
    
    .rowtok-title {
        font-size: 4rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin: 0;
        display: inline-block;
        flex-shrink: 0;
    }
    
    @keyframes logoFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
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
    
    /* FINGER POINTER - Position to point AT arrow, not cover it */
    .finger-pointer {
        position: fixed !important;
        top: 25px !important;
        left: 35px !important;
        z-index: 999998 !important;
        font-size: 2rem !important;
        color: #ff4444 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8) !important;
        animation: fingerBounce 2s infinite !important;
        pointer-events: none !important;
        user-select: none !important;
    }
    
    @keyframes fingerBounce {
        0%, 20%, 50%, 80%, 100% { 
            transform: translateY(0px) rotate(-15deg); 
        }
        40% { 
            transform: translateY(-8px) rotate(-10deg); 
        }
        60% { 
            transform: translateY(-4px) rotate(-20deg); 
        }
    }
    
    /* CONTACT BUBBLE - Direct CSS approach */
    .contact-bubble {
        position: fixed !important;
        bottom: 140px !important;
        right: 25px !important;
        z-index: 999999 !important;
        font-family: Arial, sans-serif !important;
    }
    
    .contact-button {
        width: 65px !important;
        height: 65px !important;
        border-radius: 50% !important;
        background: #25D366 !important;
        border: none !important;
        font-size: 24px !important;
        cursor: pointer !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3) !important;
        transition: all 0.3s ease !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        color: white !important;
    }
    
    .contact-button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.4) !important;
        background: #20ba5a !important;
    }
    
    .contact-menu {
        position: absolute !important;
        bottom: 75px !important;
        right: 0 !important;
        width: 260px !important;
        background: white !important;
        border-radius: 15px !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15) !important;
        display: none !important;
        padding: 0 !important;
        overflow: hidden !important;
        border: 1px solid #e0e0e0 !important;
    }
    
    .contact-menu.show {
        display: block !important;
        animation: contactSlideIn 0.3s ease-out !important;
    }
    
    @keyframes contactSlideIn {
        from { opacity: 0; transform: translateY(20px) scale(0.8); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }
    
    .contact-header {
        padding: 15px !important;
        border-bottom: 1px solid #f0f0f0 !important;
        font-weight: bold !important;
        color: #333 !important;
        background: #f8f9fa !important;
    }
    
    .contact-item {
        padding: 12px 15px !important;
        border-bottom: 1px solid #f0f0f0 !important;
    }
    
    .contact-item:last-child {
        border-bottom: none !important;
    }
    
    .contact-item strong {
        color: #2a5298 !important;
    }
    
    .contact-item a {
        color: #0066cc !important;
        text-decoration: none !important;
    }
    
    .contact-item a:hover {
        text-decoration: underline !important;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .rowtok-title {
            font-size: 2.8rem;
        }
        
        .rowtok-logo {
            width: 60px;
            height: 60px;
        }
        
        .header-container {
            gap: 20px;
        }
        
        .content-section {
            margin: 1rem;
            padding: 1.5rem;
        }
        
        .features-grid {
            grid-template-columns: 1fr;
        }
        
        .finger-pointer {
            left: 30px !important;
            font-size: 1.8rem !important;
            top: 20px !important;
        }
        
        .contact-bubble {
            bottom: 120px !important;
            right: 15px !important;
        }
        
        .contact-menu {
            width: 240px !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# COMPLETELY NEW Hero Section with embedded finger pointer and contact bubble
logo_path = get_logo_path()
if logo_path and os.path.exists(logo_path):
    # Read and encode the logo
    import base64
    with open(logo_path, "rb") as img_file:
        img_data = base64.b64encode(img_file.read()).decode()
    
    hero_html = f"""
    <!-- Finger Pointer -->
    <div class="finger-pointer">👈</div>
    
    <!-- Contact Bubble -->
    <div class="contact-bubble">
        <button class="contact-button" id="rowtokContactBtn">💬</button>
        <div class="contact-menu" id="rowtokContactMenu">
            <div class="contact-header">📞 Contact RowTok</div>
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
    
    <!-- Hero Section -->
    <div class="hero-section">
        <div class="header-container">
            <img src="data:image/png;base64,{img_data}" class="rowtok-logo" alt="RowTok Logo">
            <h1 class="rowtok-title">RowTok</h1>
        </div>
        <div class="alpha-badge">ALPHA VERSION</div>
        <p style="font-size: 1.3rem; margin-top: 1rem; opacity: 0.9;">
            The Future of Water Sports Training is Here
        </p>
    </div>
    
    <script>
    (function() {{
        let isContactOpen = false;
        
        function initContactBubble() {{
            const btn = document.getElementById('rowtokContactBtn');
            const menu = document.getElementById('rowtokContactMenu');
            
            if (!btn || !menu) {{
                console.log('Contact elements not found, retrying in 500ms...');
                setTimeout(initContactBubble, 500);
                return;
            }}
            
            console.log('Contact bubble found and initializing...');
            
            btn.onclick = function(e) {{
                e.preventDefault();
                e.stopPropagation();
                console.log('Contact button clicked!');
                
                isContactOpen = !isContactOpen;
                
                if (isContactOpen) {{
                    menu.classList.add('show');
                    btn.style.background = '#20ba5a';
                    btn.style.transform = 'scale(1.1)';
                }} else {{
                    menu.classList.remove('show');
                    btn.style.background = '#25D366';
                    btn.style.transform = 'scale(1)';
                }}
            }};
            
            // Close when clicking outside
            document.addEventListener('click', function(e) {{
                const bubble = document.querySelector('.contact-bubble');
                if (bubble && !bubble.contains(e.target) && isContactOpen) {{
                    menu.classList.remove('show');
                    btn.style.background = '#25D366';
                    btn.style.transform = 'scale(1)';
                    isContactOpen = false;
                }}
            }});
            
            console.log('Contact bubble setup complete!');
        }}
        
        // Try immediately and also after delays
        initContactBubble();
        setTimeout(initContactBubble, 100);
        setTimeout(initContactBubble, 1000);
    }})();
    </script>
    """
else:
    # Fallback to emoji if logo not found
    hero_html = """
    <!-- Finger Pointer -->
    <div class="finger-pointer">👈</div>
    
    <!-- Contact Bubble -->
    <div class="contact-bubble">
        <button class="contact-button" id="rowtokContactBtn">💬</button>
        <div class="contact-menu" id="rowtokContactMenu">
            <div class="contact-header">📞 Contact RowTok</div>
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
    
    <!-- Hero Section -->
    <div class="hero-section">
        <div class="header-container">
            <div style="font-size: 4rem; animation: logoFloat 3s ease-in-out infinite;">🚣‍♂️</div>
            <h1 class="rowtok-title">RowTok</h1>
        </div>
        <div class="alpha-badge">ALPHA VERSION</div>
        <p style="font-size: 1.3rem; margin-top: 1rem; opacity: 0.9;">
            The Future of Water Sports Training is Here
        </p>
    </div>
    
    <script>
    (function() {
        let isContactOpen = false;
        
        function initContactBubble() {
            const btn = document.getElementById('rowtokContactBtn');
            const menu = document.getElementById('rowtokContactMenu');
            
            if (!btn || !menu) {
                console.log('Contact elements not found, retrying in 500ms...');
                setTimeout(initContactBubble, 500);
                return;
            }
            
            console.log('Contact bubble found and initializing...');
            
            btn.onclick = function(e) {
                e.preventDefault();
                e.stopPropagation();
                console.log('Contact button clicked!');
                
                isContactOpen = !isContactOpen;
                
                if (isContactOpen) {
                    menu.classList.add('show');
                    btn.style.background = '#20ba5a';
                    btn.style.transform = 'scale(1.1)';
                } else {
                    menu.classList.remove('show');
                    btn.style.background = '#25D366';
                    btn.style.transform = 'scale(1)';
                }
            };
            
            // Close when clicking outside
            document.addEventListener('click', function(e) {
                const bubble = document.querySelector('.contact-bubble');
                if (bubble && !bubble.contains(e.target) && isContactOpen) {
                    menu.classList.remove('show');
                    btn.style.background = '#25D366';
                    btn.style.transform = 'scale(1)';
                    isContactOpen = false;
                }
            });
            
            console.log('Contact bubble setup complete!');
        }
        
        // Try immediately and also after delays
        initContactBubble();
        setTimeout(initContactBubble, 100);
        setTimeout(initContactBubble, 1000);
    })();
    </script>
    """

st.markdown(hero_html, unsafe_allow_html=True)

# Fix contact popup with a more reliable approach
contact_fix_js = """
<script>
// Simple, direct approach to fix contact popup
function fixContactBubble() {
    console.log('Attempting to fix contact bubble...');
    
    const btn = document.getElementById('rowtokContactBtn');
    const menu = document.getElementById('rowtokContactMenu');
    
    if (!btn || !menu) {
        console.log('Elements not found, will retry...');
        setTimeout(fixContactBubble, 200);
        return;
    }
    
    console.log('Contact elements found!');
    
    let isOpen = false;
    
    // Direct onclick assignment
    btn.onclick = function(event) {
        event.preventDefault();
        event.stopPropagation();
        
        console.log('Contact button clicked! Current state:', isOpen);
        
        isOpen = !isOpen;
        
        if (isOpen) {
            console.log('Opening menu...');
            menu.style.display = 'block';
            menu.classList.add('show');
            btn.style.background = '#20ba5a';
            btn.style.transform = 'scale(1.1)';
        } else {
            console.log('Closing menu...');
            menu.style.display = 'none';
            menu.classList.remove('show');
            btn.style.background = '#25D366';
            btn.style.transform = 'scale(1)';
        }
    };
    
    // Click outside to close
    document.onclick = function(event) {
        const bubble = document.querySelector('.contact-bubble');
        if (isOpen && bubble && !bubble.contains(event.target)) {
            console.log('Clicking outside, closing menu...');
            isOpen = false;
            menu.style.display = 'none';
            menu.classList.remove('show');
            btn.style.background = '#25D366';
            btn.style.transform = 'scale(1)';
        }
    };
    
    console.log('Contact bubble setup completed successfully!');
}

// Try multiple times to ensure it works
fixContactBubble();
setTimeout(fixContactBubble, 100);
setTimeout(fixContactBubble, 500);
setTimeout(fixContactBubble, 1000);
setTimeout(fixContactBubble, 2000);
</script>
"""

components.html(contact_fix_js, height=0)

# Video Section
st.markdown("""
<div class="video-container">
""", unsafe_allow_html=True)

# Embed YouTube video
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
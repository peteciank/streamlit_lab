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
    # Set Streamlit page configuration
    st.set_page_config(
        page_title="RemandIn - Take Training into Your Hands",
        page_icon="🚣",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Add custom CSS with improved styling
    st.markdown("""
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            /* Global Styles */
            * {
                font-family: 'Montserrat', sans-serif;
                box-sizing: border-box;
            }
            
            h1, h2, h3, h4 {
                font-weight: 600;
                color: #1e3d59;
            }
            
            /* Custom accent colors */
            :root {
                --primary: #1e3d59;     /* Deep blue */
                --secondary: #ff6e40;   /* Coral orange */
                --light: #f5f5f5;       /* Light gray */
                --accent: #ffc13b;      /* Gold */
                --success: #5ab9ea;     /* Light blue */
            }
            
            /* Material Icons */
            .material-icons {
                font-family: 'Material Icons';
                font-weight: normal;
                font-style: normal;
                font-size: 24px;
                line-height: 1;
                letter-spacing: normal;
                text-transform: none;
                display: inline-block;
                white-space: nowrap;
                word-wrap: normal;
                direction: ltr;
                -webkit-font-smoothing: antialiased;
            }
            
            /* Hero Section */
            .hero-container {
                background: linear-gradient(135deg, var(--primary) 0%, #0f2a3f 100%);
                color: white;
                padding: 60px 20px;
                border-radius: 15px;
                margin-bottom: 30px;
                position: relative;
                overflow: hidden;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
            }
            
            .hero-container::after {
                content: "";
                position: absolute;
                top: 0;
                right: 0;
                width: 40%;
                height: 100%;
                background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="none"><path d="M0,0 L100,0 L100,100 Z" fill="%23ff6e40" opacity="0.2"/></svg>');
                background-size: cover;
                z-index: 1;
            }
            
            .header-container {
                display: flex;
                align-items: center;
                padding: 10px 0;
                margin-bottom: 20px;
            }
            
            .logo-container {
                flex: 0 0 auto;
                margin-right: 20px;
            }
            
            .title-container {
                flex: 1 1 auto;
                text-align: left;
            }
            
            .logo-image {
                max-height: 70px;
                width: auto;
                filter: drop-shadow(0px 4px 6px rgba(0, 0, 0, 0.3));
            }
            
            /* Feature Cards */
            .feature-container {
                text-align: center;
                padding: 30px 20px;
                border-radius: 10px;
                background-color: white;
                margin: 10px 0;
                transition: transform 0.3s, box-shadow 0.3s;
                height: 100%;
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
                border-bottom: 4px solid var(--secondary);
            }
            
            .feature-container:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.12);
            }
            
            .feature-icon {
                font-size: 56px !important;
                color: var(--secondary);
                margin-bottom: 15px;
                background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            
            /* Stats Section */
            .stat-box {
                background-color: white;
                border-radius: 10px;
                padding: 20px 15px;
                text-align: center;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
                height: 100%;
                border-left: 4px solid var(--accent);
            }
            
            .stat-number {
                font-size: 2.5rem;
                font-weight: 700;
                color: var(--primary);
                margin-bottom: 5px;
            }
            
            .stat-label {
                color: #666;
                font-size: 1rem;
            }
            
            /* Quick Access Cards */
            .quick-access-card {
                background-color: white;
                border-radius: 12px;
                padding: 20px;
                text-align: center;
                transition: all 0.3s ease;
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.08);
                height: 100%;
                cursor: pointer;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                border-top: 4px solid var(--success);
            }
            
            .quick-access-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 12px 24px rgba(0, 0, 0, 0.12);
            }
            
            .quick-access-icon {
                font-size: 36px !important;
                color: var(--success);
                margin-bottom: 15px;
            }
            
            /* Testimonial Section */
            .testimonial-container {
                background-color: var(--light);
                border-radius: 12px;
                padding: 30px;
                position: relative;
                margin-top: 50px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
            }
            
            .testimonial-text {
                font-style: italic;
                color: #444;
                line-height: 1.6;
                margin-bottom: 20px;
            }
            
            .testimonial-author {
                font-weight: 600;
                color: var(--primary);
            }
            
            .testimonial-container::before {
                content: ''';
                font-size: 120px;
                position: absolute;
                top: -40px;
                left: 20px;
                color: var(--secondary);
                opacity: 0.15;
                font-family: serif;
            }
            
            /* Form Styling */
            .form-container {
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            }
            
            /* Button Styling */
            .custom-button {
                background: linear-gradient(135deg, var(--secondary) 0%, #ff8a65 100%);
                border: none;
                color: white;
                padding: 10px 20px;
                border-radius: 30px;
                font-weight: 600;
                letter-spacing: 0.5px;
                box-shadow: 0 4px 10px rgba(255, 110, 64, 0.3);
                transition: all 0.3s ease;
            }
            
            .custom-button:hover {
                box-shadow: 0 6px 15px rgba(255, 110, 64, 0.4);
                transform: translateY(-2px);
            }
            
            /* Responsive Styles */
            @media screen and (max-width: 768px) {
                .hero-container::after {
                    display: none;
                }
                .header-container {
                    flex-direction: column;
                    text-align: center;
                }
                .title-container {
                    text-align: center;
                }
                .logo-container {
                    margin-right: 0;
                    margin-bottom: 20px;
                }
            }
            
            /* Footer Styling */
            .footer {
                text-align: center;
                padding: 30px 0;
                color: #7f8c8d;
                font-size: 0.9rem;
                background-color: var(--light);
                border-radius: 10px;
                margin-top: 40px;
            }
            
            /* Custom wave separator */
            .wave-separator {
                height: 70px;
                background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none"><path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" fill="%23f5f5f5"></path></svg>');
                background-size: cover;
                background-repeat: no-repeat;
                margin-top: -60px;
                margin-bottom: -20px;
                position: relative;
                z-index: 2;
            }
            
            /* Progress bar styling */
            .progress-container {
                width: 100%;
                height: 8px;
                background-color: #e0e0e0;
                border-radius: 4px;
                margin-top: 10px;
            }
            
            .progress-bar {
                height: 8px;
                border-radius: 4px;
                background: linear-gradient(90deg, var(--secondary) 0%, var(--accent) 100%);
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Try to load logo path
    logo_path = get_logo_path()
    
    # Create a single integrated banner with logo and text
    st.markdown("""
        <div style="background: linear-gradient(90deg, #1e3d59 0%, #0f2a3f 100%); 
                    padding: 20px 30px;
                    width: 100%; 
                    margin-bottom: 40px;
                    position: relative;
                    overflow: hidden;
                    border-radius: 15px;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                    display: flex;
                    align-items: center;">
            
            <!-- Logo container (left aligned) -->
            <div style="flex: 0 0 auto; margin-right: 20px; background: white; padding: 15px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);">
    """, unsafe_allow_html=True)
    
    # Add logo if available
    if logo_path:
        st.markdown(f"""
                <img src="data:image/png;base64,{get_image_as_base64(logo_path)}" style="max-height: 80px; width: auto;">
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
                <div style="font-size: 2rem; font-weight: 700; color: #1e3d59;">R</div>
            </div>
        """, unsafe_allow_html=True)
    
    # Add title text (centered within the remaining space)
    st.markdown("""
            <!-- Title container (centered in remaining space) -->
            <div style="flex: 1; text-align: center;">
                <h1 style="font-size: 3rem; font-weight: 700; margin: 0; color: white; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">RemandIn</h1>
                <p style="font-size: 1.3rem; font-style: italic; margin: 0; color: rgba(255,255,255,0.9); text-shadow: 0 1px 2px rgba(0,0,0,0.2);">Take Training into Your Hands</p>
            </div>
            
            <!-- Background decoration -->
            <div style="position: absolute; bottom: 0; right: 0; width: 40%; height: 100%; background: linear-gradient(135deg, transparent 50%, rgba(255, 110, 64, 0.2) 100%);"></div>
        </div>
    """, unsafe_allow_html=True)
    
    # Add a second banner for the hero section
    st.markdown("""
        <div style="background: linear-gradient(90deg, #1e3d59 0%, #0f2a3f 100%); 
                    padding: 40px 30px;
                    width: 100%; 
                    margin-bottom: 40px;
                    position: relative;
                    overflow: hidden;
                    border-radius: 15px;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);">
    """, unsafe_allow_html=True)
    
    # Main headline and call to action with sidebar toggle functionality
    st.markdown("""
            <!-- Main hero content -->
            <div style='text-align: center; margin: 2rem 0; position: relative; z-index: 2;'>
                <h2 style='font-size: 2.3rem; color: white; margin-bottom: 1.5rem; text-shadow: 0 2px 10px rgba(0,0,0,0.3); font-weight: 700; letter-spacing: 0.5px;'>
                    Reclaim your rhythm. Track every stroke. Measure your speed.
                </h2>
                <p style='font-size: 1.4rem; color: rgba(255,255,255,0.95); max-width: 800px; margin: 0 auto 30px; text-shadow: 0 1px 3px rgba(0,0,0,0.2);'>
                    <strong>Remand</strong> your training. Own your progress. Command your journey.
                </p>
                <button 
                    onclick="
                        // Get the sidebar element 
                        const sidebar = window.parent.document.querySelector('.st-emotion-cache-1cypcdb, .st-emotion-cache-z5fcl4, .css-1cypcdb, .css-z5fcl4');
                        // Toggle sidebar by clicking the burger menu if sidebar is not expanded
                        if(sidebar && !sidebar.classList.contains('--expanded')) {
                            const burgerMenu = window.parent.document.querySelector('[data-testid=\\"BurgerMenu\\"]');
                            if(burgerMenu) burgerMenu.click();
                        }
                    "
                    class="custom-button" 
                    style="font-size: 1.2rem; padding: 12px 30px; cursor: pointer; background: linear-gradient(135deg, #ff6e40 0%, #ff8a65 100%); border: none; color: white; border-radius: 30px; font-weight: 600; letter-spacing: 0.5px; box-shadow: 0 4px 10px rgba(255, 110, 64, 0.3);">
                    Start Training Now
                </button>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Wave separator
    st.markdown("""
        <div class="wave-separator"></div>
    """, unsafe_allow_html=True)
    
    # Stats Section
    st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>The Power of RemandIn</h2>", unsafe_allow_html=True)
    
    stats_cols = st.columns(4)
    
    stats_data = [
        {"number": "7,500+", "label": "Active Rowers"},
        {"number": "250+", "label": "Teams Using RemandIn"},
        {"number": "85%", "label": "Training Improvement"},
        {"number": "98%", "label": "User Satisfaction"}
    ]
    
    for i, col in enumerate(stats_cols):
        with col:
            st.markdown(f"""
                <div class="stat-box">
                    <div class="stat-number">{stats_data[i]['number']}</div>
                    <div class="stat-label">{stats_data[i]['label']}</div>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Features in columns with Material Icons - Enhanced
    st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Why Choose RemandIn?</h2>", unsafe_allow_html=True)
    
    feature_cols = st.columns(3)
    
    with feature_cols[0]:
        st.markdown("""
            <div class='feature-container'>
                <i class='material-icons feature-icon'>speed</i>
                <h3>Precise Tracking</h3>
                <p>Monitor your performance with GPS accuracy. Track speed, distance, and strokes in real-time with precision that gives you the competitive edge.</p>
                <div class="progress-container">
                    <div class="progress-bar" style="width: 92%;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with feature_cols[1]:
        st.markdown("""
            <div class='feature-container'>
                <i class='material-icons feature-icon'>analytics</i>
                <h3>Smart Analytics</h3>
                <p>Get detailed insights into your training sessions. Analyze trends, identify patterns, and make data-driven decisions to improve your technique.</p>
                <div class="progress-container">
                    <div class="progress-bar" style="width: 88%;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with feature_cols[2]:
        st.markdown("""
            <div class='feature-container'>
                <i class='material-icons feature-icon'>emoji_events</i>
                <h3>Progress Tracking</h3>
                <p>Set ambitious goals, track meaningful improvements, and celebrate your achievements along the way. Let your data tell the story of your success.</p>
                <div class="progress-container">
                    <div class="progress-bar" style="width: 95%;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Team Management Section - New Feature
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Team Management Made Simple</h2>", unsafe_allow_html=True)
    
    team_cols = st.columns([1, 3])
    
    with team_cols[0]:
        st.markdown("""
            <div style="padding: 20px; height: 100%;">
                <i class="material-icons" style="font-size: 150px; color: #1e3d59;">groups</i>
            </div>
        """, unsafe_allow_html=True)
    
    with team_cols[1]:
        st.markdown("""
            <div style="padding: 20px;">
                <h3>Coordinate Your Crew with Ease</h3>
                <p style="font-size: 1.1rem; margin-bottom: 20px;">
                    RemandIn brings your entire team together on one platform. Schedule practices, track individual 
                    and team metrics, and compare performance over time. Coaches can identify strengths and areas for 
                    improvement at both individual and team levels.
                </p>
                <ul style="list-style-type: none; padding-left: 0; margin-top: 20px;">
                    <li style="margin-bottom: 10px; display: flex; align-items: center;">
                        <i class="material-icons" style="color: #ff6e40; margin-right: 10px;">check_circle</i>
                        Schedule and manage team practices
                    </li>
                    <li style="margin-bottom: 10px; display: flex; align-items: center;">
                        <i class="material-icons" style="color: #ff6e40; margin-right: 10px;">check_circle</i>
                        Track individual and team performance
                    </li>
                    <li style="margin-bottom: 10px; display: flex; align-items: center;">
                        <i class="material-icons" style="color: #ff6e40; margin-right: 10px;">check_circle</i>
                        Generate detailed reports for coaches
                    </li>
                    <li style="margin-bottom: 10px; display: flex; align-items: center;">
                        <i class="material-icons" style="color: #ff6e40; margin-right: 10px;">check_circle</i>
                        Compare historical data to measure growth
                    </li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick Access Section - Enhanced with cards
    st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Quick Access</h2>", unsafe_allow_html=True)
    
    quick_access_cols = st.columns(4)
    
    quick_access_items = [
        {"icon": "timer", "title": "Timer", "description": "Start tracking your rowing sessions"},
        {"icon": "speed", "title": "Speed", "description": "Monitor your pace in real-time"},
        {"icon": "straighten", "title": "Distance", "description": "Track how far you've traveled"},
        {"icon": "leaderboard", "title": "Team Stats", "description": "View team performance"}
    ]
    
    for i, col in enumerate(quick_access_cols):
        with col:
            st.markdown(f"""
                <div class="quick-access-card">
                    <i class="material-icons quick-access-icon">{quick_access_items[i]['icon']}</i>
                    <h3>{quick_access_items[i]['title']}</h3>
                    <p>{quick_access_items[i]['description']}</p>
                </div>
            """, unsafe_allow_html=True)
    
    # Testimonial Section - New
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>What Rowers Are Saying</h2>", unsafe_allow_html=True)
    
    testimonial_cols = st.columns(2)
    
    with testimonial_cols[0]:
        st.markdown("""
            <div class="testimonial-container">
                <p class="testimonial-text">
                    RemandIn has transformed how our team trains. The data insights have helped us identify and correct technical issues we weren't even aware of.
                </p>
                <p class="testimonial-author">- Sarah J., Head Coach, University Rowing Team</p>
            </div>
        """, unsafe_allow_html=True)
    
    with testimonial_cols[1]:
        st.markdown("""
            <div class="testimonial-container">
                <p class="testimonial-text">
                    As a competitive rower, having access to precise metrics has been a game-changer. My stroke efficiency improved by 23% in just three months!
                </p>
                <p class="testimonial-author">- Michael T., National Championship Medalist</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Contact Form - Enhanced
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Share Your Thoughts</h2>", unsafe_allow_html=True)
    
    form_cols = st.columns([1, 2, 1])
    
    with form_cols[1]:
        st.markdown("""
            <div class="form-container">
        """, unsafe_allow_html=True)
        
        with st.form("suggestion_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            suggestion = st.text_area("Your Suggestion")
            submitted = st.form_submit_button("Submit")
            
            if submitted:
                st.success("Thank you for your feedback! We value your input and will consider it for future updates.")
        
        st.markdown("""
            </div>
        """, unsafe_allow_html=True)
    
    # Footer - Enhanced
    st.markdown("""
        <div class="footer">
            <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                <div style="margin: 0 15px;"><i class="material-icons" style="font-size: 24px; color: #1e3d59;">facebook</i></div>
                <div style="margin: 0 15px;"><i class="material-icons" style="font-size: 24px; color: #1e3d59;">chat</i></div>
                <div style="margin: 0 15px;"><i class="material-icons" style="font-size: 24px; color: #1e3d59;">email</i></div>
            </div>
            <p>© 2024 RemandIn. All rights reserved.</p>
            <p>Made with ❤️ for rowers everywhere</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_home()
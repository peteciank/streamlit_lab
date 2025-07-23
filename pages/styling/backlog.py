import streamlit as st
import json
from datetime import datetime, date
import pandas as pd

# Custom CSS for styling
st.markdown("""
<style>
    .roadmap-container {
        padding: 20px 0;
    }
    
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
    }
    
    .status-completed {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
    }
    
    .status-in-progress {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .status-planned {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    
    .status-on-hold {
        background: linear-gradient(135deg, #4b6cb7 0%, #182848 100%);
    }
    
    .status-refining {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    .feature-description {
        font-size: 1rem;
        margin-bottom: 15px;
        opacity: 0.9;
    }
    
    .feature-meta {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.9rem;
        opacity: 0.8;
    }
    
    .status-badge {
        background: rgba(255,255,255,0.2);
        padding: 5px 12px;
        border-radius: 20px;
        font-weight: bold;
    }
    
    .quarter-header {
        text-align: center;
        padding: 20px 0;
        font-size: 2rem;
        font-weight: bold;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .timeline-line {
        border-left: 4px solid #667eea;
        margin-left: 20px;
        padding-left: 30px;
    }
    
    .app-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
    }
    
    .stat-card {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border-radius: 10px;
        color: white;
        min-width: 120px;
    }
</style>
""", unsafe_allow_html=True)

# Sample JSON roadmap data
roadmap_data = {
    "app_info": {
        "name": "RowTok - Water Sports Training Suite",
        "version": "2.0",
        "last_updated": "2025-01-15"
    },
    "quarters": {
        "Q1 2025": [
            {
                "feature": "Enhanced Timer App R9-R12 Phases",
                "description": "Expand rhythm phases beyond R8 to include ultra-high intensity R9-R12 phases for sprint training.",
                "status": "Completed",
                "release_date": "2025-01-15",
                "priority": "High",
                "team": "Core Development",
                "progress": 100
            },
            {
                "feature": "Improved GPS Accuracy Algorithm",
                "description": "Enhanced GPS filtering and smoothing for more accurate speed readings in challenging conditions.",
                "status": "Completed", 
                "release_date": "2025-02-01",
                "priority": "High",
                "team": "GPS Team",
                "progress": 100
            },
            {
                "feature": "Multi-Language Audio Cues",
                "description": "Support for audio prompts in Spanish, French, German, and Italian for international teams.",
                "status": "In Progress",
                "release_date": "2025-03-15",
                "priority": "Medium", 
                "team": "Localization Team",
                "progress": 75
            }
        ],
        "Q2 2025": [
            {
                "feature": "Advanced Boat Weight Balancer 2.0",
                "description": "Enhanced balancer with heel/trim optimization, adaptive positioning, and weight shift recommendations.",
                "status": "In Progress",
                "release_date": "2025-04-30",
                "priority": "High",
                "team": "Algorithm Team",
                "progress": 45
            },
            {
                "feature": "Team Sync Dashboard",
                "description": "Real-time data sharing between coach and multiple crew boats with live performance comparison.",
                "status": "Planned",
                "release_date": "2025-05-15",
                "priority": "High",
                "team": "Backend Team", 
                "progress": 0
            },
            {
                "feature": "Enhanced Sprints Analytics",
                "description": "Advanced 100m split analysis with power curve modeling and fatigue detection algorithms.",
                "status": "Planned",
                "release_date": "2025-06-30",
                "priority": "Medium",
                "team": "Data Analytics",
                "progress": 0
            }
        ],
        "Q3 2025": [
            {
                "feature": "Heart Rate Monitor Integration",
                "description": "Direct integration with Polar, Garmin, and Wahoo heart rate monitors for combined performance data.",
                "status": "Planned",
                "release_date": "2025-07-15",
                "priority": "High",
                "team": "Hardware Integration",
                "progress": 0
            },
            {
                "feature": "Weather-Aware Training Suggestions",
                "description": "Real-time weather integration to suggest optimal training modes based on wind/water conditions.",
                "status": "Planned", 
                "release_date": "2025-08-30",
                "priority": "Medium",
                "team": "Weather API Team",
                "progress": 0
            },
            {
                "feature": "SPM Trainer Mode 5 - Adaptive",
                "description": "AI-powered stroke rate adaptation based on GPS speed, heart rate, and training phase targets.",
                "status": "Planned",
                "release_date": "2025-09-15",
                "priority": "High",
                "team": "AI Development",
                "progress": 0
            }
        ],
        "Q4 2025": [
            {
                "feature": "360° Camera Integration for Technique Analysis",
                "description": "Integration with 360° cameras for comprehensive stroke technique recording and analysis.",
                "status": "Planned",
                "release_date": "2025-10-31",
                "priority": "High",
                "team": "Camera Integration", 
                "progress": 0
            },
            {
                "feature": "Regatta Race Day Manager",
                "description": "Complete race day management with warm-up protocols, lane assignments, and performance tracking.",
                "status": "On Hold",
                "release_date": "2025-11-30",
                "priority": "Medium",
                "team": "Event Management",
                "progress": 0
            },
            {
                "feature": "Offline Mode with Data Sync",
                "description": "Full offline functionality with automatic data synchronization when internet connection is restored.",
                "status": "Planned",
                "release_date": "2025-12-15",
                "priority": "High",
                "team": "Infrastructure Team",
                "progress": 0
            }
        ]
    }
}

def get_status_class(status):
    status_classes = {
        "Completed": "status-completed",
        "In Progress": "status-in-progress", 
        "Planned": "status-planned",
        "On Hold": "status-on-hold"
    }
    return status_classes.get(status, "status-planned")

def get_status_emoji(status):
    status_emojis = {
        "Completed": "✅",
        "In Progress": "🚧",
        "Planned": "📋", 
        "On Hold": "⏸️"
    }
    return status_emojis.get(status, "📋")

def calculate_stats(roadmap_data):
    total_features = 0
    completed = 0
    in_progress = 0
    planned = 0
    on_hold = 0
    
    for quarter, features in roadmap_data["quarters"].items():
        total_features += len(features)
        for feature in features:
            status = feature["status"]
            if status == "Completed":
                completed += 1
            elif status == "In Progress":
                in_progress += 1
            elif status == "Planned":
                planned += 1
            elif status == "On Hold":
                on_hold += 1
    
    return {
        "total": total_features,
        "completed": completed,
        "in_progress": in_progress, 
        "planned": planned,
        "on_hold": on_hold
    }

# Main app
def main():
    # Header
    st.markdown(f"""
    <div class="app-header">
        <h1>🚣‍♀️ {roadmap_data['app_info']['name']} 🚣‍♂️</h1>
        <h3>Product Roadmap - Version {roadmap_data['app_info']['version']}</h3>
        <p>Last Updated: {roadmap_data['app_info']['last_updated']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Statistics
    stats = calculate_stats(roadmap_data)
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <h2>{stats['total']}</h2>
            <p>Total Features</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-card status-completed">
            <h2>{stats['completed']}</h2>
            <p>✅ Completed</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stat-card status-in-progress">
            <h2>{stats['in_progress']}</h2>
            <p>🚧 In Progress</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="stat-card status-planned">
            <h2>{stats['planned']}</h2>
            <p>📋 Planned</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col5:
        st.markdown(f"""
        <div class="stat-card status-refining">
            <h2>{stats['refining']}</h2>
            <p>🪄 Refining</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col6:
        st.markdown(f"""
        <div class="stat-card status-on-hold">
            <h2>{stats['on_hold']}</h2>
            <p>⏸️ On Hold</p>
        </div>
        """, unsafe_allow_html=True)

    # Progress overview
    completion_rate = (stats['completed'] / stats['total']) * 100 if stats['total'] > 0 else 0
    st.markdown("---")
    st.markdown(f"### 📊 Overall Progress: {completion_rate:.1f}% Complete")
    st.progress(completion_rate / 100)
    
    # Funding Campaign Message
    st.markdown("---")
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 15px; 
                padding: 25px; 
                margin: 20px 0; 
                color: white; 
                text-align: center;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        <h2>🚀 Support RowTok's Development</h2>
        <p style="font-size: 1.1rem; margin: 15px 0;">
            RowTok is currently a solo startup project developed with passion for the rowing community. 
            Your support can help accelerate development and bring more features to water sports athletes worldwide!
        </p>
        <p style="font-size: 1rem; margin: 15px 0; opacity: 0.9;">
            <strong>🎯 Funding Goals:</strong><br>
            • Faster feature development<br>
            • Enhanced GPS accuracy algorithms<br>
            • Professional infrastructure scaling<br>
            • Multi-platform mobile apps<br>
            • Advanced AI coaching features
        </p>
        <p style="font-size: 0.9rem; margin-top: 20px; opacity: 0.8;">
            Interested in contributing or partnering? Contact us to be part of the RowTok journey!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Roadmap timeline
    st.markdown("---")
    st.markdown("## 🗓️ Development Timeline")
    
    # Filter options
    col1, col2, col3 = st.columns(3)
    
    with col1:
        status_filter = st.selectbox(
            "Filter by Status:",
            ["All", "Completed", "In Progress", "Planned", "Refining", "On Hold"]
        )
    
    with col2:
        priority_filter = st.selectbox(
            "Filter by Priority:",
            ["All", "High", "Medium", "Low"]
        )
        
    with col3:
        team_filter = st.selectbox(
            "Filter by Team:",
            ["All", "Pedro Ciancaglini", "Gervasio Merchand"]
        )
    
    # Display roadmap
    for quarter, features in roadmap_data["quarters"].items():
        st.markdown(f"""
        <div class="quarter-header">
            <h2>🎯 {quarter}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Filter features
        filtered_features = features
        if status_filter != "All":
            filtered_features = [f for f in filtered_features if f["status"] == status_filter]
        if priority_filter != "All":
            filtered_features = [f for f in filtered_features if f["priority"] == priority_filter]
        if team_filter != "All":
            filtered_features = [f for f in filtered_features if f["team"] == team_filter]
        
        if not filtered_features:
            st.info(f"No features match the current filters for {quarter}")
            continue
        
        for feature in filtered_features:
            status_class = get_status_class(feature["status"])
            status_emoji = get_status_emoji(feature["status"])
            
            st.markdown(f"""
            <div class="feature-card {status_class}">
                <div class="feature-title">
                    {status_emoji} {feature['feature']}
                </div>
                <div class="feature-description">
                    {feature['description']}
                </div>
                <div class="feature-meta">
                    <div>
                        <strong>Team:</strong> {feature['team']} | 
                        <strong>Priority:</strong> {feature['priority']} | 
                        <strong>Release:</strong> {feature['release_date']}
                    </div>
                    <div class="status-badge">
                        {feature['status']} ({feature['progress']}%)
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Progress bar for in-progress and refining items
            if feature["status"] in ["In Progress", "Refining"] and feature["progress"] > 0:
                st.progress(feature["progress"] / 100)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #666;">
        <p>🌊 RowTok - Solo Startup Built with Passion for Water Sports Excellence 🌊</p>
        <p><em>This roadmap is subject to change based on user feedback, funding, and technical requirements</em></p>
        <p style="font-size: 0.9rem; margin-top: 10px;">
            <strong>Developer:</strong> Pedro Ciancaglini | <strong>Infrastructure:</strong> Gervasio Merchand
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
import streamlit as st
import time
import base64
import os

# Initialize session state for controlling the beat
if 'is_playing' not in st.session_state:
    st.session_state.is_playing = False

# Function to get base64 encoded audio
def get_audio_base64(audio_file_path):
    with open(audio_file_path, "rb") as f:
        audio_bytes = f.read()
    return base64.b64encode(audio_bytes).decode()

# Get the base64 encoded audio
try:
    audio_base64 = get_audio_base64("pages/research/tom.mp3")
except Exception as e:
    st.error(f"Could not load audio file: {e}")
    audio_base64 = ""

# Add custom CSS for the beat indicator and audio setup
st.markdown(f"""
<style>
    .beat-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 20px 0;
    }}
    .beat-indicator {{
        background-color: #ff4b4b;
        color: white;
        font-size: 48px;
        font-weight: bold;
        padding: 20px 40px;
        border-radius: 15px;
        opacity: 0;
        transition: opacity 0.1s;
    }}
    .beat-indicator.visible {{
        opacity: 1;
    }}
</style>

<script>
    // Create audio element with base64 encoded sound
    const audio = new Audio("data:audio/mp3;base64,{audio_base64}");
    
    function playBeat() {{
        // Clone and play the audio for better performance
        const clone = audio.cloneNode();
        clone.play();
    }}
</script>
""", unsafe_allow_html=True)

# Create placeholder for beat indicator
beat_placeholder = st.empty()

def play_beat():
    """Play the beat using browser audio"""
    # The sound will be played by the JavaScript code
    pass

# Create two columns for the controls
col1, col2 = st.columns(2)

# Dropdown for selecting beats per minute (BPM)
with col1:
    bpm = st.selectbox("Select Beats Per Minute (BPM):", 
                       list(range(40, 125, 5)),
                       key='bpm')

# Start/Stop button
with col2:
    if not st.session_state.is_playing:
        if st.button("Start Beats"):
            st.session_state.is_playing = True
            st.rerun()
    else:
        if st.button("Stop Beats"):
            st.session_state.is_playing = False
            st.rerun()

# Display the current BPM
st.write(f"Playing at {bpm} BPM")

# Container for the beat indicator
beat_container = st.container()

# Play the beats with visual indicator
if st.session_state.is_playing:
    try:
        while st.session_state.is_playing:
            # Calculate the interval based on current BPM
            interval = 60 / bpm
            
            # Show beat indicator and trigger sound
            beat_placeholder.markdown("""
                <div class="beat-container">
                    <div class="beat-indicator visible">BEAT</div>
                </div>
                <script>
                    playBeat();
                </script>
            """, unsafe_allow_html=True)
            
            # Wait a short time to show the beat
            time.sleep(0.1)
            
            # Hide beat indicator
            beat_placeholder.markdown("""
                <div class="beat-container">
                    <div class="beat-indicator">BEAT</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Wait for the remaining interval
            remaining_time = interval - 0.1
            if remaining_time > 0:
                time.sleep(remaining_time)
            
    except Exception as e:
        st.error(f"Error: {e}")
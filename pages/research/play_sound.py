import streamlit as st
import time

# Initialize session state for controlling the beat
if 'is_playing' not in st.session_state:
    st.session_state.is_playing = False
if 'beat_trigger' not in st.session_state:
    st.session_state.beat_trigger = 0

# Add custom CSS for the beat indicator
st.markdown("""
<style>
    .beat-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 20px 0;
    }
    .beat-indicator {
        background-color: #ff4b4b;
        color: white;
        font-size: 48px;
        font-weight: bold;
        padding: 20px 40px;
        border-radius: 15px;
        opacity: 0;
        transition: opacity 0.1s;
    }
    .beat-indicator.visible {
        opacity: 1;
    }
    /* Hide the default audio player when not playing */
    .stAudio {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# Create placeholder for beat indicator and audio
beat_placeholder = st.empty()
audio_placeholder = st.empty()

# Load the audio file once
with open("pages/research/tom.mp3", "rb") as f:
    audio_bytes = f.read()

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
            
            # Show beat indicator and play sound
            beat_placeholder.markdown("""
                <div class="beat-container">
                    <div class="beat-indicator visible">BEAT</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Play the sound using st.audio
            st.session_state.beat_trigger += 1
            audio_placeholder.audio(audio_bytes, format='audio/mp3', start_time=0)
            
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
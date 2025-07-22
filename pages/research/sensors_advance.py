import streamlit as st
import pandas as pd
import numpy as np

# Set page config for a wider layout and cleaner look
st.set_page_config(layout="wide", page_title="Device Sensor Analysis", page_icon="🔬")

# Custom CSS for a more polished look and feel
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6;
    }
    .sidebar .sidebar-content {
        background: #f8f9fa;
    }
    .st-bv {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .st-cc {
        color: #333;
    }
    h1, h2, h3 {
        color: #0d6efd;
    }
    .sensor-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 20px;
    }
    .sensor-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    .sensor-card:hover {
        transform: translateY(-5px);
    }
    .sensor-name {
        font-size: 1.2em;
        font-weight: bold;
        color: #333;
    }
    .status-available {
        color: #28a745;
        font-weight: bold;
    }
    .status-unavailable {
        color: #dc3545;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- App Header ---
st.title("🔬 Device Sensor Availability")
st.markdown("This application analyzes the sensors available on your device. Based on the results, we can determine which features and modules can be offered.")

# --- Sensor Data ---
# In a real-world scenario, you would use JavaScript to detect these sensors.
# For this example, we'll simulate the detection with random data.
sensors = {
    "Accelerometer": np.random.choice([True, False], p=[0.8, 0.2]),
    "Gyroscope": np.random.choice([True, False], p=[0.7, 0.3]),
    "Magnetometer": np.random.choice([True, False], p=[0.6, 0.4]),
    "GPS": np.random.choice([True, False], p=[0.9, 0.1]),
    "Barometer": np.random.choice([True, False], p=[0.4, 0.6]),
    "Proximity Sensor": np.random.choice([True, False], p=[0.8, 0.2]),
    "Ambient Light Sensor": np.random.choice([True, False], p=[0.8, 0.2]),
    "Heart Rate Monitor": np.random.choice([True, False], p=[0.2, 0.8]),
    "Fingerprint Sensor": np.random.choice([True, False], p=[0.7, 0.3]),
    "NFC": np.random.choice([True, False], p=[0.5, 0.5]),
    "Pedometer": np.random.choice([True, False], p=[0.6, 0.4]),
    "Thermometer": np.random.choice([True, False], p=[0.1, 0.9]),
}

# --- Display Sensor Status ---
st.header("Sensor Analysis Results")
st.markdown('<div class="sensor-grid">', unsafe_allow_html=True)

for sensor, available in sensors.items():
    status_text = "Available" if available else "Not Available"
    status_class = "status-available" if available else "status-unavailable"
    icon = "✅" if available else "❌"
    
    st.markdown(f"""
    <div class="sensor-card">
        <div class="sensor-name">{icon} {sensor}</div>
        <div class="{status_class}">{status_text}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- Feature Availability ---
st.header("Module and Feature Availability")
st.markdown("Based on the sensor analysis, here are the features that can be enabled on this device:")

feature_requirements = {
    "Augmented Reality (AR)": ["Accelerometer", "Gyroscope"],
    "Advanced Navigation": ["GPS", "Magnetometer"],
    "Fitness Tracking": ["Pedometer", "Heart Rate Monitor"],
    "Contactless Payments": ["NFC"],
    "Automatic Screen Brightness": ["Ambient Light Sensor"],
    "Weather Forecasting": ["Barometer", "Thermometer"],
}

for feature, required_sensors in feature_requirements.items():
    is_available = all(sensors.get(sensor, False) for sensor in required_sensors)
    
    if is_available:
        st.success(f"**{feature}:** Available")
        st.markdown(f"  - *Requires: {', '.join(required_sensors)}*")
    else:
        st.error(f"**{feature}:** Not Available")
        missing_sensors = [s for s in required_sensors if not sensors.get(s, False)]
        st.markdown(f"  - *Missing sensors: {', '.join(missing_sensors)}*")

# --- Detailed Sensor Information ---
st.header("Detailed Sensor Information")
st.markdown("The following table provides a summary of all analyzed sensors and their availability.")

sensor_df = pd.DataFrame(list(sensors.items()), columns=["Sensor", "Available"])
sensor_df["Status"] = sensor_df["Available"].apply(lambda x: "✅ Available" if x else "❌ Not Available")

st.dataframe(sensor_df[["Sensor", "Status"]].style.applymap(
    lambda x: 'color: green' if "Available" in x else 'color: red', subset=['Status']
))

# --- Footer ---
st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit")

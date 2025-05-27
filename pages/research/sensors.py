import streamlit as st
from streamlit.components.v1 import html

st.title("📱 Phone Sensors Live Feedback")

# We embed all our logic in one HTML blob:
html("""
<!DOCTYPE html>
<html>
  <head>
    <style>
      body { font-family: sans-serif; margin:0; padding:1rem; }
      h2 { margin-bottom: 0.2rem; }
      ul { list-style: none; padding: 0; }
      li { margin: 0.1rem 0; }
      #readings p { margin: 0.2rem 0; font-family: monospace; }
    </style>
  </head>
  <body>
    <h2>Supported Sensors</h2>
    <ul id="sensor-list"></ul>
    <h2>Live Sensor Data</h2>
    <div id="readings"></div>

    <script>
      const sensors = [
        { name: 'Accelerometer', ctor: window.Accelerometer,       opts: { frequency: 60 } },
        { name: 'Gyroscope',     ctor: window.Gyroscope,           opts: { frequency: 60 } },
        { name: 'Magnetometer',  ctor: window.Magnetometer,        opts: { frequency: 60 } },
        // Not every browser/device supports AmbientLightSensor:
        { name: 'Ambient Light', ctor: window.AmbientLightSensor, opts: { frequency: 1  } },
        // For orientation you can use the older events:
        { name: 'DeviceOrientationEvent', ctor: 'DeviceOrientationEvent', opts: null }
      ];

      // 1. List support
      sensors.forEach(s => {
        const li = document.createElement('li');
        if (s.ctor && (s.ctor !== 'DeviceOrientationEvent' ? s.ctor.prototype : true)) {
          li.innerText = s.name;
        } else {
          li.innerText = s.name + ' (not supported)';
          li.style.opacity = 0.5;
        }
        document.getElementById('sensor-list').appendChild(li);
      });

      // 2. Hook up each sensor
      sensors.forEach(s => {
        if (!s.ctor) return;
        // DeviceOrientation uses global event listener
        if (s.ctor === 'DeviceOrientationEvent') {
          window.addEventListener('deviceorientation', ev => {
            const txt = `Orientation α:${ev.alpha.toFixed(1)} β:${ev.beta.toFixed(1)} γ:${ev.gamma.toFixed(1)}`;
            document.getElementById('readings').innerHTML = `<p>${txt}</p>` + 
              document.getElementById('readings').innerHTML;
          });
          return;
        }

        try {
          const sensor = new s.ctor(s.opts);
          sensor.addEventListener('reading', () => {
            // we assume x, y, z for these sensors
            const { x, y, z } = sensor;
            const txt = `${s.name}: x=${x.toFixed(2)}, y=${y.toFixed(2)}, z=${z.toFixed(2)}`;
            document.getElementById('readings').innerHTML = `<p>${txt}</p>` + 
              document.getElementById('readings').innerHTML;
          });
          sensor.start();
        } catch (err) {
          console.warn(`${s.name} error:`, err);
        }
      });

      // 3. Geolocation (works in all browsers, with permission)
      if ('geolocation' in navigator) {
        navigator.geolocation.watchPosition(pos => {
          const { latitude, longitude, accuracy } = pos.coords;
          const txt = `Geo: lat=${latitude.toFixed(5)}, lon=${longitude.toFixed(5)}, acc=${accuracy}m`;
          document.getElementById('readings').innerHTML = `<p>${txt}</p>` +
            document.getElementById('readings').innerHTML;
        }, err => console.warn('Geo err', err), { enableHighAccuracy: true });
      }
    </script>
  </body>
</html>
""", height=700)

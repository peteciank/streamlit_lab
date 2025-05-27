import streamlit as st
from streamlit.components.v1 import html

st.title("🚗 Rear-Mirror Viewer")

html(
    """
    <video id="mirror" autoplay playsinline 
           style="width:100%;height:auto;transform:scaleX(-1);">
    </video>
    <script>
      navigator.mediaDevices
        .getUserMedia({ video: { facingMode: { ideal: "environment" } } })
        .then(stream => {
          document.getElementById("mirror").srcObject = stream;
        })
        .catch(err => {
          console.error("Camera access error:", err);
        });
    </script>
    """,
    height=500,
)

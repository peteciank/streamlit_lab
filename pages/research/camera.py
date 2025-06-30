import streamlit as st
from streamlit.components.v1 import html

st.title("🔍 Phone-Mirror")

html(
    """
    <video id="mirror" autoplay muted playsinline 
           style="width:100%;height:auto;transform:scaleX(-1);">
    </video>
    <script>
      navigator.mediaDevices
        .getUserMedia({
          video: { facingMode: { ideal: "user" } }
        })
        .then(stream => {
          const video = document.getElementById("mirror");
          video.srcObject = stream;
        })
        .catch(err => {
          console.error("Camera access error:", err);
        });
    </script>
    """,
    height=500,
)

def navigate_home():
    st.switch_page("pages/home_page.py")  # Replace with your page file

if st.button("Go Home", on_click=navigate_home):
    pass

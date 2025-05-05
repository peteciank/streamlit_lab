import streamlit as st
from streamlit_superapp import State

NAME = "Counter"
TAG = "{A:}📚 Studies" # This page will appear in a group "📚 Studies" at the top of a index page
ICON = "🔢"

def main(page):
    counter = State("counter", default_value=0, key=page)

    if st.button("Increment"):
        # This is the same as binding a new value
        counter.value += 1

    # Initial value only updates after changing pages
    # or if we update it manually
    st.write(f"initial_value: {counter.initial_value}")
    st.write(f"current value: {counter.value}")
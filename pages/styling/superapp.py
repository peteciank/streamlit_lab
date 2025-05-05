import pandas as pd
import streamlit as st
from streamlit_superapp.state import State

ICON = "📊"

def main():
    state = State("df", default_value=get_base_input())


    with st.sidebar:
        if st.button("✖️ Multiply"):
            # The "state.value" is always the most updated value
            # So we can manipulate it before rendering it again
            state.initial_value = calculate(state.value)

        if st.button("🔄 Reset"):
            # Forcing a value update before rendering
            state.initial_value = get_base_input()

    # setting the "initial_value" and "key" is mandatory
    df = st.data_editor(data=state.initial_value, key=state.key, hide_index=True)

    # binding the new value to the state is mandatory!
    # plus you get the previous value for free!
    previous_df = state.bind(df)

    if not df.equals(previous_df):
        st.success("Data changed!")


def get_base_input():
    return pd.DataFrame(index=[0, 1, 2], columns=["a", "b"], dtype=float)


def calculate(df: pd.DataFrame):
    df["result"] = df["a"] * df["b"]

    return df

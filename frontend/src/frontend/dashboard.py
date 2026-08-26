import streamlit as st
import httpx

def main():
    st.markdown("# PokeDash")

    stats = httpx.get
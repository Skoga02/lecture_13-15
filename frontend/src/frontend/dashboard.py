import streamlit as st
import httpx
import os 

# try to get enviroment variable BASE_URL, if not exists default to 2nd argumnet 
BASE_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

# To run this dashboard, 
# Stand in frontend/src/frontend
# Command: uv run streamlit run dashboard.py


def main():
    st.markdown("# PokeDash")

    st.write(BASE_URL)

    stats = httpx.get(f"{BASE_URL}/pokemons/stats", timeout=30).json()
    st.dataframe(stats)

if __name__ == "__main__":
    main()
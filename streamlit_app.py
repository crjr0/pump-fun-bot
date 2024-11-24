import streamlit as st
import subprocess
import os

st.title("Pump-Fun-Bot")
st.write("Welcome to the Pump-Fun-Bot interface!")

# Sidebar for configuration
st.sidebar.header("Bot Configuration")
api_key = st.sidebar.text_input("API Key")
wallet_address = st.sidebar.text_input("Wallet Address")
max_gas_fee = st.sidebar.number_input("Max Gas Fee (in SOL)", min_value=0.0, value=0.1)
slippage = st.sidebar.number_input("Slippage Tolerance (%)", min_value=0.0, value=1.0)

# Start the bot
if st.button("Start Bot"):
    st.write("Starting the bot...")
    try:
        # Run the trade.py script in the bot folder
        result = subprocess.run(
            ['python', 'bot\\trade.py'],  # Use double backslashes for Windows paths
            capture_output=True,
            text=True
        )
        st.text(result.stdout)
        st.text(result.stderr)
    except Exception as e:
        st.error(f"Error: {e}")

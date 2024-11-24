import streamlit as st
import yaml
import os

# Configuration file path
CONFIG_FILE = "config.yml"

# Load existing configuration
def load_config(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    return {}

# Save updated configuration
def save_config(file_path, config_data):
    with open(file_path, "w") as file:
        yaml.dump(config_data, file, default_flow_style=False)

# Streamlit app interface
def app():
    st.title("Pump Fun Bot Configuration")

    # Load existing config
    config = load_config(CONFIG_FILE)

    # Input fields for trading parameters
    st.subheader("Trading Parameters")
    buy_amount = st.number_input(
        "Buy Amount (SOL)",
        value=config.get("BUY_AMOUNT", 0.0001),
        step=0.0001,
    )
    buy_slippage = st.number_input(
        "Buy Slippage (%)",
        value=config.get("BUY_SLIPPAGE", 0.2),
        step=0.1,
    )
    sell_slippage = st.number_input(
        "Sell Slippage (%)",
        value=config.get("SELL_SLIPPAGE", 0.2),
        step=0.1,
    )

    # Input fields for node information
    st.subheader("Node Information")
    rpc_endpoint = st.text_input(
        "Solana RPC Endpoint",
        value=config.get("RPC_ENDPOINT", ""),
    )
    wss_endpoint = st.text_input(
        "Solana WebSocket Endpoint",
        value=config.get("WSS_ENDPOINT", ""),
    )

    # Input field for private key
    st.subheader("Solana Private Key")
    private_key = st.text_area(
        "Enter your Solana Private Key",
        value=config.get("PRIVATE_KEY", ""),
    )

    # Pubkeys (predefined constants in the script)
    st.subheader("System & Pump Fun Addresses (Predefined)")
    st.code(
        """
PUMP_PROGRAM = 6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P
PUMP_GLOBAL = 4wTV1YmiEkRvAtNtsSGPtUrqRYQMe5SKy2uB4Jjaxnjf
PUMP_EVENT_AUTHORITY = Ce6TQqeHC9p8KetsN6JsjHK7UTZk7nasjjnr7XxXp9F1
PUMP_FEE = CebN5WGQ4jvEPvsVU4EoHEpgzq1VV7AbicfhtW4xC9iM
SYSTEM_PROGRAM = 11111111111111111111111111111111
SYSTEM_TOKEN_PROGRAM = TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA
SYSTEM_ASSOCIATED_TOKEN_ACCOUNT_PROGRAM = ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL
SYSTEM_RENT = SysvarRent111111111111111111111111111111111
SOL = So11111111111111111111111111111111111111112
LAMPORTS_PER_SOL = 1_000_000_000
        """
    )

    # Save Config Button
    if st.button("Save Configuration"):
        # Update the configuration dictionary
        config["BUY_AMOUNT"] = buy_amount
        config["BUY_SLIPPAGE"] = buy_slippage
        config["SELL_SLIPPAGE"] = sell_slippage
        config["RPC_ENDPOINT"] = rpc_endpoint
        config["WSS_ENDPOINT"] = wss_endpoint
        config["PRIVATE_KEY"] = private_key

        # Save configuration to file
        save_config(CONFIG_FILE, config)
        st.success("Configuration saved successfully!")

    # Display current configuration
    st.markdown("### Current Configuration")
    st.json(config)

if __name__ == "__main__":
    app()

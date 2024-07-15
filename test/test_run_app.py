import streamlit as st
from io import BytesIO
from millify import millify
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from io import BytesIO
import sys
from utils import (
    config_menu_footer, generate_card, empty_lines, get_delta, color_highlighter
)
from data import (
    get_income_statement, get_balance_sheet, get_stock_price, get_company_info,
    get_financial_ratios, get_key_metrics, get_cash_flow
)
from streamlit_option_menu import option_menu

# Define caching functions for each API call
@st.cache_data(ttl=60*60*24*30) # cache output for 30 days
def company_info(symbol):
    return get_company_info(symbol)

@st.cache_data(ttl=60*60*24*30) # cache output for 30 days
def income_statement(symbol):
    return get_income_statement(symbol)

@st.cache_data(ttl=60*60*24*30) # cache output for 30 days
def balance_sheet(symbol):
    return get_balance_sheet(symbol)

@st.cache_data(ttl=60*60*24*30) # cache output for 30 days
def stock_price(symbol):
    return get_stock_price(symbol)

@st.cache_data(ttl=60*60*24*30) # cache output for 30 days
def financial_ratios(symbol):
    return get_financial_ratios(symbol)

@st.cache_data(ttl=60*60*24*30) # cache output for 30 days
def key_metrics(symbol):
    return get_key_metrics(symbol)

@st.cache_data(ttl=60*60*24*30) # cache output for 30 days
def cash_flow(symbol):
    return get_cash_flow(symbol)

# Configure the app page
st.set_page_config(
    page_title='Financial Report',
    page_icon='📈',
    layout="centered",
)

# Initialize session state
if 'watch_list' not in st.session_state:
    st.session_state.watch_list = []

# Sidebar menu for navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Find a Stock", "Watch list"],
        icons=["search", "list"],
        default_index=0,
    )

# Page 1: Find a Stock
if selected == "Find a Stock":

    # Existing code for displaying the dashboard goes here
    # Display the app title
    st.title("Financial Report 📈")

    # Initialize the state of the button
    if 'btn_clicked' not in st.session_state:
        st.session_state['btn_clicked'] = False

    # Input symbol
    symbol = st.text_input("Enter Stock Symbol", value="AAPL", max_chars=5)

    # Save button functionality
    def save_to_watch_list():
        if symbol not in st.session_state.watch_list:
            st.session_state.watch_list.append(symbol)
            st.success(f"Added {symbol} to watch list!")

    # Add Save button
    if st.button("Save"):
        save_to_watch_list()

    # Display additional content based on your app's existing functionality

# Page 2: Watch list
elif selected == "Watch list":
    st.title("Watch list 📋")
    if st.session_state.watch_list:
        st.write("Saved stocks:")
        for stock in st.session_state.watch_list:
            st.write(f"- {stock}")
    else:
        st.write("No stocks in the watch list.")

# Configure the menu and footer with the user's information
# config_menu_footer()

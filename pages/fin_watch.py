import streamlit as st
from io import BytesIO
from millify import millify
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from io import BytesIO
import sys
from utils import (
     generate_card, empty_lines, get_delta, color_highlighter, logo
)
from data import (
    get_income_statement, get_balance_sheet, get_stock_price, get_company_info,
    get_financial_ratios, get_key_metrics, get_cash_flow
)

from streamlit_option_menu import option_menu



# st.title("Watch list 📋")
# # if st.session_state.watch_list:
# #     st.write("Saved stocks:")
# #     for stock in st.session_state.watch_list:
# #         generate_card(f"{stock}")
# # else:
# #     st.write("No stocks in the watch list.")


# if st.session_state.watch_list:
#     st.write("Saved stocks:")
#     for stock in st.session_state.watch_list:
#         if st.button(f"View {stock}", key=stock):
#             st.switch_page("pages/1_📊_Financial_Report.py")


# Initialize session state
if 'watch_list' not in st.session_state:
    st.session_state.watch_list = []   

st.title("Watch list 📋")

if 'watch_list' not in st.session_state:
    st.session_state.watch_list = []

if st.session_state.watch_list:
    st.write("Saved Companies:")
    for stock in st.session_state.watch_list:
        if st.button(f"View: {stock}", key=stock):
            st.session_state.selected_stock = stock 
            st.switch_page("fin_dash.py") and st.experimental_rerun()
             
else:
    st.write("No stocks in the watch list.")
    

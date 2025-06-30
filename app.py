# Trigger redeploy – fixing numpy/NaN crash
pip install --upgrade pip
import streamlit as st
from crypto_engine import get_crypto_signals
from stock_engine import get_stock_signals
from options_engine import get_options_spreads

st.set_page_config(page_title="Safe Trade Screener", layout="wide", page_icon="💹")
st.markdown("<h1 style='text-align: center; color: white;'>⚔️ Scrollfuel Safe Trade Screener</h1>", unsafe_allow_html=True)

tabs = st.tabs(["📈 Crypto", "📊 Stocks", "💰 Options"])

with tabs[0]:
    st.subheader("Crypto Safe Trades")
    crypto_df = get_crypto_signals()
    st.dataframe(crypto_df, use_container_width=True)

with tabs[1]:
    st.subheader("Stock Safe Trades")
    stock_df = get_stock_signals()
    st.dataframe(stock_df, use_container_width=True)

with tabs[2]:
    st.subheader("Safe Option Spreads")
    option_df = get_options_spreads()
    st.dataframe(option_df, use_container_width=True)

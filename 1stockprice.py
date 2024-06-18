import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Apple
""")
tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31')
st.write("""## Closing Price""")
st.line_chart(tickerDf.Close)
st.write("""## Volume""")
st.line_chart(tickerDf.Volume)
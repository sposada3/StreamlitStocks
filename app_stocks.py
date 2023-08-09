#Import packages
import yfinance as yf
import streamlit as st
import pandas as pd


#Titles
st.title("Simple Stock Price App")
st.markdown("Streamlit first project")
st.subheader("Shown are the stock closing price and volume!")


#Inspired by: https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

#Define the ticker symbol
tickerSymbol = st.selectbox("Pick a company", ['AMZN', 'CSCO','GOOGL', 'META', 'MSFT'])
st.markdown("Actual stock price:")

#Get data 
tickerData = yf.Ticker(tickerSymbol)

#Get the historical prices
tickerDf = tickerData.history(period='1d', start='2013-5-31', end=None)
# Open	High	Low	Close	Volume	Dividends	Stock Splits

#Get current price
current_price = tickerDf["Close"][-1]

#Data Shown
st.code(current_price)
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

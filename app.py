import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="Stock Beginner Analyser", layout="wide")

st.markdown("""

<style>
.stApp {
    background-color: #08111f;
    color: white;
}
</style>

""", unsafe_allow_html=True)

st.title("📈 Stock Beginner Analyser")

default_watchlist = ["AAPL", "MSFT", "NVDA", "TSLA", "PLTR", "RKLB", "BTC-USD"]

if "watchlist" not in st.session_state:
st.session_state.watchlist = default_watchlist

st.subheader("Live Watchlist")

rows = []

for ticker in st.session_state.watchlist:
try:
stock = yf.Ticker(ticker)
hist = stock.history(period="2d")

```
    current = round(hist["Close"].iloc[-1], 2)
    previous = round(hist["Close"].iloc[-2], 2)

    change = round(current - previous, 2)
    percent = round((change / previous) * 100, 2)

    rows.append({
        "Ticker": ticker,
        "Price": current,
        "Move": f"{change} ({percent}%)"
    })

except:
    rows.append({
        "Ticker": ticker,
        "Price": "Error",
        "Move": "No data"
    })
```

st.dataframe(pd.DataFrame(rows), use_container_width=True)

new_stock = st.text_input("Add ticker (Example: AAPL or BTC-USD)")

if st.button("Add Stock"):
if new_stock:
st.session_state.watchlist.append(new_stock.upper())
st.rerun()

selected = st.selectbox("Select stock chart", st.session_state.watchlist)

try:
chart_stock = yf.Ticker(selected)
chart_data = chart_stock.history(period="1mo")

```
st.subheader(f"{selected} Last 30 Days")
st.line_chart(chart_data["Close"])
```

except:
st.warning("Could not load chart data.")

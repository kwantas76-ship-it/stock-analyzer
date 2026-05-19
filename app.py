import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import date

st.set_page_config(page_title="Stock Beginner Analyser", page_icon="📈", layout="wide")

DEFAULT_WATCHLIST = ["AAPL", "MSFT", "NVDA", "TSLA", "PLTR", "RKLB", "BTC-USD"]

if "watchlist" not in st.session_state:
    st.session_state.watchlist = DEFAULT_WATCHLIST.copy()

st.markdown("""
<style>
.stApp {
    background: #07101f;
    color: #eaf1ff;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

.block-container {
    max-width: 1500px;
    padding-top: 0.5rem;
}

.hero {
    background: linear-gradient(90deg,#142347,#08111f);
    padding: 40px;
    border-radius: 0px 0px 20px 20px;
    margin-bottom: 30px;
}

.hero h1 {
    color: white;
    font-size: 60px;
    font-weight: 800;
}

.hero p {
    color: #c7d4eb;
    font-size: 22px;
    max-width: 1200px;
}

.card {
    background: linear-gradient(145deg,#1a2642,#111827);
    border: 1px solid #263858;
    border-radius: 30px;
    padding: 30px;
    min-height: 260px;
}

.card-title {
    color: #b8c6df;
    font-size: 18px;
}

.blue {
    color: #6ea8ff;
    font-size: 52px;
    font-weight: 800;
}

.yellow {
    color: #ffd75e;
    font-size: 52px;
    font-weight: 800;
}

.green {
    color: #39df90;
    font-size: 52px;
    font-weight: 800;
}

.card p {
    color: #c7d4eb;
    font-size: 22px;
    line-height: 1.6;
}

.panel {
    background: linear-gradient(145deg,#18233c,#111827);
    border: 1px solid #263858;
    border-radius: 30px;
    padding: 30px;
    margin-top: 30px;
}

.stButton button {
    background: #3168ff;
    color: white;
    border-radius: 14px;
    border: none;
    font-weight: 700;
}

.stTextInput input {
    background: #0b1528 !important;
    color: white !important;
    border: 1px solid #30456f !important;
}

h1,h2,h3 {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="hero">
<h1>Stock Beginner Analyser</h1>
<p>
A beginner-safe dashboard for daily market context, watchlist tracking,
news checks, YouTube claim reviews, and learning notes.
Not financial advice — designed to help you understand what is happening.
</p>
</div>
""", unsafe_allow_html=True)

@st.cache_data(ttl=300)
def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="5d")

        current = round(hist["Close"].iloc[-1], 2)
        previous = round(hist["Close"].iloc[-2], 2)

        change = round(current - previous, 2)
        percent = round((change / previous) * 100, 2)

        return {
            "Ticker": ticker,
            "Price": current,
            "Move": f"{change} ({percent}%)",
            "Meaning": "Live market movement",
            "Risk": "Always research before investing"
        }

    except:
        return {
            "Ticker": ticker,
            "Price": "Error",
            "Move": "No data",
            "Meaning": "Could not load",
            "Risk": "Check symbol"
        }

rows = []

for ticker in st.session_state.watchlist:
    rows.append(get_stock_data(ticker))

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="card">
    <div class="card-title">Market Mood</div>
    <div class="blue">Neutral</div>
    <p>Market is mixed. Watch indexes first.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <div class="card-title">Hype Risk</div>
    <div class="yellow">Watch</div>
    <p>Social media hype needs evidence.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
    <div class="card-title">Source Gate</div>
    <div class="green">On</div>
    <p>Using live Yahoo Finance data.</p>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="card">
    <div class="card-title">Learning Focus</div>
    <div class="blue">P/E</div>
    <p>Price-to-Earnings ratio explained.</p>
    </div>
    """, unsafe_allow_html=True)

left, right = st.columns([1.4,1])

with left:
    st.markdown('<div class="panel">', unsafe_allow_html=True)

    st.subheader("Your Watchlist")

    st.dataframe(
        pd.DataFrame(rows),
        use_container_width=True,
        hide_index=True
    )

    col1, col2 = st.columns([4,1])

    with col1:
        new_stock = st.text_input(
            "",
            placeholder="Add ticker e.g. AAPL or BTC-USD"
        )

    with col2:
        if st.button("Add"):
            if new_stock:
                st.session_state.watchlist.append(new_stock.upper())
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="panel">', unsafe_allow_html=True)

    st.subheader("Live Price Chart")

    selected = st.selectbox(
        "Choose stock",
        st.session_state.watchlist
    )

    try:
        chart_stock = yf.Ticker(selected)
        chart_data = chart_stock.history(period="1mo")

        st.line_chart(chart_data["Close"])

    except:
        st.warning("Could not load chart.")

    st.markdown('</div>', unsafe_allow_html=True)

st.info("Beginner rule: Learn the market before risking money.")

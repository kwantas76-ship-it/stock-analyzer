
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Stock Beginner Analyser",
    page_icon="📈",
    layout="wide",
)

if "watchlist" not in st.session_state:
    st.session_state.watchlist = ["AAPL", "MSFT", "NVDA", "TSLA", "RKLB", "PLTR", "BITCOIN"]

st.markdown("""
<style>
.stApp {
    background: #08111f;
    color: #e8eefc;
}
[data-testid="stHeader"] {
    background: rgba(8,17,31,0);
}
.block-container {
    padding-top: 1.4rem;
    max-width: 1450px;
}
.hero {
    background: linear-gradient(135deg, #0d1830 0%, #111d37 100%);
    border-bottom: 1px solid #22304d;
    padding: 24px 28px;
    border-radius: 0 0 22px 22px;
    margin-bottom: 24px;
}
.hero h1 {
    font-size: 34px;
    margin: 0;
    color: #f5f8ff;
    font-weight: 800;
}
.hero p {
    max-width: 850px;
    color: #aebbd4;
    font-size: 16px;
    line-height: 1.55;
}
.brief-card {
    float: right;
    margin-top: -72px;
    background: #141f34;
    border: 1px solid #273753;
    border-radius: 18px;
    padding: 18px 26px;
    text-align: center;
}
.brief-card .small {
    color: #9aa9c4;
    font-size: 12px;
}
.brief-card .date {
    color: #ffffff;
    font-size: 22px;
    font-weight: 800;
}
.card {
    background: #141a2b;
    border: 1px solid #273753;
    border-radius: 20px;
    padding: 20px;
    min-height: 155px;
    box-shadow: 0 20px 45px rgba(0,0,0,0.22);
}
.card h3 {
    margin: 0 0 12px 0;
    color: #ffffff;
    font-size: 17px;
}
.label {
    color: #93a1bb;
    font-size: 12px;
    margin-bottom: 8px;
}
.big-blue {
    color: #7ab1ff;
    font-size: 28px;
    font-weight: 800;
}
.big-yellow {
    color: #ffdb66;
    font-size: 28px;
    font-weight: 800;
}
.big-green {
    color: #39d98a;
    font-size: 28px;
    font-weight: 800;
}
.pill {
    display: inline-block;
    float: right;
    background: #202d49;
    color: #aebbd4;
    font-size: 12px;
    border-radius: 999px;
    padding: 6px 12px;
}
.card p {
    color: #bdc7da;
    line-height: 1.55;
}
.table-card {
    background: #141a2b;
    border: 1px solid #273753;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 20px 45px rgba(0,0,0,0.22);
}
.stTextInput > div > div > input {
    background-color: #0b1528;
    color: #e8eefc;
    border: 1px solid #273753;
    border-radius: 12px;
}
.stButton button {
    background: #3168ff;
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="hero">
    <h1>Stock Beginner Analyser</h1>
    <p>A beginner-safe dashboard for daily market context, watchlist tracking, news checks, YouTube claim reviews, and learning notes. Not financial advice — designed to help you understand what is happening.</p>
    <div class="brief-card">
        <div class="small">Daily Brief</div>
        <div class="date">{date.today().strftime("%b %d, %Y")}</div>
        <div class="small">Confidence: Medium</div>
    </div>
</div>
""", unsafe_allow_html=True)

top1, top2, top3, top4 = st.columns(4)

with top1:
    st.markdown("""
    <div class="card">
        <span class="pill">V1</span>
        <div class="label">Market Mood</div>
        <div class="big-blue">Neutral</div>
        <p>Market is mixed. Check indexes first, then watchlist moves, then company-specific news.</p>
    </div>
    """, unsafe_allow_html=True)

with top2:
    st.markdown("""
    <div class="card">
        <span class="pill">YouTube</span>
        <div class="label">Hype Risk</div>
        <div class="big-yellow">Watch</div>
        <p>Influencer claims need evidence from prices, filings, earnings, or trusted data sources.</p>
    </div>
    """, unsafe_allow_html=True)

with top3:
    st.markdown("""
    <div class="card">
        <span class="pill">Audit</span>
        <div class="label">Source Gate</div>
        <div class="big-green">On</div>
        <p>No conclusion should be trusted unless it has a source, timestamp, or data snapshot.</p>
    </div>
    """, unsafe_allow_html=True)

with top4:
    st.markdown("""
    <div class="card">
        <span class="pill">Tutor</span>
        <div class="label">Learning Focus</div>
        <div class="big-blue">P/E</div>
        <p>Today’s concept: Price-to-Earnings ratio — what investors pay for each dollar of earnings.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

left, right = st.columns([1.35, 1])

with left:
    st.markdown('<div class="table-card">', unsafe_allow_html=True)
    st.subheader("Your Watchlist")

    risk_notes = {
        "AAPL": "Check earnings and news.",
        "MSFT": "Watch valuation.",
        "NVDA": "High expectations can create volatility.",
        "TSLA": "Hype and sentiment can swing price.",
        "RKLB": "Growth stocks can be volatile.",
        "PLTR": "Check revenue growth vs valuation.",
        "BITCOIN": "Research before reacting.",
    }

    rows = []
    for ticker in st.session_state.watchlist:
        rows.append({
            "Ticker": ticker,
            "Move": "—",
            "Beginner Meaning": "Waiting for live data.",
            "Risk Note": risk_notes.get(ticker, "Check the evidence first."),
        })

    st.dataframe(rows, use_container_width=True, hide_index=True)

    c1, c2, c3 = st.columns([4, 1, 1])
    with c1:
        new_ticker = st.text_input("Add ticker", placeholder="Add ticker e.g. AAPL", label_visibility="collapsed")
    with c2:
        if st.button("Add", use_container_width=True):
            cleaned = new_ticker.strip().upper()
            if cleaned and cleaned not in st.session_state.watchlist:
                st.session_state.watchlist.append(cleaned)
                st.rerun()
    with c3:
        if st.button("Reset", use_container_width=True):
            st.session_state.watchlist = ["AAPL", "MSFT", "NVDA", "TSLA", "RKLB", "PLTR", "BITCOIN"]
            st.rerun()

    remove = st.selectbox("Remove a ticker", [""] + st.session_state.watchlist)
    if remove:
        st.session_state.watchlist.remove(remove)
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="table-card">', unsafe_allow_html=True)
    st.subheader("Market Index Summary")
    st.dataframe(
        [
            {"Index": "S&P 500", "Status": "Mixed", "Plain English": "Broad US market direction."},
            {"Index": "Nasdaq", "Status": "Volatile", "Plain English": "Tech-heavy market mood."},
            {"Index": "NZ Market", "Status": "Check", "Plain English": "Useful for local context."},
        ],
        use_container_width=True,
        hide_index=True,
    )
    st.caption("Connect this later to OpenBB, FMP, Yahoo Finance, or another market data source.")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")

bottom1, bottom2, bottom3 = st.columns(3)

with bottom1:
    st.markdown("""
    <div class="card">
        <h3>News Context Agent</h3>
        <p>Pulls article summaries, links them to tickers/sectors, separates fact from opinion, and scores importance.</p>
    </div>
    """, unsafe_allow_html=True)

with bottom2:
    st.markdown("""
    <div class="card">
        <h3>YouTube Claim Checker</h3>
        <p>Paste a video claim or transcript later. The app will compare hype claims against prices, filings, and news.</p>
    </div>
    """, unsafe_allow_html=True)

with bottom3:
    st.markdown("""
    <div class="card">
        <h3>Audit / Evidence Layer</h3>
        <p>Stores source URLs, timestamps, raw JSON snapshots, and daily reports so you can check everything later.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.info("V1 rule: This dashboard teaches and explains. It does not give buy/sell instructions.")

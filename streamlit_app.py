import streamlit as st
import yfinance as yf

st.set_page_config(page_title="DAX ETF Dashboard", layout="wide")
st.title("📊 DAX ETF – Finanz-Kennzahlen")

ticker_symbol = "EXS1.DE"
ticker = yf.Ticker(ticker_symbol)
info = ticker.info
hist = ticker.history(period="1y")

# ⏱️ Aktueller Kurs
st.metric("Aktueller Kurs", f"{info.get('regularMarketPrice', 'N/A')} €")
st.write(f"52-Wochen-Spanne: {info.get('fiftyTwoWeekLow')} € – {info.get('fiftyTwoWeekHigh')} €")

# 📈 Kurschart
st.subheader("📈 Kursverlauf (12 Monate)")
st.line_chart(hist['Close'])

# 🧮 Fundamentalkennzahlen
st.subheader("📌 Fundamentale Kennzahlen")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("KGV", round(info.get("trailingPE", 0), 2))
    st.metric("KBV", round(info.get("priceToBook", 0), 2))

with col2:
    div = info.get("dividendYield", 0)
    st.metric("Dividendenrendite", f"{round(div * 100, 2)} %" if div else "N/A")
    st.metric("Marktkapitalisierung", f"{round(info.get('marketCap', 0) / 1e9, 2)} Mrd. €")

with col3:
    st.metric("TER (geschätzt)", "0,16 %")
    st.metric("Ausschüttung", "Thesaurierend")
    st.metric("Replikation", "Physisch")

# Hinweis
st.caption("📘 Quelle: Yahoo Finance / iShares / justETF – Stand: April 2025")

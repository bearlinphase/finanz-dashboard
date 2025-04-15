import streamlit as st
import yfinance as yf

st.set_page_config(page_title='Finanz-Dashboard', layout='wide')
st.title("📊 Finanz-Dashboard mit Streamlit")

ticker = st.text_input("Gib ein Ticker-Symbol ein (z. B. AAPL, DAI.DE, INDA):", "AAPL")

if ticker:
    data = yf.Ticker(ticker)
    hist = data.history(period="1y")

    st.subheader("📈 Kursverlauf")
    st.line_chart(hist['Close'])

    st.subheader("📌 Fundamentaldaten")
    st.write({
        "KGV": data.info.get("trailingPE"),
        "KBV": data.info.get("priceToBook"),
        "Dividendenrendite": data.info.get("dividendYield"),
        "Marktkapitalisierung": data.info.get("marketCap")
    })
else:
    st.warning("Bitte gib ein Ticker-Symbol ein.")

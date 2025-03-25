import streamlit as st

st.title("My new Lens App")
st.write(
    "Ein kleines Sommerprojekt aus Lust und Laune")
tab1, tab2, tab3 = st.tabs(["Willkommen", "Todo", "LEER"])
with tab1: # Welcome Page
    'Dies ist mein kleines Privates Projekt, hier möchte ich ein paar Stunden investieren.'
    'Ich möchte eine App zu kreieren, welche Short-Term und Long-Term Investment-Entscheidungen unterstützen soll.'
with tab2: # Todo-Liste
    'Was noch Ansteht:'
    '- Longterm-Tab: Insider Scraping integrieren. Möglichst viel aus altem Projekt übernehmen.'
    '- Shortterm-Tab: Integration von Fundamentalanalyse und Indikatoren. Evtl. Option Pricing als Tab hierunter einführen'
    '- Integration vom Investment-Rechner den ich bereits in Excel umgesetzt hatte. -> Evtl. Python in Excel navigieren lassen.'
    '- Fear and Greed Index wie bei Quiverquant nur evtl. stattdessen durch Twitter Scraping'
    'Lobbying index mit api auf https://lda.senate.gov/api/ wie https://www.quiverquant.com/lobbying/'
with st.sidebar: st.write('Notes in Sidebar')
with tab3:
    'LEERER TAB'
import streamlit as st
from PIL import Image

def introduction():
    #st.title(":currency_exchange:Crypto Risk Tolerance Assessment")

    st.write("The object of this Risk Calculator is to estimate the risk tolerance of a cryptocurrency. This project uses two approaches that provide two individual risk scores.")

    st.write("Approach 1 explaination")
    st.write("Approach 2 explaination")
    col1, col2, col3 = st.columns((0.3,1,0.3))
    col2.image("coin.gif")

    st.sidebar.info("This Cryptocurrency risk estimation tool is designed and built by 李鸿鹄")



import ssl
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px

from distribution_analysis import distribution_analysis
from intro import introduction
from user_analysis import user_analysis

def main():
    # Streamlit web
    st.set_page_config(layout="wide")

    st.title(":currency_exchange:Crypto Risk Tolerance Assessment")

    with st.sidebar:
        selected_page = option_menu(
            "Menu",
            options = ("Introduction", "User Analysis","Volatility Analysis"),
            icons = ("house","gear","gear"),
            menu_icon = "cast"
        )
    if selected_page == "Introduction":
        introduction()
    
    elif selected_page == "User Analysis":
        user_analysis()

    elif selected_page == "Volatility Analysis":
        distribution_analysis()


if __name__ == "__main__":
    main()

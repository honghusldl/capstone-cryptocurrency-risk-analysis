import ssl
import streamlit as st
from streamlit_option_menu import option_menu

from distribution_analysis_page import distribution_analysis
from introduction_page import introduction
from user_analysis_page import user_analysis

# print('test')

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

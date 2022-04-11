import numpy as np, pandas as pd
import ssl
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px

from functions import get_crypto_api, get_coin_list, get_max_density, find_best_distribution, data_wrangling, get_name_parameters,get_historical_data, cauchy_pdf, chi2_pdf, expon_pdf, exponpow_pdf, gamma_pdf, lognorm_pdf, norm_pdf, powerlaw_pdf, rayleigh_pdf, uniform_pdf

get_pdfs = {
    'cauchy':cauchy_pdf,
    'chi2':chi2_pdf,
    'expon':expon_pdf,
    'exponpow':exponpow_pdf,
    'gamma':gamma_pdf,
    'lognorm':lognorm_pdf,
    'norm':norm_pdf,
    'powerlaw':powerlaw_pdf,
    'rayleigh':rayleigh_pdf,
    'uniform':uniform_pdf
}

def distribution_analysis():
    coin_list = get_coin_list(get_crypto_api())
    coin_names = list(coin_list.keys())
    coin_names.insert(0, "Select a coin")
    selected_coin = st.selectbox(
        "Choose a coin:",
        coin_names
    )
    if selected_coin != "Select a coin":
        price = "{:,}".format(round(coin_list[selected_coin]['price'],2))
        volume = "{:,}".format(round(coin_list[selected_coin]['volume'],2))
        symbol = coin_list[selected_coin]['symbol']
        st.markdown(f"**Price** : (USD) ${price}")
        st.markdown(f"**Volume** : ${volume}") 
        st.markdown(f"**Symbol** : {symbol}") 
        st.subheader(":point_down:Enter a Weight for each indicator")
        st.markdown("---")
        

        # some design adjustments
        st.write(
            """
            <style>
            [data-testid="stMetricDelta"] div {
                #border: 1px outset green;
                #background-color: lightblue;
                #text-align: center;
                font-family: 'SmallCaps', sans-serif;
                font-weight: bold;
                font-size: 30px;
                #text-shadow: 0.2em 0.2em /* 0.2em */ silver ;
            }
            [data-testid="stMetricValue"] div {
                font-size: 35px;
            }
            [class="stNumberInput"] div {
                width: 70%;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # price change 24h
        st.metric("", f"{selected_coin} Price Change in 24 Hours", delta=f"{round(coin_list[selected_coin]['pc_24h'], 2)}%", delta_color="normal")
        weight_pc_24h = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 1
        )
        st.markdown("---")

        # price change 7d
        st.metric("", f"{selected_coin} Price Change in 7 Days", delta=f"{round(coin_list[selected_coin]['pc_7d'], 2)}%", delta_color="normal")
        weight_pc_7d = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 2
        )
        st.markdown("---")

        # price change 30d
        st.metric("", f"{selected_coin} Price Change in 30 Days", delta=f"{round(coin_list[selected_coin]['pc_30d'], 2)}%", delta_color="normal")
        weight_pc_30d = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 3
        )
        st.markdown("---")

        # price change 60d
        st.metric("", f"{selected_coin} Price Change in 60 Days", delta=f"{round(coin_list[selected_coin]['pc_60d'], 2)}%", delta_color="normal")
        weight_pc_60d = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 4
        )
        st.markdown("---")

        # price change 90d
        st.metric("", f"{selected_coin} Price Change in 90 Days", delta=f"{round(coin_list[selected_coin]['pc_90d'], 2)}%", delta_color="normal")
        weight_pc_90d = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 5
        )
        st.markdown("---")

        # volume change 24h
        st.metric("", f"{selected_coin} Price Change in 24 Hours", delta=f"{round(coin_list[selected_coin]['volume_change'], 2)}%", delta_color="normal")
        weight_volume_24h = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 6
        )
        st.markdown("---")

        # CALCULATIONS
        df = get_historical_data(coin_list[selected_coin]['symbol'])
        df = data_wrangling(df)

        try:
            best_dist
        except:
            if np.isinf(df).values.sum() > 0:
                df_find = df.replace([np.inf, -np.inf], np.nan)
                best_dist = find_best_distribution(df_find)

            else:
                best_dist = find_best_distribution(df)


        distname_pc_24h, distparams_pc_24h = get_name_parameters(best_dist, '%price_change_24h')
        result_pc_24h = get_pdfs[distname_pc_24h](coin_list[selected_coin]['pc_24h'], distparams_pc_24h)

        distname_pc_7d, distparams_pc_7d = get_name_parameters(best_dist, '%price_change_7d')
        result_pc_7d = get_pdfs[distname_pc_7d](coin_list[selected_coin]['pc_7d'], distparams_pc_7d)

        distname_pc_30d, distparams_pc_30d = get_name_parameters(best_dist, '%price_change_30d')
        result_pc_30d = get_pdfs[distname_pc_30d](coin_list[selected_coin]['pc_30d'], distparams_pc_30d)

        distname_pc_60d, distparams_pc_60d = get_name_parameters(best_dist, '%price_change_60d')
        result_pc_60d = get_pdfs[distname_pc_60d](coin_list[selected_coin]['pc_60d'], distparams_pc_60d)

        distname_pc_90d, distparams_pc_90d = get_name_parameters(best_dist, '%price_change_90d')
        result_pc_90d = get_pdfs[distname_pc_90d](coin_list[selected_coin]['pc_90d'], distparams_pc_90d)

        distname_volume_change_24h, distparams_volume_change_24h = get_name_parameters(best_dist, '%volume_change_24h')
        result_volume_change_24h = get_pdfs[distname_volume_change_24h](coin_list[selected_coin]['volume_change'], distparams_volume_change_24h)

        final_result = result_pc_24h * 100 * weight_pc_24h / get_max_density(df,'%price_change_24h') + \
            result_pc_7d * 100 * weight_pc_7d / get_max_density(df, '%price_change_7d') + \
                result_pc_30d * 100 * weight_pc_30d / get_max_density(df, '%price_change_30d') + \
                    result_pc_60d * 100 * weight_pc_60d / get_max_density(df, '%price_change_60d') + \
                        result_pc_90d * 100 * weight_pc_90d / get_max_density(df, '%price_change_90d') + \
                            result_volume_change_24h * 100 * weight_volume_24h / get_max_density(df, '%volume_change_24h')
                            
        weight_sum = sum([weight_pc_24h,weight_pc_30d,weight_pc_60d,weight_pc_7d,weight_pc_90d,weight_volume_24h])
        risk_output = round(100 - (final_result / weight_sum),1)
        
        
        # display risk index to users
        if st.button('Calculate'):
            if (weight_pc_24h == 0) & (weight_pc_30d == 0) & (weight_pc_60d == 0) & (weight_pc_7d == 0) & (weight_pc_90d == 0) & (weight_volume_24h == 0):
                st.write('Please, enter the weights properly.')
            else:
                st.metric(label = f"Risk Index for {selected_coin}", value = f"{risk_output}%")
        else:
            st.write('Click the button to calculate the risk.')

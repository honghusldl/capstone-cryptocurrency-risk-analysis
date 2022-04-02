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
        st.markdown(f"**Price** : (USD)$ {coin_list[selected_coin]['price']}")
        st.markdown(f"**Volume** : {coin_list[selected_coin]['volume']}")
        st.markdown("---")

        st.markdown(f"**Price Change in 24 Hours** :  {round(coin_list[selected_coin]['pc_24h'] * 100, 3)}%")
        weight_pc_24h = st.number_input(
            "Please Enter a Weight:",
            min_value = 0,
            max_value = 100,
            step = 1,
            key = 1
        )
        st.markdown("---")

        st.markdown(f"**Price Change in 7 Days** :  {round(coin_list[selected_coin]['pc_7d'],3)}%")
        weight_pc_7d = st.number_input(
            "Please Enter a Weight:",
            min_value = 0,
            max_value = 100,
            step = 1,
            key = 2
        )
        st.markdown("---")

        st.markdown(f"**Price Change in 30 Days** :  {round(coin_list[selected_coin]['pc_30d'],3)}%")
        weight_pc_30d = st.number_input(
            "Please Enter a Weight:",
            min_value = 0,
            max_value = 100,
            step = 1,
            key = 3
        )
        st.markdown("---")

        st.markdown(f"**Price Change in 60 Days** :  {round(coin_list[selected_coin]['pc_60d'],3)}%")
        weight_pc_60d = st.number_input(
            "Please Enter a Weight:",
            min_value = 0,
            max_value = 100,
            step = 1,
            key = 4
        )
        st.markdown("---")

        st.markdown(f"**Price Change in 90 Days** :  {round(coin_list[selected_coin]['pc_90d'],3)}%")
        weight_pc_90d = st.number_input(
            "Please Enter a Weight:",
            min_value = 0,
            max_value = 100,
            step = 1,
            key = 5
        )
        st.markdown("---")

        st.markdown(f"**Volume Change in 24 Hours** : {round(coin_list[selected_coin]['volume_change'],3)}%")
        weight_volume_24h = st.number_input(
            "Please Enter a Weight:",
            min_value = 0,
            max_value = 100,
            step = 1,
            key = 6
        )
        st.markdown("---")

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

        # for col in df.drop(['date','volume','price','market cap'], axis = 1).columns:

        #     dist_name, dist_params = get_name_parameters(best_dist, col)

        #     result = get_pdfs[dist_name](x, dist_params)

        #     final_result += weight* result / get_max_density(df,col)
        #     normed_final_result = final_result/6 * 100
        #     risk = 1 - normed_final_result

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

        final_result = result_pc_24h * weight_pc_24h / 100 / get_max_density(df,'%price_change_24h') + \
            result_pc_7d * weight_pc_7d / 100 / get_max_density(df, '%price_change_7d') + \
                result_pc_30d * weight_pc_30d / 100 / get_max_density(df, '%price_change_30d') + \
                    result_pc_60d * weight_pc_60d / 100 / get_max_density(df, '%price_change_60d') + \
                        result_pc_90d * weight_pc_90d / 100 / get_max_density(df, '%price_change_90d') + \
                            result_volume_change_24h * weight_volume_24h / 100 / get_max_density(df, '%volume_change_24h')
        
        risk_output = (100 - (final_result / 6 * 100))
        # risk_output = 1 - risk_output
        # display risk index to users

        if (weight_pc_24h != 0) & (weight_pc_30d != 0) & (weight_pc_60d != 0) & (weight_pc_7d != 0) & (weight_pc_90d != 0) & (weight_volume_24h != 0) :
            st.metric(label = f"Risk Index for {selected_coin}", value = f"{round(risk_output,1)}%")
        else:
            st.metric(label = f"Risk Index for {selected_coin}", value = "Calculation in progress...", delta = "Enter all weights for risk estimation", delta_color = "off")
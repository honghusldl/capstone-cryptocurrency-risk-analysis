import streamlit as st
from functions import get_crypto_api, get_coin_list
from datetime import datetime
from pytz import timezone
import pandas as pd

def user_analysis():
# # BUILDING THE WEB PAGE
# st.title ("Risk tolerance assessment")
    coin_list = get_coin_list(get_crypto_api())
    coin_names = list(coin_list.keys())
    coin_names.insert(0, "Select a coin")
    

    add_selectbox = st.selectbox(
        "Choose a coin:",
        coin_names
    )


    if add_selectbox != 'Select a coin':
        
        st.subheader("Enter a Score and a Weight for each indicator")
        
        st.markdown("""
        <style>
        <span style="color:blue">some *blue* text</span>
        .big-font {
            font-size:200px !important;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<p class="big-font">Hello World !!</p>', unsafe_allow_html=True)

        st.sidebar.title("Price")
        score_price = st.slider("price score",0,100,50)
        weight_price = st.slider("price weight",0,100,50)
        value = coin_list[add_selectbox]["price"]
        st.markdown(f'**Price** = {coin_list[add_selectbox]["price"]}')
        st.metric('Price', "", delta=value, delta_color="normal")



        st.sidebar.title("Volume")
        score_volume = st.sidebar.slider("volume score",0,100,50)
        weight_volume = st.sidebar.slider("volume weight",0,100,50)

        st.sidebar.title("Market Cap")
        score_market_cap = st.sidebar.slider("market_cap score",0,100,50)
        weight_market_cap = st.sidebar.slider("market_cap weight",0,100,50)

        st.sidebar.title("Price change 1h")
        score_pc_1h = st.sidebar.slider("pc_1h score",0,100,50)
        weight_pc_1h = st.sidebar.slider("pc_1h weight",0,100,50)

        st.sidebar.title("Price change 24h")
        score_pc_24h = st.sidebar.slider("pc_24h score",0,100,50)
        weight_pc_24h = st.sidebar.slider("pc_24h weight",0,100,50)

        st.sidebar.title("Price change 7d")
        score_pc_7d = st.sidebar.slider("pc_7d score",0,100,50)
        weight_pc_7d = st.sidebar.slider("pc_7d weight",0,100,50)

        st.sidebar.title("Price change 30d")
        score_pc_30d = st.sidebar.slider("pc_30d score",0,100,50)
        weight_pc_30d = st.sidebar.slider("pc_30d weight",0,100,50)

        st.sidebar.title("Price change 60d")
        score_pc_60d = st.sidebar.slider("pc_60d score",0,100,50)
        weight_pc_60d = st.sidebar.slider("pc_60d weight",0,100,50)

        st.sidebar.title("Price change 90d")
        score_pc_90d = st.sidebar.slider("pc_90d score",0,100,50)
        weight_pc_90d = st.sidebar.slider("pc_90d weight",0,100,50)

        st.sidebar.title("Volume change 24h")
        score_volume_change = st.sidebar.slider("volume_change score",0,100,50)
        weight_volume_change = st.sidebar.slider("volume_change weight",0,100,50)

        st.sidebar.title("Market Cap Dominance")
        score_dominance = st.sidebar.slider("dominance score",0,100,50)
        weight_dominance = st.sidebar.slider("dominance weight",0,100,50)

        st.sidebar.title("Number of Market Pairs")
        score_market_pairs = st.sidebar.slider("market_pairs score",0,100,50)
        weight_market_pairs = st.sidebar.slider("market_pairs weight",0,100,50)

        st.sidebar.title("Circulating Supply")
        score_circulating_supply = st.sidebar.slider("circulating_supply score",0,100,50)
        weight_circulating_supply = st.sidebar.slider("circulating_supply weight",0,100,50)

        st.sidebar.title("Max Supply")
        score_max_supply = st.sidebar.slider("max_supply score",0,100,50)
        weight_max_supply = st.sidebar.slider("max_supply weight",0,100,50)

        st.sidebar.title("Total Supply")
        score_total_supply = st.sidebar.slider("total_supply score",0,100,50)
        weight_total_supply = st.sidebar.slider("total_supply weight",0,100,50)

        

        st.subheader("Current data from coinmarketcap.com:")

        # st.markdown(f'**Price** = {coin_list[add_selectbox]["price"]}')
        st.markdown(f'**Volume** = {coin_list[add_selectbox]["volume"]}')
        st.markdown(f'**Market_cap** = {coin_list[add_selectbox]["market_cap"]}')
        st.markdown(f'**Price change 1h in %** = {coin_list[add_selectbox]["pc_1h"]}')
        st.markdown(f'**Price change 24h in  %** = {coin_list[add_selectbox]["pc_24h"]}')
        st.markdown(f'**Price change 7d in %** = {coin_list[add_selectbox]["pc_7d"]}')
        st.markdown(f'**Price change 30d in %** = {coin_list[add_selectbox]["pc_30d"]}')
        st.markdown(f'**Price change 60d in %** = {coin_list[add_selectbox]["pc_60d"]}')
        st.markdown(f'**Price change 90d in %** = {coin_list[add_selectbox]["pc_90d"]}')
        st.markdown(f'**Volume change 24h in %** = {coin_list[add_selectbox]["volume_change"]}')
        st.markdown(f'**Market cap dominance** = {coin_list[add_selectbox]["dominance"]}')
        st.markdown(f'**Number of market pairs** = {coin_list[add_selectbox]["market_pairs"]}')
        st.markdown(f'**Circulating supply** = {coin_list[add_selectbox]["circulating_supply"]}')
        st.markdown(f'**Max supply** = {coin_list[add_selectbox]["max_supply"]}')
        st.markdown(f'**Total supply** = {coin_list[add_selectbox]["total_supply"]}')


        st.subheader("Weighted Average Calculation:")
        
        sums = sum([weight_price, weight_volume, weight_market_cap, weight_pc_1h, weight_pc_24h, weight_pc_7d, weight_pc_30d, weight_pc_60d, weight_pc_90d, weight_volume_change, weight_dominance, weight_market_pairs, weight_circulating_supply, weight_max_supply, weight_total_supply])
        confidence = round((score_price*weight_price + score_volume*weight_volume + 
                            score_market_cap*weight_market_cap + score_pc_1h*weight_pc_1h + 
                            score_pc_24h*weight_pc_24h + score_pc_7d*weight_pc_7d +
                            score_pc_30d*weight_pc_30d + score_pc_60d*weight_pc_60d +
                            score_pc_90d*weight_pc_90d + score_volume_change*weight_volume_change +
                            score_dominance*weight_dominance + score_market_pairs*weight_market_pairs +
                            score_circulating_supply*weight_circulating_supply + score_max_supply*weight_max_supply +
                            score_total_supply*weight_total_supply)/
                        sums,1)
        coin_risk = 100 - confidence
        # st.markdown(f':point_right:Coin risk level based on the user feedback: **{coin_risk}%**')
        
        if st.button('Calculate'):
            st.metric(label = f"Risk Index for {add_selectbox}", value = f"{round(coin_risk,3)}%")
            
            # save the results in a dataframe

            fmt = "%Y-%m-%d %H:%M:%S %Z%z"
            time_object = datetime.now(timezone('US/Eastern'))
            # results['timestamp'].append(time_object)
            
            results = {'coin':[add_selectbox], 'timestamp':[time_object], 
                       'price $':[coin_list[add_selectbox]["price"]], 'score_price':[score_price], 'weight_price':[weight_price], 
                       'volume $':[coin_list[add_selectbox]["volume"]], 'score_volume':[score_volume], 'weight_volume':[weight_volume],
                       'market_cap $':[coin_list[add_selectbox]["market_cap"]], 'score_market_cap':[score_market_cap], 'weight_market_cap':[weight_market_cap],
                       'pc_1h %':[coin_list[add_selectbox]["pc_1h"]], 'score_pc_1h':[score_pc_1h], 'weight_pc_1h':[weight_pc_1h],
                       'pc_24h %':[coin_list[add_selectbox]["pc_24h"]], 'score_pc_24h':[score_pc_24h], 'weight_pc_24h':[weight_pc_24h],
                       'pc_7d %':[coin_list[add_selectbox]["pc_7d"]], 'score_pc_7d':[score_pc_7d], 'weight_pc_7d':[weight_pc_7d],
                       'pc_30d %':[coin_list[add_selectbox]["pc_30d"]], 'score_pc_30d':[score_pc_30d], 'weight_pc_30d':[weight_pc_30d],
                       'pc_60d %':[coin_list[add_selectbox]["pc_60d"]], 'score_pc_60d':[score_pc_60d], 'weight_pc_60d':[weight_pc_60d],
                       'pc_90d %':[coin_list[add_selectbox]["pc_90d"]], 'score_pc_90d':[score_pc_90d], 'weight_pc_90d':[weight_pc_90d],
                       'volume_change %':[coin_list[add_selectbox]["volume_change"]], 'score_volume_change':[score_volume_change], 'weight_volume_change':[weight_volume_change],
                       'dominance':[coin_list[add_selectbox]["dominance"]], 'score_dominance':[score_dominance], 'weight_dominance':[weight_dominance],
                       'market_pairs':[coin_list[add_selectbox]["market_pairs"]], 'score_market_pairs':[score_market_pairs], 'weight_market_pairs':[weight_market_pairs],
                       'circulating_supply':[coin_list[add_selectbox]["circulating_supply"]], 'score_circulating_supply':[score_circulating_supply], 'weight_circulating_supply':[weight_circulating_supply],
                       'max_supply':[coin_list[add_selectbox]["max_supply"]], 'score_max_supply':[score_max_supply], 'weight_max_supply':[weight_max_supply],
                       'total_supply':[coin_list[add_selectbox]["total_supply"]], 'score_total_supply':[score_total_supply], 'weight_total_supply':[weight_total_supply],
                       'coin_risk %':[coin_risk]}

        
            results_df = pd.DataFrame(results)

            import csv
            with open('results.csv', 'r') as csvfile:
                csv_dict = [row for row in csv.DictReader(csvfile)]
                if len(csv_dict) == 0:
                    results_df.to_csv('results.csv', mode='a', index=False)
                else:
                    results_df.to_csv('results.csv', mode='a', header=False, index=False)
                    
        else:
            pass
        

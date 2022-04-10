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

    selected_coin = st.selectbox(
        "Choose a coin:",
        coin_names
    )
    if selected_coin != 'Select a coin':
        symbol = coin_list[selected_coin]['symbol']
        st.markdown(f"**Symbol** : {symbol}") 
    
    # some design adjustments
    st.write(
        """
        <style>
        [data-testid="stMetricDelta"] svg {
            display: none; 
        } 
        [data-testid="stMetricDelta"] div {
            #border: 1px outset green;
            #background-color: lightblue;
            #text-align: center;
            font-family: 'SmallCaps', sans-serif;
            font-weight: bold;
            color:black;
            font-size: 30px;
            #text-shadow: 0.2em 0.2em /* 0.2em */ silver ;
        }
        [data-testid="stMetricValue"] div {
            font-size: 35px;
        }
        [class="stNumberInput"] div {

            width: 70%;
        }
        [class="stSlider"] div {
            width: 75%;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    Slider_Cursor = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
        width: 2%; </style>''', unsafe_allow_html = True)

    Max_TickBar = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div[data-testid="stTickBarMax"]{
        position: relative; left: 150px; </style>''', unsafe_allow_html = True)

    st.markdown("""
        <style>
        <span style="color:blue">some *blue* text</span>
        .big-font {
            font-size:200px !important;
        }
        </style>
        """, unsafe_allow_html=True)

    if selected_coin != 'Select a coin':
        
        st.subheader(":point_down:Enter a Score and a Weight for each indicator")
        st.markdown("---")

        # Price
        price = coin_list[selected_coin]['price']
        if price is None:
            price = "-"
        else:
            price = "{:,}".format(round(coin_list[selected_coin]['price'], 2))
            
        st.metric(label="", value=f"{selected_coin} Price", delta=f"${price}")
        score_price = st.slider(
            "Please Enter a Score from 0 to 100%",
            min_value = 0,
            max_value = 100,
            value = 50,
            key = 1
        )
        weight_price = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 1
        )
        st.markdown("---")
        
        # Volume
        volume = coin_list[selected_coin]['volume']
        if volume is None:
            volume = "-"
        else:
            volume = "{:,}".format(round(coin_list[selected_coin]['volume'], 2))
            
        st.metric(label="", value=f"{selected_coin} Volume", delta=f"${volume}")
        score_volume = st.slider(
            "Please Enter a Score from 0 to 100%",
            min_value = 0,
            max_value = 100,
            value = 50, 
            key = 2
        )
        weight_volume = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 2
        )
        st.markdown("---")

        # Market Cap
        marketcap = coin_list[selected_coin]['market_cap']
        if marketcap is None:
            marketcap = "-"
        else:
            marketcap = "{:,}".format(round(coin_list[selected_coin]['market_cap'], 2))
            
        st.metric(label="", value=f"{selected_coin} Market Cap", delta=f"${marketcap}")
        score_market_cap = st.slider(
            "Please Enter a Score from 0 to 100%",
            min_value = 0,
            max_value = 100,
            value = 50, 
            key = 3
        )
        weight_market_cap = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 3
        )
        st.markdown("---")
        
        # Price change 1h
        pc_1h = coin_list[selected_coin]['pc_1h']
        if pc_1h is None:
            pc_1h = "-"
        else:
            pc_1h = "{:,}".format(round(coin_list[selected_coin]['pc_1h'], 2))
            
        st.metric(label="", value=f"{selected_coin} Price change 1h", delta=f"% {pc_1h}")
        score_pc_1h = st.slider(
            "Please Enter a Score from 0 to 100%",
            min_value = 0,
            max_value = 100,
            value = 50, 
            key = 4
        )
        weight_pc_1h = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 4
        )
        st.markdown("---")
        
        # Price change 24h
        pc_24h = coin_list[selected_coin]['pc_24h']
        if pc_24h is None:
            pc_24h = "-"
        else:
            pc_24h = "{:,}".format(round(coin_list[selected_coin]['pc_24h'], 2))
            
        st.metric(label="", value=f"{selected_coin} Price change 24h", delta=f"% {pc_24h}")
        score_pc_24h = st.slider(
            "Please Enter a Score from 0 to 100%",
            min_value = 0,
            max_value = 100,
            value = 50, 
            key = 5
        )
        weight_pc_24h = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 5
        )
        st.markdown("---")

        # Price change 7d
        pc_7d = coin_list[selected_coin]['pc_7d']
        if pc_7d is None:
            pc_7d = "-"
        else:
            pc_7d = "{:,}".format(round(coin_list[selected_coin]['pc_7d'], 2))
            
        st.metric(label="", value=f"{selected_coin} Price change 7d", delta=f"% {pc_7d}")
        score_pc_7d = st.slider(
            "Please Enter a Score from 0 to 100%",
            min_value = 0,
            max_value = 100,
            value = 50, 
            key = 6
        )
        weight_pc_7d = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 6
        )
        st.markdown("---")
        
        # Price change 30d
        pc_30d = coin_list[selected_coin]['pc_30d']
        if pc_30d is None:
            pc_30d = "-"
        else:
            pc_30d = "{:,}".format(round(coin_list[selected_coin]['pc_30d'], 2))
            
        st.metric(label="", value=f"{selected_coin} Price change 30d", delta=f"% {pc_30d}")
        score_pc_30d = st.slider(
            "Please Enter a Score from 0 to 100%",
            min_value = 0,
            max_value = 100,
            value = 50, 
            key = 7
        )
        weight_pc_30d = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 7
        )
        st.markdown("---")

        # Price change 60d
        pc_60d = coin_list[selected_coin]['pc_60d']
        if pc_60d is None:
            pc_60d = "-"
        else:
            pc_60d = "{:,}".format(round(coin_list[selected_coin]['pc_60d'], 2))
            
        st.metric(label="", value=f"{selected_coin} Price change 60d", delta=f"% {pc_60d}")
        score_pc_60d = st.slider(
            "Please Enter a Score from 0 to 100%",
            min_value = 0,
            max_value = 100,
            value = 50, 
            key = 8
        )
        weight_pc_60d = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 8
        )
        st.markdown("---")

        # Price change 90d
        pc_90d = coin_list[selected_coin]['pc_90d']
        if pc_90d is None:
            pc_90d = "-"
        else:
            pc_90d = "{:,}".format(round(coin_list[selected_coin]['pc_90d'], 2))
            
        st.metric(label="", value=f"{selected_coin} Price change 90d", delta=f"% {pc_90d}")
        score_pc_90d = st.slider(
            "Please Enter a Score from 0 to 100%",
            min_value = 0,
            max_value = 100,
            value = 50, 
            key = 9
        )
        weight_pc_90d = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 9
        )
        st.markdown("---")
        
        # Volume change 24h
        volume_change = coin_list[selected_coin]['volume_change']
        if volume_change is None:
            volume_change = "-"
        else:
            volume_change = "{:,}".format(round(coin_list[selected_coin]['volume_change'], 2))
            
        st.metric(label="", value=f"{selected_coin} Volume change 24h", delta=f"% {volume_change}")
        score_volume_change = st.slider(
            "Please Enter a Score from 0 to 100%",
            min_value = 0,
            max_value = 100,
            value = 50, 
            key = 10
        )
        weight_volume_change = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 10
        )
        st.markdown("---")

        # Dominance        
        dominance = coin_list[selected_coin]['dominance']
        if dominance is None:
            dominance = "-"
        else:
            dominance = "{:,}".format(round(coin_list[selected_coin]['dominance'], 2))
            
        st.metric(label="", value=f"{selected_coin} Dominance", delta=f"% {dominance}")
        score_dominance = st.slider(
            "Please Enter a Score from 0 to 100%",
            min_value = 0,
            max_value = 100,
            value = 50, 
            key = 11
        )
        weight_dominance = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 11
        )
        st.markdown("---")

        # Number of Market Pairs
        market_pairs = coin_list[selected_coin]['market_pairs']
        if market_pairs is None:
            market_pairs = "-"
        else:
            market_pairs = coin_list[selected_coin]['market_pairs']
        
        st.metric(label="", value=f"{selected_coin} Count of Market Pairs", delta=f"{market_pairs}")
        score_market_pairs = st.slider(
            "Please Enter a Score from 0 to 100%",
            min_value = 0,
            max_value = 100,
            value = 50, 
            key = 12
        )
        weight_market_pairs = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 12
        )
        st.markdown("---")

        # Circulating Supply        
        circulating_supply = coin_list[selected_coin]['circulating_supply']
        if circulating_supply is None:
            circulating_supply = "-"
        else:
            circulating_supply = "{:,}".format(coin_list[selected_coin]['circulating_supply'])
            
        st.metric(label="", value=f"{selected_coin} Circulating Supply", delta=f"{circulating_supply} {symbol}")
        score_circulating_supply = st.slider(
            "Please Enter a Score from 0 to 100%",
            min_value = 0,
            max_value = 100,
            value = 50, 
            key = 13
        )
        weight_circulating_supply = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 13
        )
        st.markdown("---")
        
        # Max Supply
        max_supply = coin_list[selected_coin]['max_supply']
        if max_supply is None:
            max_supply = "-"
        else:
            max_supply = "{:,}".format(coin_list[selected_coin]['max_supply'])
            
        st.metric(label="", value=f"{selected_coin} Max Supply", delta=f"{max_supply} {symbol}")
        score_max_supply = st.slider(
            "Please Enter a Score from 0 to 100%",
            min_value = 0,
            max_value = 100,
            value = 50, 
            key = 14
        )
        weight_max_supply = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 14
        )
        st.markdown("---")
        
        # Total Supply
        total_supply = coin_list[selected_coin]['total_supply']
        if total_supply is None:
            total_supply = "-"
        else:
            total_supply = "{:,}".format(coin_list[selected_coin]['total_supply'])
            
        st.metric(label="", value=f"{selected_coin} Total Supply", delta=f"{total_supply} {symbol}")
        score_total_supply = st.slider(
            "Please Enter a Score from 0 to 100%",
            min_value = 0,
            max_value = 100,
            value = 50, 
            key = 15
        )
        weight_total_supply = st.number_input(
            "Please Enter a Weight from 0 to 10:",
            min_value = 0,
            max_value = 10,
            step = 1,
            key = 15
        )
        st.markdown("---")


        # CALCULATING RESULTS
        # st.subheader("Weighted Average Calculation:")
        
        if st.button('Calculate'):
            
            # calculate and display the results
            sums = sum([weight_price, weight_volume, weight_market_cap, weight_pc_1h, weight_pc_24h, weight_pc_7d, weight_pc_30d, weight_pc_60d, weight_pc_90d, weight_volume_change, weight_dominance, weight_market_pairs, weight_circulating_supply, weight_max_supply, weight_total_supply])
            print(sums)
            if sums == 0:
                st.write('Please, enter the weights properly.')
            else:
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

                st.markdown(":star:")
                st.metric(label = f"Risk Index for {selected_coin}", value = f"{round(coin_risk,3)}%")
                

            
                # SAVE THE RESULTS IN CSV FILE

                fmt = "%Y-%m-%d %H:%M:%S %Z%z"
                time_object = datetime.now(timezone('US/Eastern'))
                
                results = {'coin':[selected_coin], 'timestamp':[time_object], 
                        'price $':[coin_list[selected_coin]["price"]], 'score_price':[score_price], 'weight_price':[weight_price], 
                        'volume $':[coin_list[selected_coin]["volume"]], 'score_volume':[score_volume], 'weight_volume':[weight_volume],
                        'market_cap $':[coin_list[selected_coin]["market_cap"]], 'score_market_cap':[score_market_cap], 'weight_market_cap':[weight_market_cap],
                        'pc_1h %':[coin_list[selected_coin]["pc_1h"]], 'score_pc_1h':[score_pc_1h], 'weight_pc_1h':[weight_pc_1h],
                        'pc_24h %':[coin_list[selected_coin]["pc_24h"]], 'score_pc_24h':[score_pc_24h], 'weight_pc_24h':[weight_pc_24h],
                        'pc_7d %':[coin_list[selected_coin]["pc_7d"]], 'score_pc_7d':[score_pc_7d], 'weight_pc_7d':[weight_pc_7d],
                        'pc_30d %':[coin_list[selected_coin]["pc_30d"]], 'score_pc_30d':[score_pc_30d], 'weight_pc_30d':[weight_pc_30d],
                        'pc_60d %':[coin_list[selected_coin]["pc_60d"]], 'score_pc_60d':[score_pc_60d], 'weight_pc_60d':[weight_pc_60d],
                        'pc_90d %':[coin_list[selected_coin]["pc_90d"]], 'score_pc_90d':[score_pc_90d], 'weight_pc_90d':[weight_pc_90d],
                        'volume_change %':[coin_list[selected_coin]["volume_change"]], 'score_volume_change':[score_volume_change], 'weight_volume_change':[weight_volume_change],
                        'dominance':[coin_list[selected_coin]["dominance"]], 'score_dominance':[score_dominance], 'weight_dominance':[weight_dominance],
                        'market_pairs':[coin_list[selected_coin]["market_pairs"]], 'score_market_pairs':[score_market_pairs], 'weight_market_pairs':[weight_market_pairs],
                        'circulating_supply':[coin_list[selected_coin]["circulating_supply"]], 'score_circulating_supply':[score_circulating_supply], 'weight_circulating_supply':[weight_circulating_supply],
                        'max_supply':[coin_list[selected_coin]["max_supply"]], 'score_max_supply':[score_max_supply], 'weight_max_supply':[weight_max_supply],
                        'total_supply':[coin_list[selected_coin]["total_supply"]], 'score_total_supply':[score_total_supply], 'weight_total_supply':[weight_total_supply],
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
            st.write('Click the button to calculate the risk.')
        

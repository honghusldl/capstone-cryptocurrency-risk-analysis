import streamlit as st
from functions import get_crypto_api, get_coin_list

def user_analysis():
# # BUILDING THE WEB PAGE
# st.title ("Risk tolerance assessment")
    coin_list = get_coin_list(get_crypto_api())
    coin_names = list(coin_list.keys())
    coin_names.insert(0, "Select a coin")
    print('hi')

    add_selectbox = st.selectbox(
        "Choose a coin:",
        coin_names
    )


    if add_selectbox != 'Select a coin':

        st.sidebar.title("Price")
        score1 = st.sidebar.slider("#1 score",0,100,50)
        weight1 = st.sidebar.slider("#1 weight",0,100,50)

        st.sidebar.title("Volume")
        score2 = st.sidebar.slider("#2 score",0,100,50)
        weight2 = st.sidebar.slider("#2 weight",0,100,50)

        st.sidebar.title("Market Cap")
        score3 = st.sidebar.slider("#3 score",0,100,50)
        weight3 = st.sidebar.slider("#3 weight",0,100,50)

        st.sidebar.title("Price change 1h")
        score4 = st.sidebar.slider("#4 score",0,100,50)
        weight4 = st.sidebar.slider("#4 weight",0,100,50)

        st.sidebar.title("Price change 24h")
        score5 = st.sidebar.slider("#5 score",0,100,50)
        weight5 = st.sidebar.slider("#5 weight",0,100,50)

        st.sidebar.title("Price change 7d")
        score6 = st.sidebar.slider("#6 score",0,100,50)
        weight6 = st.sidebar.slider("#6 weight",0,100,50)

        st.sidebar.title("Price change 30d")
        score7 = st.sidebar.slider("#7 score",0,100,50)
        weight7 = st.sidebar.slider("#7 weight",0,100,50)

        st.sidebar.title("Price change 60d")
        score8 = st.sidebar.slider("#8 score",0,100,50)
        weight8 = st.sidebar.slider("#8 weight",0,100,50)

        st.sidebar.title("Price change 90d")
        score9 = st.sidebar.slider("#9 score",0,100,50)
        weight9 = st.sidebar.slider("#9 weight",0,100,50)

        st.sidebar.title("Volume change 24h")
        score10 = st.sidebar.slider("#10 score",0,100,50)
        weight10 = st.sidebar.slider("#10 weight",0,100,50)

        st.sidebar.title("Market Cap Dominance")
        score11 = st.sidebar.slider("#11 score",0,100,50)
        weight11 = st.sidebar.slider("#11 weight",0,100,50)

        st.sidebar.title("Number of Market Pairs")
        score12 = st.sidebar.slider("#12 score",0,100,50)
        weight12 = st.sidebar.slider("#12 weight",0,100,50)

        st.sidebar.title("Circulating Supply")
        score13 = st.sidebar.slider("#13 score",0,100,50)
        weight13 = st.sidebar.slider("#13 weight",0,100,50)

        st.sidebar.title("Max Supply")
        score14 = st.sidebar.slider("#14 score",0,100,50)
        weight14 = st.sidebar.slider("#14 weight",0,100,50)

        st.sidebar.title("Total Supply")
        score15 = st.sidebar.slider("#15 score",0,100,50)
        weight15 = st.sidebar.slider("#15 weight",0,100,50)

        

        st.subheader("Current data from coinmarketcap.com:")

        st.markdown(f'**Price** = {coin_list[add_selectbox]["price"]}')
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
        
        sums = sum([weight1, weight2, weight3, weight4, weight5, weight6, weight7, weight8, weight9, weight10, weight11, weight12, weight13, weight14, weight15])
        confidence = round((score1*weight1 + score2*weight2 + 
                            score3*weight3 + score4*weight4 + 
                            score5*weight5 + score6*weight6 +
                            score5*weight5 + score6*weight6 +
                            score7*weight7 + score8*weight8 +
                            score9*weight9 + score10*weight10 +
                            score11*weight11 + score12*weight12 +
                            score13*weight13 + score14*weight14 +
                            score15*weight15)/
                        sums,1)
        coin_risk = 100 - confidence
        # st.markdown(f':point_right:Coin risk level based on the user feedback: **{coin_risk}%**')
        st.metric(label = f"Risk Index for {add_selectbox}", value = f"{round(coin_risk,3)}%")

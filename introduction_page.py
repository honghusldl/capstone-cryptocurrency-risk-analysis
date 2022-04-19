import streamlit as st
from PIL import Image

def introduction():
    #st.title(":currency_exchange:Crypto Risk Tolerance Assessment")

    st.markdown("The Risk Calculator is a tool that allows users to evaluate \
        the risk associated with a crypto coin of their choice and assist them in making investment decisions. \
        \nThis project uses two approaches that provide two individual risk scores.")
    
    col1, col2, col3 = st.columns((0.3,1,0.3))
    col2.image("coin.gif")
    
    # APPROACH 1
    st.header("Approach 1: User Analysis")
    st.markdown(
        "In this approach, users are able to evaluate their risk appetite on 15 coin indicators pulled \
        in real-time from [coinmarketcap.com](https://coinmarketcap.com). Once on the User Analysis page, the user is expected to individually \
        assess each indicator of a chosen coin by giving it a Score (see *Definitions* below) from 1% to 100% and a Weight \
        (see *Definitions* below) from 1 to 10 (or N/A). \
        Once all the Score and Weights are collected, the final results are calculated using a Weighted Average formula below:"
    )
    col1, col2 = st.columns((0.3,1))
    col1.image('formula.jpg')
    col2.markdown("'w' - weights applied to X values\
                  \n'X' - scores to be averaged\
                  \n 'n' - number of terms to be averaged"
                  )
    st.markdown("This calculator allows users to determine their personal \
         risk tolerance based solely on their feedback on the data of the crypto coin in real-time."
         )
    
    # Definitions
    st.markdown("##### *Definitions:* \
        \n**Score**: The user gives a score based on how they perceive the performance of a particular feature \
            (i.e., the trading volume went up by 10,000 points; the user considers that an outstanding performance, \
            which is why they might give it a high score of 100%) \
        \n**Weight**: The user assigns a weight to a particular feature according to its perceived importance or value \
            (i.e., the user doesn't care about trading volume, so despite giving it a high score in performance, \
            they might give it a weight of 1) \
        \n**Beta**: It is a financial term used to describe the correlated volatility of one equity to another over a specific \
            period of time. Typically, that correlation is to the crypto market for the past 30 trading days. The key word is correlated. \
            If a coin has a beta of 1, that means that it is perfectly correlated with the crypto market. So, if the market went down 1%, we see \
            that the coin also moved down 1%. \
            If a coin had a beta of 2, that would imply that it moves in the same direction as the crypto market, but by twice as much.  \
            In this case, it is correct to say that the equity would be more volatile than the market. In fact, \
            it would be twice as volatile. \
            Note: in this project, in the absence of reliable data of the overall crypto market movements, \
            the movement of Bitcoin is taken as a benchmark instead. \
            ")

    
    # APPROACH 2
    st.header("Approach 2: Distribution Analysis")
    st.markdown(
        "In this approach, the risk is calculated based on the coin's volatility. \
        For this, cryptocurrency price and volume history are pulled in real-time from [coinmarketcap.com](https://coinmarketcap.com).\
        After the user chooses a coin of their liking, a histogram is being built for each of the 6 categories reflecting the coin's \
        historical price and volume changes, such as 24 hours price change (%), 7 days price change (%), etc. \
        The idea behind building a histogram is simple: the farther away from the center of the histogram a value falls, \
        the greater is the coin's price/volume change, and the higher is its overall risk. In this regard, \
        even a positive jump in the price will be considered risky because more often than not, the market follows the pendulum principle:\
        when a price reaches an extreme in its momentum, it turns around. \
        \nA more detailed technical explanation of the underlying analysis is given below."
        )
    
    # Technical details
    st.markdown("#### Technical Explanation:")
    st.markdown("An example of a typical distribution used in the analysis is shown on the picture:")
    st.image("distribution.jpg", caption='BTC Price 24h change')
    st.markdown("In the picture, the horizontal x-axis represents the price change in % \
        and the vertical y-axis represents the density of the values. The example here \
        shows a beautiful symmetrical price distribution for Bitcoin's historical 24 hours price change. \
        We can see that most often, BTC was showing near 0% price change throughout the history \
        of its existence. The farther away from the center a value falls, the higher the risk of the coin's \
        volatility for the observing period. However, be mindful that such symmetry as presented in the picture \
        is not always the case and can vary from coin to coin. \
        \n Next, the algorithm (with the help of Python SciPy package) decides which probability distribution \
        fits the set of data the best. In this case, it is the Cauchy distribution (represented in orange colour). \
        Each distribution has its own unique formula that will be used in the following calculations. \
        \n Once the current value of the Price 24h Change is pulled from Coinmarketcap, it is plugged into the formula \
        determined by the algorithm. The resulting value represents the corresponding density from the y-axis.\
        The density is then normalized and stored as a volatility risk assessment result for this particular distribution. \
        \n The user is then prompted to enter a Weight for each of the indicators to adjust their preferences. \
        Those weights will be plugged into the weighted average formula, and the final result will be presented to the user. \
        \n This approach allows the user to get an idea of a coin's riskiness based on its volatility \
        and estimate its future price and volume fluctuations."
        )
    
    st.markdown("#### Result Explanation:")
    st.markdown('''Investing in riskier assets can pay off in a big way, 
        as it offers you the chance to benefit from higher returns. However, 
        high volatility also presents the danger of a sudden price drop and, 
        therefore, should be regarded with caution.  \n\nNote: volatility alone is 
        rarely a reason to buy or sell. You have to look at the investment overall 
        to make an educated decision.''')

    st.sidebar.info("This Cryptocurrency risk estimation tool is designed and built by Team Humber Coin. Team members: Fadumo Diriye, Honghu Li, Nadiia Pavlovska & Sminu Mathew.")



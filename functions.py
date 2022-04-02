
import streamlit as st
# Data Processing
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from fitter import Fitter, get_common_distributions, get_distributions

# api for web scraping coinmarketcap
from cryptocmd import CmcScraper

# crypto api
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# get distributions from scipy
from scipy.stats import cauchy,chi2,expon,exponpow,gamma,lognorm,norm,powerlaw,rayleigh,uniform

@st.cache
def get_crypto_api():
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'USD',
    'sort':'market_cap',
    'sort_dir':'desc',
    'circulating_supply_max':'100000000000000000',
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '', # replace with personal API key
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    #print(data)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

  return data

def get_coin_list(data):
  coin_list = {}
  for i in range(5000):
    name = data['data'][i]['name']
    symbol = data['data'][i]['symbol']
    id = data['data'][i]['id']
    circulating_supply = data['data'][i]['circulating_supply']
    max_supply = data['data'][i]['max_supply']
    total_supply = data['data'][i]['total_supply']
    market_pairs = data['data'][i]['num_market_pairs']
    market_cap = data['data'][i]['quote']['USD']['market_cap']
    dominance = data['data'][i]['quote']['USD']['market_cap_dominance']
    price =  data['data'][i]['quote']['USD']['price']
    pc_1h = data['data'][i]['quote']['USD']['percent_change_1h']
    pc_24h = data['data'][i]['quote']['USD']['percent_change_24h']
    pc_7d = data['data'][i]['quote']['USD']['percent_change_7d']
    pc_30d =  data['data'][i]['quote']['USD']['percent_change_30d']
    pc_60d =  data['data'][i]['quote']['USD']['percent_change_60d']
    pc_90d =  data['data'][i]['quote']['USD']['percent_change_90d']
    volume =  data['data'][i]['quote']['USD']['volume_24h']
    volume_change =  data['data'][i]['quote']['USD']['volume_change_24h']
    # coin_list[name] = [id, symbol,circulating_supply, max_supply, total_supply, market_pairs, market_cap, dominance, price, pc_1h, pc_24h, pc_7d, pc_30d, pc_60d,pc_90d, volume, volume_change ]
    coin_list[name] = {}
    
    coin_list[name]["symbol"] = symbol
    coin_list[name]["id"] = id
    coin_list[name]["circulating_supply"] = circulating_supply
    coin_list[name]["max_supply"] = max_supply
    coin_list[name]["total_supply"] = total_supply
    coin_list[name]["market_pairs"] = market_pairs
    coin_list[name]["market_cap"] = market_cap
    coin_list[name]["dominance"] = dominance
    coin_list[name]["price"] = price
    coin_list[name]["pc_1h"] = pc_1h
    coin_list[name]["pc_24h"] = pc_24h
    coin_list[name]["pc_7d"] = pc_7d
    coin_list[name]["pc_30d"] = pc_30d
    coin_list[name]["pc_60d"] = pc_60d
    coin_list[name]["pc_90d"] = pc_90d
    coin_list[name]["volume"] = volume
    coin_list[name]["volume_change"] = volume_change

  return coin_list

def get_historical_data(symbol):
  # initialise scraper without time interval
  scraper = CmcScraper(symbol)

  # get raw data as list of list
  headers, data = scraper.get_data()

  # get data in a json format
  xrp_json_data = scraper.get_data("json")

  # # export the data as csv file, you can also pass optional `name` parameter
  # scraper.export("csv", name="bit_all_time")

  # Pandas dataFrame for the same data
  df = scraper.get_dataframe()

  return df

def plot_distributions(df):
  df_visual = df.replace(np.nan,0)

  if np.isinf(df).values.sum() > 0:
    df_visual.replace([np.inf, -np.inf], 0, inplace = True)

  fig, axes = plt.subplots(9,2, figsize = (20,50))
  row_num = 0

  for col in df.drop(columns = 'date').columns:
    sns.histplot(data = df_visual, x = col, ax = axes[row_num][0])
    sns.lineplot(data = df_visual, x = 'date', y = col, ax = axes[row_num][1])
    row_num += 1

def get_max_density(df, column):
  if np.isinf(df).values.sum() > 0:
    df_density = df.replace([np.inf, -np.inf], np.nan)
  
  else:
    df_density = df.copy()
  
  hist = plt.hist(df_density[column].dropna(), bins = 200, density = True)
  density, bins, patches = hist
  plt.close()
  return density.max()

def get_name_parameters(best_dist, column):
  return next(iter(best_dist[column])), next(iter(best_dist[column].values()))

'''cauchy,
 chi2,
 expon,
 exponpow,
 gamma,
 lognorm,
 norm,
 powerlaw,
 rayleigh,
 uniform'''

def cauchy_pdf(x, parameters):
  return cauchy.pdf(x = x, loc = parameters['loc'], scale = parameters['scale'])

def chi2_pdf(x, parameters):
  return chi2.pdf(x = x, df = parameters['df'], loc = parameters['loc'], scale = parameters['scale'])

def expon_pdf(x ,parameters):
  return expon.pdf(x = x, loc = parameters['loc'], scale = parameters['scale'])

def exponpow_pdf(x, parameters):
  return exponpow.pdf(x = x, b = parameters['b'], loc = parameters['loc'], scale = parameters['scale'])

def gamma_pdf(x, parameters):
  return gamma.pdf(x = x, a = parameters['a'], loc = parameters['loc'], scale = parameters['scale'])

def lognorm_pdf(x, parameters):
  return lognorm.pdf(x = x, s = parameters['s'], loc = parameters['loc'], scale = parameters['scale'])

def norm_pdf(x, parameters):
  return norm.pdf(x = x, loc = parameters['loc'], scale = parameters['scale'])

def powerlaw_pdf(x, parameters):
  return powerlaw.pdf(x = x, a = parameters['a'], loc = parameters['loc'], scale = parameters['scale'])

def rayleigh_pdf(x, parameters):
  return rayleigh.pdf(x = x, loc= parameters['loc'], scale = parameters['scale'])

def uniform_pdf(x, parameters):
  return uniform.pdf(x = x, loc = parameters['loc'], scale = parameters['scale'])

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

def data_wrangling(df):
      # data cleaning
    df.drop(['Open','High','Low'], axis = 1, inplace = True)

    df['close_24h'] = df['Close'].shift(periods = -1)
    df['close_7d'] = df['Close'].shift(periods = -7)
    df['close_30d'] = df['Close'].shift(periods = -30)
    df['close_60d'] = df['Close'].shift(periods = -60)
    df['close_90d'] = df['Close'].shift(periods = -90)
    df['volume_24h'] = df['Volume'].shift(periods = -1)

    df['%price_change_24h'] =   (  df['Close'] / df['close_24h'] - 1 ) * 100
    df['%price_change_7d'] =  (  df['Close'] /  df['close_7d'] - 1 ) * 100
    df['%price_change_30d'] =   (  df['Close'] / df['close_30d'] - 1 ) * 100
    df['%price_change_60d'] =   (  df['Close'] / df['close_60d'] - 1 ) * 100
    df['%price_change_90d'] =   (  df['Close'] / df['close_90d'] - 1 ) * 100
    df['%volume_change_24h'] =   (df['Volume'] / df['volume_24h'] - 1 ) * 100

    df.drop(['close_24h','close_7d','close_30d','close_60d','close_90d','volume_24h'], 
            axis = 1, inplace = True)
    df.rename({'Close':'price'}, axis = 1, inplace = True)
    df.columns = df.columns.str.lower()
    df.fillna(0, inplace = True)

    return df

@st.cache
def find_best_distribution(df):
  best_dist = {}

  for col in df.drop('date',axis = 1).columns:
    f = Fitter(
        df[col].dropna().values,
        distributions = get_common_distributions(),
        bins = 200
    )

    f.fit()
    best_dist[col] = f.get_best(method= 'sumsquare_error')

  return best_dist

import os
from functools import reduce
import random

# Data Processing
import numpy as np
import pandas as pd
import datetime as dt

import seaborn as sns
import matplotlib.pyplot as plt
# !pip install fitter
from fitter import Fitter, get_common_distributions, get_distributions

# api for web scraping coinmarketcap
from cryptocmd import CmcScraper

# crypto api
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# get distributions from scipy
from scipy.stats import cauchy,chi2,expon,exponpow,gamma,lognorm,norm,powerlaw,rayleigh,uniform

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

def get_name_parameters(column):
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

def chi2_pdf(x, parameters, data):
  df = (data.shape[0]-1) * (data.shape[1]-1)
  return chi2.pdf(x = x, df = df, loc = parameters['loc'], scale = parameters['scale'])

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

